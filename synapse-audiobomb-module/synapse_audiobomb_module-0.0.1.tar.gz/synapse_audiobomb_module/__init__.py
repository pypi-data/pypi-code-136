import json
from twisted.web.resource import Resource
from twisted.web.server import Request
from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.web.server import NOT_DONE_YET
from .database import *
import psycopg2


def checkAuth(request, connection, callback):
    agent = Agent(reactor)
    user = None
    authHeader = None
    try:
        user = request.args.get(b"user")[0].decode()
        authHeader = request.getHeader("Authorization")
    except Exception as error:
        None

    if authHeader is None or user is None:
        request.setResponseCode(401)
        request.setHeader(b"Content-Type", b"application/json")
        request.write(json.dumps({"errcode": "M_MISSING_TOKEN", "error": "Missing access token"}).encode())
        request.finish()
        return

    url = "http://localhost:8008/_matrix/client/v3/presence/{0}/status".format(user).encode("utf-8")
    d = agent.request(b"GET",
                      url,
                      Headers({"Content-Type": ["application/json"], "Authorization": [authHeader]}),
                      None,
                      )

    def handle_response(response):
        if response.code != 200:
            request.setResponseCode(401)
            request.setHeader(b"Content-Type", b"application/json")
            request.write(json.dumps({"errcode": "M_MISSING_TOKEN", "error": "Missing access token"}).encode())
            request.finish()
        else:
            callback(request, connection)

    d.addCallback(handle_response)


def postRequest(request, connection):
    newdata = request.content.getvalue()
    user = request.args.get(b"user")[0].decode()
    if newdata is None:
        request.setResponseCode(400)
        request.setHeader(b"Content-Type", b"application/json")
        request.write(json.dumps({"errcode": "M_BAD_JSON ", "error": "Malformed JSON Data"}).encode())
        request.finish()
    else:
        data = json.loads(newdata)
        result = database.create_audio(connection, data["id"], data["name"], data["src"], user)
        if result is not None:
            request.setResponseCode(500)
            request.write(json.dumps({"errcode": "M_UNKNOWN  ", "error": "Unknown Server error"}).encode())

        request.setHeader(b"Content-Type", b"application/json")
        request.write(json.dumps({"success": "ok "}).encode())
        request.finish()


def pollRequest(request, connection):
    result = database.get_all(connection)
    jsonResult = json.dumps(result)
    request.write(jsonResult.encode())
    request.finish()


def singlePollRequest(request, connection):
    audioid = None
    try:
        audioid = request.args.get(b"audioid")[0].decode()

    except Exception as error:
        None

    if audioid is None:
        request.setResponseCode(400)
        request.setHeader(b"Content-Type", b"application/json")
        request.write(json.dumps({"errcode": "M_BAD_JSON ", "error": "Malformed JSON Data"}).encode())
        request.finish()
    else:
        result = database.get_audio(connection, audioid)
        jsonResult = json.dumps(result[0])
        request.write(jsonResult.encode())
        request.finish()


def deleteRequest(request, connection):
    audioid = None
    try:
        audioid = request.args.get(b"audioid")[0].decode()

    except Exception as error:
        None

    if audioid is None:
        request.setResponseCode(400)
        request.setHeader(b"Content-Type", b"application/json")
        request.write(json.dumps({"errcode": "M_BAD_JSON ", "error": "Malformed JSON Data"}).encode())
        request.finish()
    else:
        try:
            result = database.delete_audio(connection, audioid)
            if result is not None:
                request.setResponseCode(500)
                request.write(json.dumps({"errcode": "M_UNKNOWN  ", "error": "Unknown Server error"}).encode())
            else:
                request.write(json.dumps({"success": "ok "}).encode())

            request.setHeader(b"Content-Type", b"application/json")
            request.finish()
        except Exception as error:
            request.setResponseCode(500)
            request.setHeader(b"Content-Type", b"application/json")
            request.write(json.dumps({"errcode": "M_UNKNOWN", "error": "Unknown Server error"}).encode())
            request.finish()


class AudiobombResource(Resource):

    def __init__(self, config):
        self.connection = psycopg2.connect(**config)
        super(AudiobombResource, self).__init__()

    def render_GET(self, request: Request):
        path_resource = request.prepath[-1].decode('utf-8')
        if path_resource is not None:
            if path_resource == 'audiobomb':
                request.setResponseCode(200)
                request.setHeader(b"Content-Type", b"application/json")
                request.write(json.dumps({"success": "Module exists "}).encode())
                request.finish()
            elif path_resource == 'getall':
                checkAuth(request, self.connection, pollRequest)
            elif path_resource == 'getaudio':
                checkAuth(request, self.connection, singlePollRequest)
            else:
                request.setResponseCode(400)
                request.setHeader(b"Content-Type", b"application/json")
                request.write(json.dumps({"errcode": "M_BAD_JSON ", "error": "Malformed JSON Data"}).encode())
                request.finish()
        return NOT_DONE_YET

    def render_POST(self, request: Request):
        path_resource = request.prepath[-1].decode('utf-8')
        if path_resource is not None:
            if path_resource == 'createaudio':
                checkAuth(request, self.connection, postRequest)
            elif path_resource == 'createaudio':
                checkAuth(request, self.connection, deleteRequest)
            else:
                request.setResponseCode(400)
                request.setHeader(b"Content-Type", b"application/json")
                request.write(json.dumps({"errcode": "M_BAD_JSON ", "error": "Malformed JSON Data"}).encode())
                request.finish()

        return NOT_DONE_YET


class Audiobomb:
    def __init__(self, config, api):
        self._api = api
        self._config = config
        self.connection = psycopg2.connect(**config)
        database.create_tables(self.connection)

        self._api.register_web_resource(
            path="/_synapse/client/audiobomb",
            resource=AudiobombResource(config),
        )

        self._api.register_web_resource(
            path="/_synapse/client/audiobomb/getall",
            resource=AudiobombResource(config),
        )

        self._api.register_web_resource(
            path="/_synapse/client/audiobomb/getaudio",
            resource=AudiobombResource(config),
        )

        self._api.register_web_resource(
            path="/_synapse/client/audiobomb/createaudio",
            resource=AudiobombResource(config),
        )

        self._api.register_web_resource(
            path="/_synapse/client/audiobomb/deleteaudio",
            resource=AudiobombResource(config),
        )

    @staticmethod
    def parse_config(config):
        return config
