import multiprocessing

import uvicorn
from gunicorn.app.wsgiapp import WSGIApplication


def number_of_workers() -> int:
    return (multiprocessing.cpu_count() * 2) + 1


def _run_uvicorn(app_uri: str, web_host: str, web_port: int):
    uvicorn.run(
        app_uri,
        host=web_host,
        port=web_port,
        reload=True,
    )


class StandaloneApplication(WSGIApplication):  # pragma: no cover
    def __init__(self, app_uri, options=None):
        self.options = options or {}
        self.app_uri = app_uri
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)


def _run_gunicorn(app_uri: str, web_host: str, web_port: int):
    options = {
        "bind": f"{web_host}:{web_port}",
        "workers": number_of_workers(),
        "worker_class": "uvicorn.workers.UvicornWorker",
    }
    StandaloneApplication(app_uri, options).run()


def run_gunicorn_or_uvicorn(app_uri: str, web_host: str, web_port: int, reload: bool):
    """Run either gunicorn or uvicorn depending on whether reloading is needed."""
    if reload:
        _run_uvicorn(app_uri, web_host, web_port)
    else:
        _run_gunicorn(app_uri, web_host, web_port)
