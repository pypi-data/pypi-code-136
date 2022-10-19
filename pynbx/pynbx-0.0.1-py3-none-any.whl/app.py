import logging
import pathlib
import webbrowser
from pathlib import Path
from typing import Any, Dict, List
from threading import Timer

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from nbx import nbx, util
from nbx.note import Note

FRONTEND_SESSION_STATE = {
    # See all page options in ./frontend/src/App.svelte
    "routing": {"page": "", "params": {}},
    # EditNote related
    "relevantRecords": [],
    "uploadedImageUrl": "",
    "noteTitle": "",
    "noteContent": "",
    # EditInsight related
    "insightGraph": {
        "nodes": [],
        "edges": [],
        "selectedNodes": []
    },
    "statementHtmls": [],
    # ListNotes related
    "selectedNoteIdx": -1,
    # Connection related
    "connectedToBackend": True
}

BACKEND_SESSION_STATE = {
    # EditNote related
    "note": None,
    # ListNotes related
}

logger = logging.getLogger(__name__)

####################################################################################################
# FastAPI Configurations

HOST = "localhost"
PORT = 8000

app = FastAPI()

# Allow CORS from svelte frontend to fastapi backend
origins = [
    f"http://{HOST}",
    f"http://{HOST}:{PORT}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd = pathlib.Path(__file__).parent.resolve()
app.mount(
    "/app",
    StaticFiles(directory=Path(pwd, "frontend/dist/"), html=True),
    name="static",
)

####################################################################################################
# Logics for handling data sent by the UI frontend


def handle_save_note():
    note = BACKEND_SESSION_STATE["note"]
    has_changed = True
    if note:
        has_changed = note.has_changed
        note.save()
    else:
        full_content = FRONTEND_SESSION_STATE["noteContent"]
        if FRONTEND_SESSION_STATE["noteTitle"] != "<h1></h1>":
            full_content = FRONTEND_SESSION_STATE["noteTitle"] + "\n" + full_content
        nbx.create_note(full_content)
    if has_changed:
        nbx.index_all_notes(background=True)
    util.terminate_process()


def handle_exit():
    note = BACKEND_SESSION_STATE["note"]
    if note:
        note.reset()
    util.terminate_process()


def handle_update_note(data):
    global FRONTEND_SESSION_STATE
    if "data" not in data:
        logger.warning(
            "Invalid update_note websocket: No data specified", data)
        return

    input = data["data"]["input"]
    content = data["data"]["content"]
    update_type = data["data"]["updateType"]
    if update_type == "noteContent":
        FRONTEND_SESSION_STATE["noteContent"] = content
    if update_type == "noteTitle":
        FRONTEND_SESSION_STATE["noteTitle"] = content

    note = BACKEND_SESSION_STATE["note"]
    if note:
        if update_type == "noteContent":
            note.update_body(content)
        if update_type == "noteTitle":
            note.update_title(content)
    # find relevant note abstracts as prompts for the user to select
    relevantRecords = nbx.find_relevant_records(input)
    FRONTEND_SESSION_STATE["relevantRecords"] = relevantRecords


def handle_upload_image(data):
    global FRONTEND_SESSION_STATE

    if "data" not in data:
        logger.warning(
            "Invalid upload_image websocket: No data specified",
            data
        )
        return
    image = data["data"]["image"]
    image_name = nbx.add_image(image)
    FRONTEND_SESSION_STATE["uploadedImageUrl"] = f"http://{HOST}:{PORT}/images/{image_name}"


def handle_data(data):
    if "type" not in data:
        logger.warning("Invalid websocket data: No type specified", data)
        return
    data_type = data["type"]

    if data_type == "exit":
        handle_exit()
    elif data_type == "save_note":
        handle_save_note()
    elif data_type == "update_note":
        handle_update_note(data)
    elif data_type == "upload_image":
        handle_upload_image(data)
    elif data_type == "show_note":
        if "data" not in data:
            logger.warning(
                "Invalid update_note websocket: No data specified", data)
            return
        note = nbx.load_note(data["data"]["filename"])
        FRONTEND_SESSION_STATE["routing"]["params"]["currentNote"] = note


####################################################################################################
# FastAPI Endpoints

@app.get("/images/{filename}")
async def images(filename: str) -> FileResponse:
    image_path = nbx.get_image_path(filename)
    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Item not found")
    return FileResponse(image_path)


@app.get("/data")
async def data():
    return FRONTEND_SESSION_STATE


@app.websocket("/stream")
async def stream(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            handle_data(data)
            await websocket.send_json(FRONTEND_SESSION_STATE)
    except WebSocketDisconnect:
        logger.info("connection closed")


@app.get("/")
async def root():
    return RedirectResponse(url="app")


def add_note(host: str = HOST, port: int = PORT) -> None:
    global FRONTEND_SESSION_STATE
    FRONTEND_SESSION_STATE["routing"] = {"page": "EditNote", "params": {}}
    webbrowser.open_new(f"http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)


def edit_note(note: Note, host: str = HOST, port: int = PORT, read_only: bool = False) -> None:
    global FRONTEND_SESSION_STATE
    global BACKEND_SESSION_STATE
    note_title = "<h1>" + note.get_title() + "</h1>"  # get_title returns pure text without h1 tag
    note_content = note.get_body()
    # @TODO This param is a redundant info as it is only needed to initialize UI components
    # And also the info is already recorded in the FRONTEND_SESSION_STATE
    add_note_params = {
        "noteTitle": note_title,
        "noteContent": note_content,
        "logs": note.logs
    }
    FRONTEND_SESSION_STATE["routing"] = {"page": "EditNote", "params": add_note_params}
    FRONTEND_SESSION_STATE["connectedToBackend"] = not read_only
    FRONTEND_SESSION_STATE["noteTitle"] = note_title
    FRONTEND_SESSION_STATE["noteContent"] = note_content
    BACKEND_SESSION_STATE["note"] = note
    webbrowser.open_new(f"http://{host}:{port}")
    if read_only:
        Timer(1, util.terminate_process).start()  # kill the python backend in 1 second
    uvicorn.run(app, host=host, port=port)


def list_notes(note_infos: List[Dict[str, Any]], host: str = HOST, port: int = PORT) -> None:
    global FRONTEND_SESSION_STATE
    FRONTEND_SESSION_STATE["routing"] = {"page": "ListNotes", "params": {"noteInfos": note_infos}}
    webbrowser.open_new(f"http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)
