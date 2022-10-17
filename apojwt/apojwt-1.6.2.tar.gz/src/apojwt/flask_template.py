from flask import request, abort

def ajwt_token_finder():
    request.headers["Authorization"].replace("Bearer ", "")

def ajwt_exception_handler(code, msg):
    abort(code, msg)

def create_flask_template():
    token_finder = ajwt_token_finder
    exception_handler = ajwt_exception_handler
    return token_finder, exception_handler