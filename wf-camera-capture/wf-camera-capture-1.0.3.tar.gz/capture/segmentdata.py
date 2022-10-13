from dataclasses import dataclass
import logging
import math
import sqlite3

import pendulum
import yaml

from .config import DEVICE_ID, ENV_ID, ASSIGNMENT_ID
from .vidtools import get_video_file_details
from .sokobon import send_to_minio



@dataclass(repr=False)
class Timecode:
    hour: int = 0
    minute: int = 0
    second: int = 0
    frame: int = 0

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}.{self.frame:02}"

    @classmethod
    def from_string(cls, value: str) -> "Timecode":
        clock, frame = value.split(".")
        hour, minute, second = clock.split(":")
        return Timecode(hour=hour, minute=minute, second=second, frame=frame)

    @classmethod
    def from_offset(cls, value: float, fps: float) -> "Timecode":
        ms = int(value)
        second = int((ms / 1000) % 60)
        minute = int((ms / 1000 / 60) % 60)
        hour = int((ms / 1000 / 60 / 60)  % 60)
        frame = math.ceil((ms % 1000) / (1000/fps))
        if frame == fps:
            frame = 0
            second += 1
        return Timecode(hour=hour, minute=minute, second=second, frame=frame)


@dataclass
class VideoInfo:
    id: int
    name: str
    offset: float = 0.0
    uploaded: bool = False
    frame_count: int = 0
    timecode: Timecode = Timecode()
    fps: int = 0
    duration: float = 0.0


class InvalidDirectory(Exception):

    def __init__(self, path):
        self.path = path
        super().__init__(f"specified [{path}] path does not contain required `wf-video-index.yml` or `start.timestamp` files")


class MissingZeroVideo(Exception):

    def __init__(self, path):
        self.path = path
        super().__init__(f"specified [{path}] path does not contain the first video in the sequence")


