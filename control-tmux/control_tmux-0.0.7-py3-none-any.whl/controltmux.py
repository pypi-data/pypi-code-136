#!/usr/bin/python3

#
# control-tmux: Wrapper script around tmux that enables quickly switching between
# sessions, history saving and loading.
#
# Copyright 2018 Katie Rust (https://ktpanda.org)
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list
# of conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import sys
import re
import tempfile
import time
import traceback
import argparse

import os
import select
import subprocess
import errno
from collections import deque, defaultdict
from pathlib import Path
import zipfile

VERSION = "0.0.1"

RETRY_ERRNO = {errno.EAGAIN, errno.EINTR}

RESTORE_SCRIPT = '''\
cd "$pwd"
history -c
history -r "$histf"
echo -ne '\\033c'
echo "=== $name ==="
rm -f "$tempf" "$histf"
unset pwd histf tempf name
_cmd_writehist &> /dev/null
'''

RX_PANE = re.compile(r'(\d+)\.(\d+)=(\d+)')

def runproc(args, capture=False, **kw):
    if capture:
        return subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8', errors='ignore', **kw)
    else:
        return subprocess.run(args, **kw)

def get_ssh_sock(host):
    return Path.home() / '.ssh' / (f'control-{host}')

class SessionNotFoundError(Exception):
    pass

