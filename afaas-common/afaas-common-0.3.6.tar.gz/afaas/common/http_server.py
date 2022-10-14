""" Simple http server to expose healthz and some basic introspection for the MSA/Fold servers """
import http.server
import socketserver
import threading

from google.cloud import firestore
from google import auth

import afaas.cache.cache


class Handler(http.server.BaseHTTPRequestHandler):
    """ Handles incoming HTTP GET requests. """

    def __init__(self, *args, **kwargs):
        creds, project_id = auth.default()
        self.db_client = firestore.Client(credentials=creds, project=project_id)
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        self.send_response(200)

    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('OK'.encode('UTF-8'))
        elif self.path == '/cache':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self._print_cache().encode('UTF-8'))
        elif self.path == '/localcache':
            if self.local_cache is None:  # no local cache available (for Folding server)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('Folding server has no local cache'.encode('UTF-8'))
                return
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self._print_local_cache().encode('UTF-8'))

    def _print_cache(self):
        sequence_cache_collection = self.db_client.collection('sequences')
        result = ''
        for seq in sequence_cache_collection.stream():
            result += f'{seq.get("user")}\t{seq.get("location")}\t{seq.get("seq")}\n\n'
        return result

    def _print_local_cache(self):
        result = f'Total items in cache: {len(self.local_cache.cache)}\n'
        items = []
        for seq, (userid, location) in self.local_cache.cache.items():
            if userid == '':
                continue
            items.append(f'{userid}\t{seq}\t{location}')
        items.sort()
        return result + '\n'.join(items)


def _create_handler(local_cache: afaas.cache.cache.Cache):
    class CustomHandler(Handler):
        def __init__(self, *args, **kwargs):
            self.local_cache = local_cache
            super().__init__(*args, **kwargs)

    return CustomHandler


def _run_http_server(port: int, local_cache: afaas.cache.cache.Cache = None):
    CacheHandler = _create_handler(local_cache)
    httpd = socketserver.TCPServer(('', port), CacheHandler)
    httpd.serve_forever()


def start_daemon(port: int, local_cache: afaas.cache.cache.Cache = None):
    http_thread = threading.Thread(name='http_server', target=_run_http_server, args=(port, local_cache))
    http_thread.setDaemon(True)
    http_thread.start()
