
from flask import Flask

from htmx_flask import Htmx, request, make_response

app = Flask(__name__)
h = Htmx()
h.init_app(app)

@app.route("/")
def hello_world():
    body = f"Boosted = {request.htmx.boosted}"
    return make_response(body, location="/foo")

