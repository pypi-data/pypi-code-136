import re

import inspect
import json


class API:
  def __init__(self):
    self.routes = {}

  def route(self, path, handler):
    # assert path not in self.routes, "Such route already exists."
    self.routes[path] = handler

  def not_found(self, response):
    response['statusCode'] = 404
    response['body'] = json.dumps({
        "message": "Not found"
    })

  def method_not_allowed(self, response):
    response['statusCode'] = 405
    response['body'] = json.dumps({
        "message": "Method not allowed"
    })

  def find_handler(self, request_path):
    for path, handler in self.routes.items():
      re_path = re.compile(path)
      match = re_path.search(request_path)

      if match:
        kwargs = match.groupdict()
        return handler, kwargs

    return None, None

  def handle_request(self, request):
    response = {
        "headers": {
            "Content-Type": "application/json"
        },
    }
    method = request.get('httpMethod', None)

    handler, kwargs = self.find_handler(request_path=request['path'])

    if handler is not None:
      if inspect.isclass(handler):
        handler = getattr(handler(), method.lower(), None)
        if handler is None:
          self.method_not_allowed(response)
          return response

      handler(request, response, **kwargs)
    else:
      self.not_found(response)

    return response