from .scene import LidarScene
from .transform import Transform
from .frame import LidarFrame
from .camera import LidarCamera
from .image import LidarImage
from .helper import (
    s3_smart_upload,
    format_lidar_point,
    format_point,
    format_quaternion,
    scale_file_upload,
    get_signed_url
)

from io import BytesIO
from functools import partial
from multiprocessing.pool import ThreadPool
from typing import MutableMapping, List, Dict
from urllib.parse import urlparse
from typing import Any

import pandas as pd
import numpy as np

import ujson
import nucleus

UPLOAD_POOL_SIZE = 8

#Formatting Helpers

def get_image_url_path(path, camera_id, frame_id):
    return f"{path}/image-{camera_id}-{frame_id}.jpg"

def get_image_ref_id(ref_id_prefix, camera_id, frame_id):
    return f"{ref_id_prefix}-{camera_id}-image-{frame_id}"

def get_pointcloud_ref_id(ref_id_prefix, frame_id):
    return f"{ref_id_prefix}-pointcloud-{frame_id}"

def get_scene_ref_id(ref_id_prefix):
    return f"{ref_id_prefix}-scene"

class Cuboid():
    '''Work in progress class - need to fill out'''
    def __init__(self, position: np.ndarray, yaw: float):
        self.position: np.ndarray = np.zeroes((0,3), dtype = float)
        self.yaw: float = None

class NucleusLidarFrame(LidarFrame):
    '''Overloaded Nucleus Frame class

    Annotation and predictions are next up for implementation
    '''

    def __init__(self, frame_id, cameras):
        self.id = frame_id
        self.cameras: pd.Series[Any, LidarCamera] = cameras
        self.images: pd.Series[Any, LidarImage] = pd.Series(dtype=object)
        self.points: np.ndarray = np.zeros((0, 5), dtype=float)
        self.pointcloud_metadata: dict = {}
        self.radar_points: np.ndarray = np.zeros((0, 3), dtype=float)
        self.colors: np.ndarray = np.zeros((0, 3), dtype=float)
        self.transform = Transform()
        self.annotations: pd.Series[Any,Cuboid] = pd.Series(dtype=object)
        self.predictions: pd.Series[Any,Cuboid] = pd.Series(dtype=object)

    def add_points(
        self, points: np.array, transform: Transform = None, metadata: dict = None, intensity=1, sensor_id=0,
    ):
        """Add points to the frame, structure: np.array with dimension 1 and shape (N,3) or (N,4) (N being the number of point in the frame)

        Points with intensity:

        .. highlight:: python
        .. code-block:: python

          points = np.array([
            [0.30694541, 0.27853175, 0.51152715, 0.4],
            [0.80424087, 0.24164057, 0.45256181, 1],
            ...
          ])

        Points without intensity:

        .. highlight:: python
        .. code-block:: python

          points = np.array([
            [0.30694541, 0.27853175, 0.51152715],
            [0.80424087, 0.24164057, 0.45256181],
            ...
          ])

        :param points: List of points
        :type points: np.array
        :param transform: Transform that should be applied to the points
        :type transform: Transform
        :param metadata: Any pointcloud metadata to be associated with dataset item
        :type metadata: dict
        :param intensity: If the points list doesn't include intensity, this value will be used as intensity for all the points (default ``1``)
        :type intensity: int
        :param sensor_id: Sensor id, used in case that you have more than one lidar sensor. (Default ``0``)
        :type sensor_id: int

        """
        if points.ndim == 1:
            points = np.array([points])
        if points.shape[1] == 3:
            points = np.hstack([points, np.ones((points.shape[0], 1)) * intensity])
        if transform is not None:
            points = transform.apply(points)

        points = np.hstack([points, np.ones((points.shape[0], 1)) * sensor_id])

        self.points = np.vstack([self.points, points])
        self.pointcloud_metadata = metadata

    def to_json(
        self,
        base_url: str = "",
        s3_upload: bool = True,
        project_name: str = ""
    ):
        """Returns pointcloud json

        :param base_url: This url will concatenated with the frame name
        :type base_url: str
        :returns: Frame object as a JSON formatted stream
        :rtype: str

        """

        points_json = pd.DataFrame(
            self.get_world_points(), columns=["x", "y", "z", "i", "d"]
        ).to_json(double_precision=4, orient="records", date_format=None)

        frame_object = {
            "points": "__POINTS__",
            "device_position": format_point(self.transform.position),
            "device_heading": format_quaternion(self.transform.quaternion),
        }

        out = ujson.dumps(frame_object)
        out = out.replace('"__POINTS__"', points_json)

        return out

    def s3_upload(self, bucket: str, path: str):
        """Save frame in S3

        :param bucket: S3 Bucket name
        :type bucket: str
        :param path: Path to store data
        :type key: str
        """
        # print(f'Uploading frame {self.id}...')
        base_url = f"s3://{bucket}/{path}"

        # Upload frame json file
        s3_smart_upload(
            fileobj=BytesIO(
                bytes(self.to_json(base_url), encoding="utf-8")
            ),
            bucket=bucket,
            key=f"{path}/frame-{self.id}.json",
            content_type="application/json",
        )

        # Upload images
        for camera_id, image in self.images.items():
            image.s3_upload(bucket, f"{path}/image-{camera_id}-{self.id}.jpg")

    def generate_cam_nucleus_dataset_items(
        self,
        scene_dict: dict,
        ref_id_prefix: str,
        presigned_items: bool = False
    ):
        """Generates all necessary camera dataset items for corresponding LidarFrame

        :param scene_dict: Mapping from frame and camera images to URL
        :type scene_dict: str
        :param ref_id_prefix: String insert at beginning of automatically generated ref-id, required
        :type ref_id_prefix: str
        :param presigned_items: Presigns all URLs via S3
        :type presigned_items: str
        :returns: Dictionary of Nucleus image dataset items associated with camera ID
        :rtype: Dict

        """
        assert ref_id_prefix is not "", "Please set a Reference ID prefix to ensure reference idempotency."

        def generate_camera_params(self, camera):
            """Generates camera specific metadata for nucleus dataset item"""
            wct = self.transform @ camera.pose

            heading = format_quaternion(wct.quaternion)
            position = format_point(wct.translation)
            camParams = {
                "cx": float(camera.cx),
                "cy": float(camera.cy),
                "fx": float(camera.fx),
                "fy": float(camera.fy),
                "k1": float(camera.D[0]),
                "k2": float(camera.D[1]),
                "p1": float(camera.D[2]),
                "p2": float(camera.D[3]),
                "k3": float(camera.D[4]),
                "k4": float(camera.D[5]),
                "k5": float(camera.D[6]) if len(camera.D) >= 7 else 0,
                "k6": float(camera.D[7]) if len(camera.D) >= 8 else 0,
                "heading": heading,
                "position": position,
                "camera_model": camera.model,
            }
            return camParams

        nucleus_camera_items = {}
        for camera in self.cameras:
            camera_params = generate_camera_params(self, camera)
            image_location = scene_dict["cameras"][camera.id][self.id]

            if presigned_items:
                image_location = get_signed_url(
                    bucket=urlparse(image_location).netloc,
                    path=urlparse(image_location).path[1:],
                )

            item_metadata = {"camera_params": camera_params}

            if self.images[camera.id].metadata:
                item_metadata = dict(self.images[camera.id].metadata, **item_metadata)

            item = nucleus.DatasetItem(
                image_location=image_location,
                reference_id=get_image_ref_id(ref_id_prefix,camera.id,self.id),
                metadata=item_metadata,
            )
            nucleus_camera_items[str(camera.id)] = item

        return nucleus_camera_items