class SegmentDataIndex():

    def __init__(self, path):
        self.path = path
        # timestamp calculated after reading all other times
        self.start_datetime = None
        # timestamp written to the `start.timestamp` file
        self.start_approx_ts = None
        # create time from stat for the `start.timestamp` file
        self.start_ts_create = None
        # create time from stat for the first video
        self.start_zero_create = None
        logging.info("SegmentDataIndex startup %s", path)
        self.dbcon = None
        self._init_index()
        self._load_timestamps()

    def _init_index(self):
        index_file_path = self.path / "wf-video-index.yml"
        start_ts_file = self.path / "start.timestamp"
        if index_file_path.exists():
            logging.info("indexing already started, resuming")
            with index_file_path.open() as fp:
                index_info = yaml.safe_load(fp.read())
            self.start_datetime = pendulum.parse(index_info.get("start_datetime"))
            self.start_approx_ts = pendulum.parse(index_info.get("start_approx_ts"))
            self.start_ts_create = pendulum.parse(index_info.get("start_ts_create"))
            self.start_zero_create = pendulum.parse(index_info.get("start_zero_create"))
        elif start_ts_file.exists():
            self._perform_start_calculation()
        else:
            raise InvalidDirectory(self.path)
        self.dbcon = sqlite3.connect(self.path / "index.db")
        cur = self.dbcon.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS main.videos (id int PRIMARY KEY, name text, offset float, uploaded bool, frame_count int, fps int, timecode text, duration float)')
        cur.execute('CREATE TABLE IF NOT EXISTS main.frames (id int PRIMARY KEY, offset float)')
        self.dbcon.commit()
        cur.close()

    def _perform_start_calculation(self):
        """
        This is a sort of messy way to calculate the actual start time of the
        video capture. When capture starts a timestamp is written to "start.timestamp"
        Then capture kicks off. The timestamp of the first video file is the preferred
        timestamp to use, as it should align with when actual capture started.
        If that timestamp is somehow in the past of more than 10 seconds later
        then we reject it. We next look at the create time for the "start.timestamp"
        file. If that is in the past or more than 10 seconds later then we assme the
        timestamp in the file is the best candidate. We add a millesecond to that
        to account for startup time for libcamera, which may be naive.
        """
        start_ts_file = self.path / "start.timestamp"
        zero_video =  self.path / "video-00000.h264"
        if not zero_video.exists():
            raise MissingZeroVideo(self.path)
        logging.info("start timestamp found")
        with start_ts_file.open() as fp:
            ts_str = fp.read()
            logging.info(ts_str.strip())
        self.start_approx_ts = pendulum.parse(f'{ts_str[:-4]}+0000')
        start_ts_file_stat = start_ts_file.stat()
        zero_video_stat = zero_video.stat()
        self.start_ts_create = pendulum.from_timestamp(start_ts_file_stat.st_birthtime if hasattr(start_ts_file_stat, "st_birthtime") else start_ts_file_stat.st_ctime, 'UTC')
        self.start_zero_create = pendulum.from_timestamp(zero_video_stat.st_birthtime if hasattr(zero_video_stat, "st_birthtime") else zero_video_stat.st_ctime, 'UTC')
        aprox_create_diff = (self.start_ts_create - self.start_approx_ts).total_seconds()
        aprox_zero_diff = (self.start_zero_create - self.start_approx_ts).total_seconds()
        if (0 > aprox_create_diff > 10) and (0 > aprox_zero_diff > 10):
            # files probably moved or some sort of pause happened.
             # naive assumption that it took 1ms for capture to start after timestamp was written
            self.start_datetime = self.start_approx_ts.add(seconds=0.0001)
        elif 0 < aprox_zero_diff < 10:
            # prefer the zero create time over others.
            self.start_datetime = self.start_zero_create
        else:
            # fallback to create time of the ts file.
            self.start_datetime = self.start_zero_create
        self._write_index()

    def _write_index(self):
        index_file_path = self.path / "wf-video-index.yml"
        with index_file_path.open('w') as fp:
            fp.write(yaml.safe_dump({
                "start_datetime": self.start_datetime.isoformat(),
                "start_approx_ts": self.start_approx_ts.isoformat(),
                "start_ts_create": self.start_ts_create.isoformat(),
                "start_zero_create": self.start_zero_create.isoformat(),
            }))
            fp.flush()

    def find_video_for_index(self, index):
        cur = self.dbcon.cursor()
        existing = cur.execute("SELECT * FROM main.videos WHERE id = ?", [index]).fetchall()
        if len(existing) < 1:
            return None
        existing = existing[0]
        return VideoInfo(
            id=existing[0],
            name=existing[1],
            offset=existing[2],
            uploaded=existing[3],
            frame_count=existing[4],
            fps=existing[5],
            timecode=Timecode.from_string(existing[6]),
            duration=existing[6],
        )

    def add_video(self, path):
        cur = self.dbcon.cursor()
        # do we already have and existing entry, if so check that it is correct.
        index = int(path.name[6:-5], 10)
        existing = self.find_video_for_index(index)
        if existing:
            logging.info("video exists in the index [%s]", path.name)
        else:
            logging.info("new video added to index [%s]", path.name)
            cur.execute('INSERT OR IGNORE INTO main.videos (id, name, offset, uploaded, frame_count, fps, timecode) VALUES (?, ?, 0, false, 0, 0, ?)', [index, path.name, "00:00:00.00"])
            existing = self.find_video_for_index(index)
        is_dirty = False
        if index == 0 and existing.offset != 0:
            existing.offset = 0
            existing.timecode = Timecode()
            is_dirty = True
        if existing.frame_count == 0 or existing.fps == 0:
            video_properties = get_video_file_details(self.path / path)
            existing.fps = video_properties.get("fps")
            existing.duration = video_properties.get("duration")
            existing.frame_count = video_properties.get("frame_count")
        if index and existing.offset <= 0.0:
            previous = self.find_video_for_index(index-1)
            if previous:
                offset = previous.offset
                frame = cur.execute("SELECT id FROM main.frames WHERE offset = ?", [offset]).fetchone()
                if frame:
                    previous_frame_index = int(frame[0])
                    frame = cur.execute("SELECT offset FROM main.frames WHERE id = ?", [existing.frame_count + previous_frame_index]).fetchone()
                    if frame:
                        existing.offset = frame[0]
                        existing.timecode = Timecode.from_offset(float(frame[0]), existing.fps)
                        is_dirty = True
        if is_dirty:
            logging.info("saving updated meta into to index [%s]", path.name)
            cur.execute('UPDATE main.videos SET id = ?, name = ?, offset = ?, uploaded = ?, frame_count = ?, fps = ?, timecode = ?, duration = ? WHERE id = ?', [
                existing.id,
                existing.name,
                existing.offset,
                existing.uploaded,
                existing.frame_count,
                existing.fps,
                str(existing.timecode),
                existing.duration,
                existing.id,
            ])
        if not existing.uploaded and (index == 0 or existing.offset >= 0.0) and existing.frame_count > 0:
            logging.info("sending %s to be uploaded now", path.name)
            logging.info("ok, offset is %s", existing.offset)
            send_to_minio(self.path, {
                "name": path.name,
                "timestamp": self.timestamp_for_offset(existing.offset).isoformat(),
                "meta": {
                    "environment_id": ENV_ID,
                    "assignment_id": ASSIGNMENT_ID,
                    "camera_id": DEVICE_ID,
                    "path": f"{ENV_ID}/{ASSIGNMENT_ID}/{str((self.path / path).relative_to(self.path.parent))}",
                    "duration_seconds": existing.duration,
                    "fps": existing.fps,
                    "frame_offsets": self.load_offsets(existing.offset, existing.frame_count),
                }
            })
            cur.execute('UPDATE main.videos SET uploaded = true WHERE id = ?', [existing.id])
            logging.info("%s - %s", existing.name, existing.timecode)
        self.dbcon.commit()
        cur.close()

    def load_offsets(self, offset, frame_count):
        cur = self.dbcon.cursor()
        frames = cur.execute("SELECT id, offset FROM main.frames WHERE offset >= ? ORDER BY id LIMIT ?", [offset, frame_count]).fetchall()
        result = [f[1] for f in frames]
        cur.close()
        return result

    def timestamp_for_offset(self, offset):
        return self.start_datetime.add(microseconds=(offset*1000))

    def _load_timestamps(self):
        with (self.path / "video-frame.timestamps").open() as fp:
            stamps = fp.read()
        cur = self.dbcon.cursor()
        for i, frame in enumerate(stamps.split('\n')[1:]):
            if frame != "":
                cur.execute('INSERT OR IGNORE INTO main.frames (id, offset) VALUES (?, ?)', [i, frame])
                # tc = Timecode.from_offset(float(frame), 10)
        self.dbcon.commit()
        cur.close()
