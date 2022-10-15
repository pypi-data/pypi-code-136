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
    """
    Sends a message to all or a specific client
    :param msg: Message you want to send, can be a dict too
    :param event: Socket event
    :param to: SID of the connected user, if its set, it will only send to that specific client otherwise broadcast
    :return: list.append
    """
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
    """
    Starts the SocketIO Server
    :param host: Host IP, when left blank server runs at 0.0.0.0
    :param port: Port
    :param threaded: If True, it runs the eventlet server in a thread, otherwise in foreground
    :param cors: Adds cors headers to the WSGIApp
    :param static_files: Static Files
    :return: Void
    """
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


