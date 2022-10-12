import functools
import io
import logging
import os
from pathlib import Path

from minio import Minio
from minio.error import MinioException
import yaml

from .config import DEVICE_ID

BUCKET = os.environ.get("MINIO_BUCKET_NAME", "videos")


@functools.cache
def get_client():
    minioClient = Minio(os.environ.get("MINIO_URL", "minio-service.classroom.svc.cluster.local:9000"),
                        access_key=os.environ.get("MINIO_KEY", "wildflower-classroom"),
                        secret_key=os.environ.get("MINIO_SECRET"),
                        secure=False)
    try:
        minioClient.make_bucket(BUCKET, location="us-east-1")
    except MinioException:
        pass
    return minioClient


def send_to_minio(data_dir, video_metadata):
    name = video_metadata["name"]
    rel_path = video_metadata["meta"]["path"]
    ts = video_metadata["timestamp"]
    try:
        obj_name = (f'{DEVICE_ID}/{rel_path}.meta')
        logging.info("putting %s metadata on minio", obj_name)
        data = yaml.safe_dump(video_metadata)
        get_client().put_object(BUCKET, obj_name, io.BytesIO(data.encode("utf8")), len(data), content_type='text/yaml', metadata={
                                "source": DEVICE_ID,
                                "ts": ts,
                                })
        obj_name = (f'{DEVICE_ID}/{rel_path}')
        logging.info("putting %s on minio", obj_name)
        get_client().fput_object(BUCKET, obj_name, data_dir / name, content_type='video/mp4', metadata={
                                "source": DEVICE_ID,
                                "ts": ts,
                                })
        # Path(data_dir / name).rename(data_dir / f"_{name}_")
        Path(data_dir / name).unlink()
    except MinioException as err:
        logging.info(err)
        logging.info("failed to process %s", name)
