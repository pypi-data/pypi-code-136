import datetime
import logging
from multiprocessing import Process, Queue
import os
import time

import yaml
from minio import Minio
from minio.error import MinioException
from picamera2 import Picamera2
from picamera2.encoders import Quality
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from libcamera import Transform


with open('/boot/wildflower-config.yml', 'r', encoding="utf-8") as fp:
    config = yaml.safe_load(fp.read())


DEVICE_ID = config.get("device_id", "unknown")
BUCKET = os.environ.get("MINIO_BUCKET_NAME", "videos")

CAMERA_RES = (os.environ.get("CAMERA_RES_W", 1296), os.environ.get("CAMERA_RES_H", 972))
CAMERA_FRAMERATE = os.environ.get("CAMERA_FRAMERATE", 10)
INTRA_PERIOD = os.environ.get("INTRA_PERIOD", 120)
BITRATE = os.environ.get("BITRATE", 1000000)
PERIOD = os.environ.get("DURATION", 120)
# CAMERA_ISO_SETTING = int(os.environ.get("CAMERA_ISO_SETTING", 400))
# CAMERA_EXPOSURE_MODE = os.environ.get("CAMERA_EXPOSURE_MODE", 'sports')
# CAMERA_SHUTTER_SPEED = int(os.environ.get("CAMERA_SHUTTER_SPEED", 0))
CAMERA_H_FLIP = os.environ.get("CAMERA_H_FLIP", 0)
CAMERA_V_FLIP = os.environ.get("CAMERA_V_FLIP", 0)




def next_timeslot(now):
    return now + (PERIOD - (now % PERIOD))


def capture_loop():
    logging.info("starting capture")
    try:
        transform = Transform()
        if CAMERA_H_FLIP=="yes" and CAMERA_V_FLIP=="yes":
            transform = Transform(hflip=True, vflip=True)
        elif CAMERA_H_FLIP=="yes":
            transform = Transform(hflip=True, vflip=False)
        elif CAMERA_V_FLIP=="yes":
            transform = Transform(hflip=False, vflip=True)
        camera = Picamera2()
        with camera:
            video_config = camera.create_video_configuration(main={"size": CAMERA_RES}, transform=transform, controls={"FrameRate": CAMERA_FRAMERATE})
            camera.configure(video_config)

            encoder = H264Encoder(BITRATE)

            logging.info(f"period is {PERIOD}")

            now = time.time()
            timeslot = next_timeslot(now)
            sleep_time = timeslot - now

            if sleep_time < 2:  # Ensure camera has enough time to adjust
                sleep_time += PERIOD
                timeslot += PERIOD
            logging.info(f"going to sleep for a bit {sleep_time}")
            time.sleep(sleep_time)

            video_start_time = datetime.datetime.fromtimestamp(timeslot)
            name = f'/data/video-{video_start_time:%Y_%m_%d_%H_%M-%S}.mp4'
            output = FfmpegOutput(name)
            while True:
                camera.start_and_record_video(output, encoder=encoder, quality=Quality.VERY_HIGH, duration=PERIOD)
                # camera.stop_recording()
                timeslot += PERIOD
                video_start_time = datetime.datetime.fromtimestamp(timeslot)
                name = f'/data/video-{video_start_time:%Y_%m_%d_%H_%M-%S}.mp4'
                output = FfmpegOutput(name)
                # camera.start_recording(encoder, output, quality=Quality.VERY_HIGH)
                # delay = timeslot + PERIOD - time.time()
                # logging.info(f"waiting {delay}")
                # time.sleep(delay)
    except Exception as e:
        logging.info(e)



def get_next_file():
    for item in os.listdir('/data'):
        if item.endswith(".mp4"):
            fname = f'/data/{item}'
            st = os.stat(fname)
            if (time.time() - st.st_mtime) > 11 and st.st_size > 300000:
                return fname
    return None


def upload_loop():
    minioClient = Minio(os.environ.get("MINIO_URL", "minio-service.classroom.svc.cluster.local:9000"),
                        access_key=os.environ.get("MINIO_KEY", "wildflower-classroom"),
                        secret_key=os.environ.get("MINIO_SECRET"),
                        secure=False)
    try:
        minioClient.make_bucket(BUCKET, location="us-east-1")
    except MinioException:
        pass
    while True:
        name = get_next_file()
        if name:
            try:
                ts = name[12:-4]
                obj_name = (f'{DEVICE_ID}/{ts}.mp4').replace("_", "/")
                logging.info(f"putting {obj_name} on minio")
                minioClient.fput_object(BUCKET, obj_name, name, content_type='video/mp4', metadata={
                                        "source": DEVICE_ID,
                                        "ts": ts,
                                        "duration": f"{PERIOD}s",
                                        })
                os.remove(name)
            except MinioException as err:
                logging.info(err)
                logging.info(f"failed to process {name}")
        else:
            logging.info("no files")
            time.sleep(1)