class SessionLogger:
    def __init__(self, sock, save_path, debug=False, notify_pipe=None):
        self.sock = sock
        self.save_path = save_path
        self.debug = debug
        self.notify_pipe = notify_pipe

        self.old_sessions = {}
        self.old_panes = set()

        self.command_callback = deque([((lambda lines: None), (), {})])
        self.cur_lines = None
        self.instance = None
        self.instance_dir = None
        self.list_command_outstanding = False

        sub_env = dict(os.environ)
        sub_env.pop('TMUX', None)
        tmux_args = ['tmux', '-C', '-S', sock, 'new-session', '-A', '-D', '-s', '_control', 'cat']

        self.proc = subprocess.Popen(tmux_args, env=sub_env, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        self.command('show-env -g TMUX_INSTANCE', self.get_instance_callback)
        self.do_session_log()

    def read_command_output(self):
        while True:
            r = self.proc.stdout.readline()
            if not r:
                break

            r = r.decode('utf-8', 'ignore').rstrip('\n')
            if r.startswith('%'):
                lst = r.split()
                event = lst[0]
                func = getattr(self, f"evt_{event[1:].replace('-', '_')}", None)
                if func:
                    func(lst)
                else:
                    if self.debug:
                        print(f'unhandled event: {r}')
            elif self.cur_lines is not None:
                self.cur_lines.append(r)

    def command(self, cmd, cb, *a, **kw):
        self.command_callback.append((cb, a, kw))
        self.proc.stdin.write((cmd + '\n').encode('utf-8'))
        self.proc.stdin.flush()

    def evt_begin(self, argv):
        self.cur_lines = []

    def evt_end(self, argv):
        lines = self.cur_lines
        self.cur_lines = None
        f, a, kw = self.command_callback.popleft()
        return f(lines, *a, **kw)

    evt_error = evt_end

    def evt_sessions_changed(self, argv):
        if self.debug:
            print(f'session change event: {argv[0]}')
        if not self.list_command_outstanding:
            self.do_session_log()

    evt_session_renamed = evt_sessions_changed
    evt_window_add = evt_sessions_changed
    evt_window_close = evt_sessions_changed
    evt_unlinked_window_add = evt_sessions_changed
    evt_unlinked_window_close = evt_sessions_changed
    evt_linked_window_add = evt_sessions_changed
    evt_linked_window_close = evt_sessions_changed

    def do_session_log(self):
        #self.list_command_outstanding = True
        self.command('list-panes -a -F "#{session_name}|#{window_index}.#{pane_index}|#{pane_id}"', self.list_session_callback)

    def list_session_callback(self, lines):
        sessions = defaultdict(list)
        allpanes = set()
        #self.list_command_outstanding = False
        for l in lines:
            sid, win, pane = l.split('|')
            pane = pane.lstrip('%')
            if sid != '_control':
                sessions[sid].append(f'{win}={pane}')
                allpanes.add(pane)

        if self.debug:
            print('sessions:')

        for sess, panes in sessions.items():
            old_panes = self.old_sessions.get(sess)
            if panes == old_panes:
                continue
            txt = f"{sess} {' '.join(panes)}"
            if self.debug:
                print(txt)
            for sessfn in (self.save_path / f'{sess}.session', self.instance_dir / f'{sess}.session'):
                sessfn.write_text('{self.instance}\n{txt}\n')

        deleted_sessions = self.old_sessions.keys() - sessions.keys()

        for sess in deleted_sessions:
            if self.debug:
                print(f'deleted session {sess}')
            for sessfn in (self.save_path / f'{sess}.session', self.instance_dir / f'{sess}.session'):
                try:
                    sessfn.rename(sessfn.with_name(sessfn.name + '-obs'))
                except OSError:
                    pass

        deleted_panes = self.old_panes - allpanes
        for pane in deleted_panes:
            if self.debug:
                print(f'deleted pane {pane}')
            for suffix in ('-hist', '-pwd'):
                try:
                    fn = self.instance_dir / (pane + suffix)
                    fn.rename(self.instance_dir / f'obs-{pane}{suffix}')
                except OSError:
                    pass

        if self.debug:
            print()

        self.old_panes = allpanes
        self.old_sessions = sessions

    def get_instance_callback(self, lines):
        if self.debug:
            print(lines)
        env = dict(lin.split('=', 1) for lin in lines if '=' in lin)
        instance = env.get('TMUX_INSTANCE')
        if instance is None:
            sock_time = int(self.sock.stat().st_mtime)
            sock_time_str = time.strftime('%Y-%m-%d__%H-%M-%S', time.localtime(sock_time))
            instance = f'{self.sock.name}-{sock_time_str}'
            self.command(f'setenv -g TMUX_INSTANCE "{instance}"', lambda lines: None)
            if self.debug:
                print(f'set instance to {instance}')

        self.instance = instance
        self.instance_dir = self.save_path / ('tmux-' + instance)
        self.instance_dir.mkdir(parents=True, exist_ok=True)

        if self.debug:
            print(f'instance={instance}')
        if self.notify_pipe is not None:
            os.close(self.notify_pipe)
            self.notify_pipe = None


class TmuxQuery:
    ivars = ()
    vars = ()
    args = []
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

    @classmethod
    def run(cls, controller, args=[], xargs=[], host=None):
        # Need a unique separator. We used to use an ASCII control
        # character, but newer versions of TMUX filter those out.
        # Also filters any non-ASCII characters 🤬  (╯°□°)╯︵ ┻━┻
        sep = '<d-_-b>'
        allvars = cls.ivars + cls.vars
        p = controller.tmux(args + cls.args + xargs + ['-F', sep.join(f'#{{{v}}}' for v in allvars)], host=host)
        r = []
        for line in p.stdout.splitlines():
            self = cls()
            i = iter(line.split(sep, len(allvars) - 1))
            for k in cls.ivars:
                setattr(self, k, int(next(i)))
            for k in cls.vars:
                setattr(self, k, next(i))
            r.append(self)
        return r

    def __repr__(self):
        args = ', '.join(f'{k}={getattr(self, k, None)!r}' for k in (self.ivars + self.vars))
        return f'{type(self).__name__}({args})'

class ListSessions(TmuxQuery):
    args = ['list-sessions']
    ivars = ('session_windows', 'session_attached')
    vars = ('session_created_string', 'session_name')

class Pane(TmuxQuery):
    ivars = 'window_index', 'line', 'pane_pid'
    vars = 'pane_id', 'session_name'
    args = ['list-panes']

class TmuxControl:
    def __init__(self):
        tmux = Path('/usr/local/bin/tmux')
        if not tmux.exists():
            tmux = Path('/usr/bin/tmux')

        self.tmux_path = tmux
        self.environment = dict(os.environ)
        self.sock_path = None
        self.env_sock_path = None

        self.environment.pop('TMUX', None)
        self.environment.pop('debian_chroot', None)

        home = Path.home()
        self.save_path = home / '.tmuxsave'
        self.ssh_user_path = home / '.ssh'

    @property
    def controlling_current_session(self):
        return self.sock_path == self.env_sock_path

    def tmux_args(self, args, capture=False, host=None):
        if host:
            return ['ssh', '-S', get_ssh_sock(host), '', ('-T' if capture else '-t'), 'tmux ' + escape_shell(args)]
        else:
            ret = [self.tmux_path, '-S', self.sock_path]
            ret.extend(args)
            return ret

    def tmux(self, args, capture=True, host=None, **kw):
        return runproc(self.tmux_args(args, capture, host), capture, env=self.environment, **kw)

    def find_socket(self, socketname=None):
        tmux_env = os.getenv('TMUX')
        if tmux_env is not None:
            self.sock_path = Path(tmux_env.split(',')[0])
            self.env_sock_path = self.sock_path
            if socketname is None:
                return

        if socketname is None:
            socketname = 'default'

        tmp = os.getenv('TMUX_TMPDIR') or os.getenv('TMPDIR') or '/tmp'
        sock_dir = Path(tmp) / 'tmux-{os.geteuid()}'

        sock_dir.mkdir(sock_dir, mode=0o700, exist_ok=True)
        self.sock_path = sock_dir / socketname

    def save_all(self, src=None):
        if src is not None:
            instancedir = sessiondir = src
        else:
            sessiondir = dir
            instancedir = None

        for fpath in sessiondir.iterdir():
            if fpath.suffix == '.session':
                name = fpath.stem
                zipf = self.save_path / f'{name}.zip'
                try:
                    mtime = zipf.stat().st_mtime
                except FileNotFoundError:
                    mtime = None

                self.do_save_session(sessiondir, instancedir, name, zipf, mtime)

    def save_session(self, name=None, dest=None, src=None):
        if src is not None:
            instancedir = sessiondir = src
        else:
            sessiondir = self.save_path
            instancedir = None

        self.do_save_session(sessiondir, instancedir, name, dest, None)

    def do_save_session(self, sessiondir, instancedir, name, dest, ifmtime):
        try:
            sf = sessiondir / f'{name}.session'
            sid, pane_list = read_session_file(sf, name)
            if instancedir is None:
                instancedir = self.save_path / f'tmux-{sid}'

            if ifmtime:
                if not any(fn.stat().st_mtime >= ifmtime for fn in instancedir.iterdir()):
                    return
        except OSError:
            raise SessionNotFoundError(f'session {name} not found') from None

        panes = []
        for l in pane_list:
            m = RX_PANE.match(l)
            if m:
                panes.append(tuple(int(v) for v in m.groups()))

        if not panes:
            return

        if dest is None:
            dest = self.save_path / f'{name}.zip'

        with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as zipf:
            print(f'Saving session {name} {sorted(set(wid for wid, pn, pid in panes))!r}')
            for wid, pn, pid in panes:
                try:
                    zipf.write(instancedir / f'{int(pid)}-pwd', f'{name}-{int(wid)}.{int(pn)}-pwd')
                except FileNotFoundError:
                    pass
                except Exception:
                    traceback.print_exc()

                try:
                    zipf.write(instancedir / f'{int(pid)}-hist', f'{name}-{int(wid)}.{int(pn)}-hist')
                except FileNotFoundError:
                    pass
                except Exception:
                    traceback.print_exc()

    def restore_tmux(self, args, sess, panes, iter):
        restorewin = {}
        data = {}
        for win, pane, histdat, pwd in iter:
            rpanes = restorewin.get(win)
            if not rpanes:
                rpanes = restorewin[win] = set()
            rpanes.add(pane)
            data[win, pane] = histdat, pwd

        if not restorewin:
            print(f'Cannot find any save information for {sess}')
            return

        exist_windows = set(p.window_index for p in panes)
        new_win = max(set(restorewin) | exist_windows) + 1

        tmux_commands = []

        pane_by_index = dict(((p.window_index, p.line), p) for p in panes)

        if not panes:
            print(f'Session {sess} does not exist, creating...')

            self.tmux(args + ['new', '-s', sess, '-d'], check=True)
        else:
            print(f'Session {sess} already exists')
            return

        create_windows = set(restorewin) - exist_windows

        ## first, restore into existing windows
        for w, pane_list in restorewin.items():
            for i in pane_list:
                cur_win = pane_by_index.get((w, i))
                if cur_win:
                    if cur_win.ok:
                        ## don't send break to pane running this script
                        make_restore(data[w, i], sess, w, i, None, cur_win.is_me, tmux_commands)

        for w, pane_list in restorewin.items():
            win_id = f'{sess}:{int(w)}'

            if w not in exist_windows:
                fn = make_restore(data[w, 0], sess, w, 0, win_id, True, None)
                tmux_commands.append(['setenv', '-t', sess, 'SCN_RESTORE_SCRIPT', fn])
                tmux_commands.append(['neww', '-k', '-d', '-t', win_id])

            maxw = max(pane_list)
            for i in range(maxw + 1):
                cur_win = pane_by_index.get((w, i))
                if i not in pane_list:
                    if i > 0:
                        tmux_commands.append(['splitw', '-h', '-t', win_id])
                    continue

                if cur_win:
                    continue

                if i != 0:
                    dst = f'{sess}:{int(new_win)}'
                    fn = make_restore(data[w, i], sess, w, i, dst, True, None)
                    tmux_commands.append(['setenv', '-t', sess, 'SCN_RESTORE_SCRIPT', fn])
                    tmux_commands.append(['neww', '-k', '-d', '-t', dst])

                if i > 0:
                    tmux_commands.append(['joinp', '-d', '-h', '-s', dst, '-t', win_id, ';'])

            tmux_commands.append(['setenv', '-t', sess, '-u', 'SCN_RESTORE_SCRIPT', ';'])

        new_wins = []
        if tmux_commands:
            for arglst in tmux_commands:
                self.tmux(args + arglst, check=True)

    def start_log_session(self, debug):
        notify_pipe = None
        wait_pipe, notify_pipe = os.pipe()

        cpid = os.fork()
        if cpid != 0:
            # parent process - wait for log-session to fully start up
            os.close(notify_pipe)
            while True:
                try:
                    r, w, e = select.select((wait_pipe,), (), (), None)
                    if wait_pipe in r:
                        break
                except EnvironmentError as e:
                    if e.errno not in RETRY_ERRNO:
                        raise

            return

        os.environ.pop('TMUX', None)
        os.environ.pop('TMUX_INSTANCE', None)

        # child process - run log-session
        os.close(wait_pipe)

        if os.fork() != 0:
            os._exit(0)
        os.setsid()

        nullf = os.open('/dev/null', os.O_RDWR)
        if debug:
            logf = os.open('/tmp/tmux-log-session.log', os.O_WRONLY|os.O_CREAT|os.O_APPEND)
        else:
            logf = nullf

        os.dup2(nullf, 0)
        os.dup2(logf, 1)
        os.dup2(logf, 2)
        os.close(nullf)
        if debug:
            os.close(logf)

        tc = SessionLogger(self.sock_path, self.save_path, debug, notify_pipe)
        try:
            tc.read_command_output()
        except KeyboardInterrupt:
            tc.command('kill-session -t _control', lambda lines: None)
            tc.read_command_output()

def escape_shell_arg_part(arg):
    if not re.search(r'([\\\[\]{}();"\*&\$<>#@!`\+|?]|\s)', arg):
        return arg
    return f"'{arg}'"

def escape_shell_arg(arg):
    arg = str(arg)
    return r"\'".join(escape_shell_arg_part(part) for part in arg.split("'"))

def escape_shell(lst):
    return ' '.join(escape_shell_arg(arg) for arg in lst)

def make_script(txt, **vars):
    return  ''.join(f"{k}={escape_shell_arg(v)}\n" for k, v in vars.items()) + txt

def make_restore(data, sess, w, i, dst, is_new, lst):
    histdat, pwd = data
    tempf_hist = tempfile.NamedTemporaryFile(prefix=f'restorescn-{sess}-{int(w)}.{int(i)}-', suffix='.hist', delete=False)
    tempf_hist.write(histdat)

    tempf = tempfile.NamedTemporaryFile(prefix=f'restorescn-{sess}-{int(w)}.{int(i)}-', suffix='.sh', delete=False)

    tempf.write(make_script(RESTORE_SCRIPT, pwd=pwd, histf=tempf_hist.name, tempf=tempf.name, name=f'{sess}:{int(w)}.{int(i)}').encode('utf-8'))
    tempf_hist.close()
    tempf.close()

    cmd = f"\n. '{tempf.name}'\n"
    if not is_new:
        cmd = '\x03\x03' + cmd
    if dst is None:
        dst = f'{sess}:{int(w)}.{int(i)}'

    #cmd = '... %s' % pfx
    if lst is not None:
        lst.append(['send', '-t', dst, cmd])
    return tempf.name

def iterdir(dir, name):
    rxfn = re.compile(re.escape(name) + r'-(\d+)\.(\d+)-hist')
    rxfn2 = re.compile(re.escape(name) + r'-(\d+)-hist')

    for path in dir.iterdir():
        m = rxfn.match(path.name)
        pane = None
        if not m:
            m = rxfn2.match(path.name)

        if not m:
            continue

        win = int(m.group(1))
        try:
            pane = int(m.group(2))
        except ValueError:
            pane = 0

        try:
            histdat = path.read_bytes()
        except OSError:
            continue

        try:
            with path.with_name(path.name[:-5] + pwd, encoding='utf8', errors='none') as fp:
                pwd = fp.readline().rstrip('\r\n')
        except OSError:
            continue

        yield win, pane, histdat, pwd

def iterzip(zipf):
    rxfn = re.compile(r'.*?-(\d+)\.(\d+)-hist')
    for f in zipf.namelist():
        m = rxfn.match(f)
        if not m:
            continue
        win = int(m.group(1))
        pane = int(m.group(2))

        try:
            histdat = zipf.read(f)
        except Exception:
            traceback.print_exc()
            continue

        try:
            pwd = zipf.read(f[:-5] + '-pwd').decode('utf-8').rstrip('\r\n')
        except Exception:
            traceback.print_exc()
            continue

        yield win, pane, histdat, pwd

def read_session_file(fpath, look=None):
    r = ([] if look is None else None)
    sid = None
    with fpath.open('r', encoding='utf8') as fp:
        for line in fp:
            pane_list = line.strip().split(' ')
            if len(pane_list) < 2:
                if len(pane_list) == 1:
                    sid = pane_list[0]
                continue
            name = pane_list[0]
            if look is not None:
                if name == look:
                    return sid, pane_list[1:]
            else:
                r.append((name, pane_list[1:]))
    return sid, r

def process_legacy_args(args):
    # Process legacy arguments
    for a in args.session_args:
        if a == 's':
            args.save = True
        elif a == 'r':
            args.restore = True
        elif a == 'n':
            args.nodetach = True
        elif a == 'ls':
            args.list = True
        else:
            args.session = a

def main():
    args = sys.argv[1:]

    options = argparse.ArgumentParser()
    options.add_argument('session_args', nargs='*', help='Session to open/save/restore')
    options.add_argument('--setup', action='store_true', help='Set up control-tmux for the current user')
    options.add_argument('--list', action='store_true', help='List sessions (default if no other arguments specified)')
    options.add_argument('-S', '--sessionpath', type=Path, help='Path to session directory')
    options.add_argument('-z', '--zip', type=Path, help='Path to zip file to save or restore session')
    options.add_argument('-s', '--save', action='store_true', help='Save sessions')
    options.add_argument('-r', '--restore', action='store_true', help='Restore sessions')
    options.add_argument('-H', '--host', help='Remote host to connect to via SSH')
    options.add_argument('-n', '--nodetach', action='store_true', help='Do not detach other clients from the target session')
    options.add_argument('-2', '--256color', action='store_true', help='Force 256-color mode')
    options.add_argument('--socket', help='TMUX socket name')
    options.add_argument('--log-session', action='store_true', help='Launch or relaunch session logger')
    options.add_argument('--debug', action='store_true', help='write session logger debug output to /tmp/tmux-log-session.log')
    options.add_argument('--remote-run-inner', help=argparse.SUPPRESS)
    options.set_defaults(
        session=None
    )

    args = options.parse_args()
    process_legacy_args(args)

    if args.save and args.restore:
        print('Cannot specify --save and --restore at the same time')
        return

    if args.setup:
        return

    ctl = TmuxControl()
    ctl.find_socket(args.socket)

    if not ctl.save_path.is_dir():
        print('`control-tmux` has not been set up for the current user.')
        print()
        print('Please run `control-tmux --setup`')
        return

    preargs = []

    if args.log_session:
        ctl.start_log_session(args.debug)
        return

    if args.remote_run_inner:
        attach_args = ['-2', 'attach']
        if not args.nodetach:
            attach_args.append('-d')
        attach_args.append('-t')
        attach_args.append(args.remote_run_inner)
        p = ctl.tmux(attach_args, capture=False, host=args.host)
        if p.returncode != 0:
            p = ctl.tmux(['-2', 'new', '-s', args.remote_run_inner], capture=False, host=args.host)
            if p.returncode != 0:
                # This is running inside a new window, so when we exit, it will
                # close. Keep it around until the user can read the errors.
                print('Cannot launch remote TMUX instance!')
                input('Press enter to close. ')
        return

    if args.host:
        if args.save or args.restore:
            print('Cannot save or restore on remote')

        csock = get_ssh_sock(args.host)
        # Check if there is a master running on the given
        p = runproc(['ssh', '-S', csock, '-O', 'check', ''], capture=True)
        if p.returncode != 0:
            print(f'Connecting new SSH session to remote host {args.host}')
            p = runproc(['ssh', '-M', '-o', 'ControlPersist=yes', '-o', f'ControlPath={csock}', '-n', '-f', '-T', '-N', args.host], capture=False)
            if p.returncode != 0:
                print(f'Could not connect master to {args.host}')
                return

    sessions = ListSessions.run(ctl, preargs, host=args.host)
    sess_by_name = dict((s.session_name, s) for s in sessions)

    ## Linux VT is the only terminal I can find that *doesn't* support 256 colors
    if not os.environ.get('TERM', '').startswith('linux'):
        preargs.append('-2')

    if args.save or args.restore:
        panes = Pane.run(ctl, preargs, ['-a'])
        existing_session = bool(panes)

        if not args.session:
            mypane = os.getenv('TMUX_PANE')
            if not mypane or not ctl.controlling_current_session:
                print('not in tmux and none specified')
                return

            mysess = [p.session_name for p in panes if p.pane_id == mypane]
            if len(mysess) > 1:
                print(f"pane is in multiple sessions ({', '.join(mysess)})")
                return

            if not mysess:
                print('pane could not be found')
                return

            args.session = mysess[0]

        panes = [p for p in panes if p.session_name == args.session]

        if args.restore:
            if '_control' not in sess_by_name:
                ctl.start_log_session(args.debug)

            defaultzip = ctl.save_path / f'{args.session}.zip'
            zip = args.zip
            if zip is None and defaultzip.exists():
                zip = defaultzip

            if zip is not None:
                itr = iterzip(zipfile.ZipFile(zip, 'r'))
            else:
                itr = iterdir(ctl.save_path, args.session)
            ctl.restore_tmux(preargs, args.session, panes, itr)
            return
        else:
            ctl.save_path.mkdir(parents=True, exist_ok=True)

            if args.session == 'all':
                return ctl.save_all(args.sessionpath)
            return ctl.save_session(args.session, args.zip, args.sessionpath)

    if args.list or (args.session is None):
        for s in sessions:
            if s.session_name == '_control':
                continue
            print('%-10s: %2d win (created %s) %s' % \
                (s.session_name, s.session_windows, s.session_created_string,
                 ' attached' if s.session_attached else ''))
        return

    if args.host:
        sessname = '_' + os.urandom(8).hex()

        tmux_args = list(preargs)

        inner_args = [sys.executable, '-m', 'controltmux', '--remote-run-inner', args.session, '-H', args.host]
        if args.nodetach:
            inner_args.append('--nodetach')

        tmux_args.extend(['new-session', '-d',  '-s', sessname, escape_shell(inner_args), ';'])
        tmux_args.extend(['set-option', '-t', sessname, 'status', 'off', ';'])
        tmux_args.extend(['set-option', '-t', sessname, 'set-titles-string', f"[RMT {args.host}] #T", ';'])
        tmux_args.extend(['set-option', '-t', sessname, 'prefix', 'C-q'])

        #print(' '.join(tmux_args))
        ctl.tmux(tmux_args, capture=False)

        # just needs to be present
        sess_by_name[sessname] = True
        args.nodetach=True
        args.session = sessname

    if ctl.controlling_current_session:
        if args.session in sess_by_name:
            if not args.nodetach:
                ctl.tmux(preargs + ['detach-client', '-s', args.session])
        else:
            ctl.tmux(preargs + ['new-session', '-d', '-s', args.session])
        execargs = ctl.tmux_args(preargs + ['switch-client', '-t', args.session])
    else:
        if '_control' not in sess_by_name:
            ctl.start_log_session(args.debug)

        if args.session in sess_by_name:
            preargs.append('attach')
            if not args.nodetach:
                preargs.append('-d')
            execargs = ctl.tmux_args(preargs + ['-t', args.session])
        else:
            execargs = ctl.tmux_args(preargs + ['new', '-s', args.session])

    if execargs:
        os.execvpe(execargs[0], execargs, ctl.environment)

main()