class NucleusLidarScene(LidarScene):
    '''Overloaded Nucleus scene'''
    def __init__(self):
        """
        :rtype: object
        """
        self.cameras: MutableMapping[LidarCamera] = pd.Series()
        self.frames: MutableMapping[NucleusLidarFrame] = pd.Series()
        self.base_url = None
        self.scale_file_attachments = None
        self.ref_id_prefix = ""

    def from_LidarScene(self, LidarScene):
        self.cameras = LidarScene.cameras
        for frame_idx, LidarFrame in enumerate(LidarScene.frames):
            self.get_frame(frame_idx).points = LidarFrame.points
            self.get_frame(frame_idx).images = LidarFrame.images
            self.get_frame(frame_idx).transform = LidarFrame.transform
        return self

    def set_ref_id_prefix(self, ref_id_prefix: str):
        self.ref_id_prefix = ref_id_prefix

    def to_dict(self, base_url: str = None) -> dict:
        """Return a dictionary with the frame urls using the base_url as base.

        :param base_url: This url will be concatenated with the frames name, e.g.: `'%s/frame-%s.json' % (base_url, frame.id)`
        :type base_url: str
        :return: Dictionary with the frame urls data
        :rtype: dict

        """
        if base_url is None:
            base_url = self.base_url

        cameras = {}
        for camera in self.cameras:
            cameras[camera.id] = [
                "%s/image-%s-%s.jpg" % (base_url, camera.id, frame.id)
                for frame in self.frames
            ]

        return dict(
            frames=["%s/frame-%s.json" % (base_url, frame.id) for frame in self.frames],
            cameras=cameras,
        )

    def get_frame(self, frame_id=None, index: int = None) -> NucleusLidarFrame:
        """Get a frame by id (or index) or create one if it does not exist

        :param frame_id: The frame id
        :type frame_id: str, int
        :param index: The frame index
        :type index: int

        :return: NucleusLidarFrame
        :rtype: NucleusLidarFrame

        """
        assert (
            frame_id is not None or index is not None
        ), "id or index must be specified"

        if frame_id is None:
            frame_id = self.frames.index[index]

        if frame_id not in self.frames:
            if isinstance(frame_id, int):
                self.frames.index = self.frames.index.astype(int)
            self.frames[frame_id] = NucleusLidarFrame(frame_id, cameras=self.cameras)
        return self.frames[frame_id]

    def s3_upload(
        self,
        bucket: str,
        path=None,
        mock_upload: float = False,
        use_threads: float = True
    ):
        """Overloaded S3 upload function

        :param bucket: S3 Bucket name
        :type bucket: str
        :param path: Path to store data
        :type key: str
        :param mock_upload: To avoid upload the data to S3  (defualt ``False``)
        :type mock_upload: float
        :param use_threads: In order to upload multiple files at the same time using threads  (defualt ``True``)
        :type use_threads: float

        :return: Scene S3 url
        :rtype: str

        """
        self.base_url = f"s3://{bucket}/{path}"

        print("Uploading scene to S3: %s" % self.base_url)
        scene_dict = self.to_dict(self.base_url)

        poses_csv = pd.DataFrame(
            self.frames.map(lambda f: list(f.transform.matrix.reshape(-1))).to_dict()
        ).T.to_csv(header=False)

        if not mock_upload:
            # Upload scene json file
            s3_smart_upload(
                bucket=bucket,
                key=f"{path}/scene.json",
                fileobj=BytesIO(bytes(ujson.dumps(scene_dict), encoding="utf-8")),
                content_type="application/json",
            )

            # Upload ego2world csv file
            s3_smart_upload(
                bucket=bucket,
                key=f"{path}/ego2world.csv",
                fileobj=BytesIO(bytes(poses_csv, encoding="utf-8")),
                content_type="text/plain",
            )

            if use_threads:
                p = ThreadPool(processes=UPLOAD_POOL_SIZE)
                func = partial(
                    NucleusLidarFrame.s3_upload,
                    bucket=bucket,
                    path=path
                )
                p.map(func, self.frames)
            else:
                for frame in self.frames:
                    frame.s3_upload(bucket, path)

        signed_url = get_signed_url(bucket, f"{path}/scene.json")

        print(f"Scene uploaded: {signed_url}")
        return self.base_url

    def generate_nucleus_scene(
        self,
        ref_id_prefix: str = "",
        presigned_items: bool = False
    ) -> nucleus.LidarScene:
        """Generates the Nucleus Scene object that can be asynchronously uploaded to the platform

        :param ref_id_prefix: a prefix that can be added to reference ID of the scene and dataset items to ensure unique values, if not already existent
        :type ref_id_prefix: string
        :param presigned_items: Dictates that all items involved in Nucleus scene are presigned via S3
        :type presigned_items: bool

        :returns: the fully constructed Nucleus LidarScene
        :type LidarScene: nucleus.LidarScene
        """

        if ref_id_prefix is not "":
            self.ref_id_prefix = ref_id_prefix

        assert self.ref_id_prefix is not "", "Please set a Reference ID prefix to ensure reference idempotency."

        scene_dict = self.to_dict()
        nucleus_frames = []
        for frame_idx, frame in enumerate(self.frames):

            cam_items = frame.generate_cam_nucleus_dataset_items(
                scene_dict=self.to_dict(),
                ref_id_prefix=self.ref_id_prefix,
                presigned_items=presigned_items,
            )

            pointcloud_location = scene_dict["frames"][frame_idx]

            if presigned_items:
                pointcloud_location = get_signed_url(
                    bucket=urlparse(pointcloud_location).netloc,
                    path=urlparse(pointcloud_location).path[1:],
                )

            nucleus_frame = nucleus.Frame(
                lidar=nucleus.DatasetItem(
                    pointcloud_location=pointcloud_location,
                    metadata=frame.pointcloud_metadata,
                    reference_id=get_pointcloud_ref_id(self.ref_id_prefix, frame_idx)
                ),
                **cam_items,
            )

            nucleus_frames.append(nucleus_frame)

        return nucleus.LidarScene(
            reference_id=get_scene_ref_id(self.ref_id_prefix), frames=nucleus_frames
        )