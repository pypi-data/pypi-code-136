import json
from pathlib import Path
import re
from importlib.resources import files

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado


def hello(nb_name, package=''):
    """
    Return the contents of the hello world notebook.
    """
    if not package:
        return files('astronbs').joinpath('notebooks').joinpath(nb_name).read_text()
    else:
        pieces = package.split('.')
        pkg_path = files(pieces[0])
        for piece in pieces[1:]:
            pkg_path = pkg_path.joinpath(piece)
        return pkg_path.joinpath(nb_name).read_text()

# class NBMaker:
#     def __init__(self, path):
#         self.path = Path(path)

#     def __call__(self, file):
#         f = Path(file)
#         ext = f.suffix()
#         stem = f.stem()
#         match = re.match(stem + '(\d*)' + ext)
#         if match:
#             digits = match.group(1)

#         pass

class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        p = Path('.')
        print(p.absolute())
        self.finish(json.dumps({
            "data": "This is /wooty-woot/get_example endpoint!"
        }))

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        p = Path('.')
        nb_content = hello('reduction-template.ipynb')

        (p / input_data['path'] / 'reduction_template.ipynb').write_text(nb_content)
        response = {
            'path': str(Path(input_data['path']) / 'reduction_template.ipynb'),
            'content': ''
        }
        self.finish(json.dumps(response))


class RouteHandler2(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        p = Path('.')
        print(p.absolute())
        self.finish(json.dumps({
            "data": "This is /wooty-woot/get_example endpoint!"
        }))

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        p = Path('.')
        nb_name = 'reprojection_template.ipynb'
        nb_content = hello(nb_name)

        (p / input_data['path'] / nb_name).write_text(nb_content)
        response = {
            'path': str(Path(input_data['path']) / nb_name),
            'content': ''
        }
        self.finish(json.dumps(response))


class RouteHandler3(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        p = Path('.')
        print(p.absolute())
        self.finish(json.dumps({
            "data": "This is /wooty-woot/get_example endpoint!"
        }))

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        p = Path('.')
        nb_name = 'light-image-combo-template.ipynb'
        nb_content = hello(nb_name)

        (p / input_data['path'] / nb_name).write_text(nb_content)
        response = {
            'path': str(Path(input_data['path']) / nb_name),
            'content': ''
        }
        self.finish(json.dumps(response))


class RouteHandler4(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        p = Path('.')
        print(p.absolute())
        self.finish(json.dumps({
            "data": "This is /wooty-woot/get_example endpoint!"
        }))

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        p = Path('.')
        nb_name = input_data['nb_name']
        pkg_path = input_data['package_path']
        nb_content = hello(nb_name, package=pkg_path)

        (p / input_data['path'] / nb_name).write_text(nb_content)
        response = {
            'path': str(Path(input_data['path']) / nb_name),
            'content': ''
        }
        self.finish(json.dumps(response))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    route_pattern = url_path_join(base_url, "astronbs", "reduction_template")
    route_pattern2 = url_path_join(base_url, "astronbs", "reprojection_template")
    route_pattern3 = url_path_join(base_url, "astronbs", "light_combo_template")
    route_pattern4 = url_path_join(base_url, "astronbs", "nb_make")
    handlers = [
        (route_pattern, RouteHandler),
        (route_pattern2, RouteHandler2),
        (route_pattern3, RouteHandler3),
        (route_pattern4, RouteHandler4),
    ]
    web_app.add_handlers(host_pattern, handlers)
