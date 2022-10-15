import eventlet
import eventlet.wsgi
import socketio
import threading


sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


CONNECTIONS = []
QUEUE = []


@sio.event()
def connect(sid, environ, request):
    print('connect ', sid)
    CONNECTIONS.append(sid)


@sio.event
def my_message(sid, data):
    print('message ', data)
    sio.emit("message", {"data": "message"})


@sio.event
def disconnect(sid):
    if sid in CONNECTIONS:
        CONNECTIONS.remove(sid)


def send_message(msg="", event="message", to=None):
    return QUEUE.append(dict(
        msg=msg,
        event=event,
        sid=to
    ))


def handle_queue():
    while True:
        sio.sleep(0.01)
        while QUEUE:
            message = QUEUE.pop(0)
            sio.emit(message.get("event"), {"data": message.get("msg")}, to=message.get("sid"))


def run_wsgi(host="", port=5000):
    eventlet.wsgi.server(eventlet.listen((host, port)), app)


def start_server(host="", port=5000, threaded=True, cors=True, static_files=None):
    global sio, app
    if not cors:
        sio = socketio.Server()
    if static_files:
        app = socketio.WSGIApp(sio, static_files=static_files)
    sio.start_background_task(handle_queue)
    if not threaded:
        run_wsgi(host=host, port=port)
    threading.Thread(target=run_wsgi, args=(host, port, )).start()


start_server(threaded=False)


