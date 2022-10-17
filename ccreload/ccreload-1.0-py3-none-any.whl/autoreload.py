import functools
import itertools
import os
import signal
import subprocess
import sys
import threading
import time
import traceback
import weakref
from collections import defaultdict
from pathlib import Path
from types import ModuleType
from zipimport import zipimporter

class Apps:
    def __init__(self):
        self.ready_event = threading.Event()
apps = Apps()

from .Signal import Signal

autoreload_started = Signal()
file_changed = Signal()

AUTORELOAD_ENV = "RUN_MAIN"


_error_files = []
_exception = None

try:
    import termios
except ImportError:
    termios = None

def check_errors(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        global _exception
        try:
            fn(*args, **kwargs)
        except Exception:
            _exception = sys.exc_info()

            et, ev, tb = _exception

            if getattr(ev, "filename", None) is None:
                filename = traceback.extract_tb(tb)[-1][0]
            else:
                filename = ev.filename

            if filename not in _error_files:
                _error_files.append(filename)

            # raise

    return wrapper


def ensure_echo_on():
    if not termios or not sys.stdin.isatty():
        return
    attr_list = termios.tcgetattr(sys.stdin)
    if not attr_list[3] & termios.ECHO:
        attr_list[3] |= termios.ECHO
        if hasattr(signal, "SIGTTOU"):
            old_handler = signal.signal(signal.SIGTTOU, signal.SIG_IGN)
        else:
            old_handler = None
        termios.tcsetattr(sys.stdin, termios.TCSANOW, attr_list)
        if old_handler is not None:
            signal.signal(signal.SIGTTOU, old_handler)


def iter_all_python_module_files():
    keys = sorted(sys.modules)
    modules = tuple(
        m
        for m in map(sys.modules.__getitem__, keys)
        if not isinstance(m, weakref.ProxyTypes)
    )
    return iter_modules_and_files(modules, frozenset(_error_files))


@functools.lru_cache(maxsize=1)
def iter_modules_and_files(modules, extra_files):
    sys_file_paths = []
    for module in modules:
        if not isinstance(module, ModuleType):
            continue
        if module.__name__ in ("__main__", "__mp_main__"):
            if hasattr(module, "__file__"):
                sys_file_paths.append(module.__file__)
            continue
        if getattr(module, "__spec__", None) is None:
            continue
        spec = module.__spec__
        if spec.has_location:
            origin = (
                spec.loader.archive
                if isinstance(spec.loader, zipimporter)
                else spec.origin
            )
            sys_file_paths.append(origin)

    results = set()
    for filename in itertools.chain(sys_file_paths, extra_files):
        if not filename:
            continue
        path = Path(filename)
        try:
            if not path.exists():
                continue
        except ValueError as e:
            continue
        resolved_path = path.resolve().absolute()
        results.add(resolved_path)
    return frozenset(results)


@functools.lru_cache(maxsize=1)
def common_roots(paths):
    path_parts = sorted([x.parts for x in paths], key=len, reverse=True)
    tree = {}
    for chunks in path_parts:
        node = tree
        for chunk in chunks:
            node = node.setdefault(chunk, {})
        node.clear()

    def _walk(node, path):
        for prefix, child in node.items():
            yield from _walk(child, path + (prefix,))
        if not node:
            yield Path(*path)

    return tuple(_walk(tree, ()))


def sys_path_directories():
    for path in sys.path:
        path = Path(path)
        if not path.exists():
            continue
        resolved_path = path.resolve().absolute()
        # If the path is a file (like a zip file), watch the parent directory.
        if resolved_path.is_file():
            yield resolved_path.parent
        else:
            yield resolved_path


def get_child_arguments():
    import __main__

    py_script = Path(sys.argv[0])

    args = [sys.executable] + ["-W%s" % o for o in sys.warnoptions]
    if sys.implementation.name == "cpython":
        args.extend(
            f"-X{key}" if value is True else f"-X{key}={value}"
            for key, value in sys._xoptions.items()
        )
    if getattr(__main__, "__spec__", None) is not None:
        spec = __main__.__spec__
        if (spec.name == "__main__" or spec.name.endswith(".__main__")) and spec.parent:
            name = spec.parent
        else:
            name = spec.name
        args += ["-m", name]
        args += sys.argv[1:]
    elif not py_script.exists():
        exe_entrypoint = py_script.with_suffix(".exe")
        if exe_entrypoint.exists():
            return [exe_entrypoint, *sys.argv[1:]]
        script_entrypoint = py_script.with_name("%s-script.py" % py_script.name)
        if script_entrypoint.exists():
            return [*args, script_entrypoint, *sys.argv[1:]]
        raise RuntimeError("Script %s does not exist." % py_script)
    else:
        args += sys.argv
    return args


def trigger_reload(filename):
    sys.exit(3)


def restart_with_reloader():
    new_environ = {**os.environ, AUTORELOAD_ENV: "true"}
    args = get_child_arguments()
    while True:
        p = subprocess.run(args, env=new_environ, close_fds=False)
        if p.returncode != 3:
            return p.returncode


class BaseReloader:
    def __init__(self):
        self.extra_files = set()
        self.directory_globs = defaultdict(set)
        self._stop_condition = threading.Event()

    def watch_dir(self, path, glob):
        path = Path(path)
        try:
            path = path.absolute()
        except FileNotFoundError:
            return
        self.directory_globs[path].add(glob)

    def watched_files(self, include_globs=True):
        yield from iter_all_python_module_files()
        yield from self.extra_files
        if include_globs:
            for directory, patterns in self.directory_globs.items():
                for pattern in patterns:
                    yield from directory.glob(pattern)

    def wait_for_apps_ready(self, app_reg, main_thread):
        while main_thread.is_alive():
            if app_reg.ready_event.wait(timeout=0.1):
                return True
        else:
            return False

    def run(self, main_thread):
        self.wait_for_apps_ready(apps, main_thread)
        from django.urls import get_resolver
        try:
            get_resolver().urlconf_module
        except Exception:
            pass
        autoreload_started.send(sender=self)
        self.run_loop()

    def run_loop(self):
        ticker = self.tick()
        while not self.should_stop:
            try:
                next(ticker)
            except StopIteration:
                break
        self.stop()

    def tick(self):
        raise NotImplementedError("subclasses must implement tick().")

    @classmethod
    def check_availability(cls):
        raise NotImplementedError("subclasses must implement check_availability().")

    def notify_file_changed(self, path):
        results = file_changed.send(sender=self, file_path=path)
        if not any(res[1] for res in results):
            trigger_reload(path)

    @property
    def should_stop(self):
        return self._stop_condition.is_set()

    def stop(self):
        self._stop_condition.set()


class StatReloader(BaseReloader):
    SLEEP_TIME = 0.2  # Check for changes once per second.

    def tick(self):
        mtimes = {}
        while True:
            for filepath, mtime in self.snapshot_files():
                old_time = mtimes.get(filepath)
                mtimes[filepath] = mtime
                if old_time is None:
                    continue
                elif mtime > old_time:
                    self.notify_file_changed(filepath)

            time.sleep(self.SLEEP_TIME)
            yield

    def snapshot_files(self):
        seen_files = set()
        for file in self.watched_files():
            if file in seen_files:
                continue
            try:
                mtime = file.stat().st_mtime
            except OSError:
                continue
            seen_files.add(file)
            yield file, mtime

    @classmethod
    def check_availability(cls):
        return True


class WatchmanUnavailable(RuntimeError):
    pass

def get_reloader():
    return StatReloader()


def start_reloader(reloader, main_func, *args, **kwargs):
    ensure_echo_on()

    main_func = check_errors(main_func)
    main_thread = threading.Thread(
        target=main_func, args=args, kwargs=kwargs, name="main-thread"
    )
    main_thread.daemon = True
    main_thread.start()

    while not reloader.should_stop:
        try:
            reloader.run(main_thread)
        except WatchmanUnavailable as ex:
            reloader = StatReloader()


def run_with_reloader(main_func, *args, **kwargs):
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    try:
        if os.environ.get(AUTORELOAD_ENV) == "true":

            # import pdb
            # pdb.set_trace()
            reloader = get_reloader()
            start_reloader(reloader, main_func, *args, **kwargs)
        else:
            exit_code = restart_with_reloader()
            sys.exit(exit_code)
    except KeyboardInterrupt:
        pass
