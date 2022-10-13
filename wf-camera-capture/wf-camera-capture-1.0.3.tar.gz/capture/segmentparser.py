import logging
from pathlib import Path

# from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from capture.segmentdata import SegmentDataIndex


class ChangeHandler(FileSystemEventHandler):

    def on_modified(self, event):
        pass


def monitor_directory(str_path):
    path = Path(str_path)
    logging.info(path)
    index = SegmentDataIndex(path)

    files = sorted(path.glob("*.h264"))
    for file in files:
        index.add_video(file.relative_to(path))
    # event_handler = ChangeHandler()
    # observer = Observer()
    # observer.schedule(event_handler, path, recursive=True)
    # observer.start()
    # try:
    #     while True:
    #         time.sleep(1)
    # finally:
    #     observer.stop()
    #     observer.join()
