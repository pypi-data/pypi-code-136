"""
Utilities to handle exotic file formats (not GeoTiff), particularly DIMAP and NETCDF.
"""
from pathlib import Path

# pylint: disable=C0411
from typing import Dict, List, Optional, Tuple
from xml.etree import ElementTree

import numpy as np
import rasterio as rio
from geojson import Feature
from rasterio.mask import mask
from shapely.geometry import shape

from blockutils.datapath import set_data_path
from blockutils.exceptions import SupportedErrors, UP42Error


def update_jsonfile(feature: Feature, output_name: str) -> Feature:
    """
    This method updates properties of a feature with a new file path.

    Arguments:
        feature: Input feature object.
        output_name: Output file path from main working folder (i.e. output.tif).

    Returns:
        Feature object with the updated data path to output_name.
    """
    new_feature = Feature(geometry=feature["geometry"], bbox=feature["bbox"])
    prop_dict = feature["properties"]
    meta_dict = {
        k: v
        for k, v in prop_dict.items()
        if not (k.startswith("up42.") or k.startswith("custom."))
    }
    new_feature["properties"] = meta_dict
    set_data_path(new_feature, output_name)
    return new_feature


MS = "ms"
PMS = "pms"
PAN = "pan"


class DimapFile:
    """
    Base class for handling DIMAP files.
    """

    SPECTRA_MAPPING = {
        "PMS": PMS,
        "PMS-FS": PMS,
        "MS-FS": MS,
        "MS": MS,
        "P": PAN,
        "PAN": PAN,
        "P-FS": PAN,
        "PAN-FS": PAN,
    }

    def __init__(self, base_path: Path = Path("/tmp/input")):
        """
        Arguments:
            base_path: Main input working folder.
        """
        self.base_path = base_path

    def _get_dimap_path(self, feature):
        dimap_file_id = feature.properties.get("up42.data_path")
        return self.base_path / dimap_file_id

    def check_dtype(self, feature: Feature) -> str:
        """
        This method opens the xml file related to the image and check for the
        data type of the image.
        Args:
            feature: Input feature.

        Returns:
            Dtype of the image.

        """
        ACCEPTED_TYPES = ["uint16", "uint8"]
        dimap_path = self._get_dimap_path(feature)
        data_paths = self._get_data_paths(dimap_path)
        if data_paths:
            paths = list(data_paths.values())[0]
            with rio.open(paths.get("metadata")) as src:
                dtype = src.profile.get("dtype")
                if dtype not in ACCEPTED_TYPES:
                    raise UP42Error(
                        SupportedErrors.WRONG_INPUT_ERROR,
                        f"Input dtype must be one of {ACCEPTED_TYPES}."
                        "Instead got {dtype}",
                    )
                return dtype

    @staticmethod
    def open_xml_file_with_rasterio(path: Path) -> rio.io.DatasetReader:
        """
        This method open xml file with rasterio.
        Args:
            path: Path to the xml file.

        Returns:
            Rasterio DatasetReader.
        """
        img_name = Path(path).joinpath(list(path.glob("DIM_*"))[0].name)

        return rio.open(img_name)

    def _get_data_paths(
        self, dimap_path: Path
    ) -> Dict[str, Dict[str, Path or List(Path)]]:
        """Reads the Airbus DIMAP dataset and returns the essential paths in the format:
        {
            "PMS": {
                "base": "BASE PATH OF PMS PRODUCT",
                "metadta": "PATH OF PMS PRODUCT METADATA",
                "data":["PATHS OF PMS PRODUCT"]
            },
            "MS":{...},
            "P": {...}
        }

        Returns:
            Dict[str, Dict[str, Path or List[Path]]]: Paths
        """

        root_metadata_patterns = ["**/*VOL*.xml", "**/*VOL*.XML"]
        root_metadata_files = set()
        for pattern in root_metadata_patterns:
            for file in dimap_path.glob(pattern):
                root_metadata_files.add(file)

        if not root_metadata_files:
            raise UP42Error(
                SupportedErrors.WRONG_INPUT_ERROR, "Input file isn't DIMAP file"
            )

        if len(root_metadata_files) > 1:
            raise UP42Error(
                SupportedErrors.WRONG_INPUT_ERROR,
                "Input file has more than one product. Multiple product read "
                "isn't supported",
            )

        root_metadata_file = root_metadata_files.pop()
        data_paths = {}
        component_paths = set()

        et_root = ElementTree.parse(root_metadata_file).getroot()
        for component in et_root.findall(".//Component"):
            component_type = component.find("COMPONENT_TYPE")
            if component_type is None:
                raise UP42Error(
                    SupportedErrors.WRONG_INPUT_ERROR,
                    "Input file doesn't include the Component info.",
                )
            if (component_type.text or "").strip() != "DIMAP":
                continue

            rel_component_uri = component.find("COMPONENT_PATH").attrib.get("href")
            component_paths.add(root_metadata_file.parent / rel_component_uri)

        for component_path in component_paths:
            component_root = ElementTree.parse(component_path).getroot()

            spectral_processing = component_root.find(".//SPECTRAL_PROCESSING")
            if spectral_processing is None:
                raise UP42Error(
                    SupportedErrors.WRONG_INPUT_ERROR,
                    "Input file doesn't include the Spectral Processing info.",
                )

            spectral_processing = (spectral_processing.text or "").strip()
            if not self.SPECTRA_MAPPING.get(spectral_processing):
                raise UP42Error(
                    SupportedErrors.WRONG_INPUT_ERROR,
                    "Ding! Ding! Ding! New spectral type found for input file."
                    "Reach out to customer support.",
                )

            data_paths[self.SPECTRA_MAPPING.get(spectral_processing)] = dict(
                base=component_path.parent,
                metadata=component_path,
                data=[
                    component_path.parent / c.attrib.get("href")
                    for c in component_root.findall(".//Data_Access//DATA_FILE_PATH")
                ],
            )
        return data_paths

    def dimap_file_path(
        self, feature: Feature
    ) -> Tuple[Optional[Path], Optional[Path]]:
        """
        This methods returns the folder name of the MS and PAN files.
        (e.g. IMG_PHR1B_MS_001, IMG_PHR1B_PS_002)

        Arguments:
            feature: Input feature.

        Returns:
            Path to multispectral and panchromatic directory.
        """
        dimap_path = self._get_dimap_path(feature)
        data_paths = self._get_data_paths(dimap_path)

        return data_paths.get(MS, {}).get("base"), data_paths.get(PAN, {}).get("base")

    def dimap_8bit_file_path(self, feature: Feature) -> Optional[Path]:
        """
        This methods returns the folder name of the PMS file.
        (e.g. IMG_PHR1B_PMS_001)

        Arguments:
            feature: Input feature.

        Returns:
            Path to pan-sharpened multispectral image directory.
        """
        dimap_path = self._get_dimap_path(feature)
        data_paths = self._get_data_paths(dimap_path)
        return data_paths.get(PMS, {}).get("base")

    def get_meta_input(self, feature: Feature, mode: str) -> dict:
        """
        This method returns the profile of the input image.

        Arguments:
            feature: Input feature object.
            mode: `ms` or `pan` depending on the profile to be returned.

        Returns:
            Rasterio profile object.
        """
        dimap_path = self._get_dimap_path(feature)
        if mode == "rgb-ned":
            # Opening a pleiades neo image by pointing to the DIM_*.XML file is currently not supported
            # by rasterio/gdal. We open each file separately and merge them together.
            with rio.open(dimap_path) as src:
                src_profile = src.profile
                src_profile.update(count=6)
                return src_profile

        data_paths = self._get_data_paths(dimap_path)
        metadata_path = data_paths.get(mode, {}).get("metadata")
        if metadata_path:
            with rio.open(metadata_path) as src:
                return src.profile

    def get_dim_xml_path(
        self, feature: Feature
    ) -> Tuple[Optional[Path], Optional[Path]]:
        """
        This method returns the path to the input image.
        (e.g. IMG_PHR1B_PMS_001/DIM_PHR1B_MS_201810161039434_ORT_15007a44-dffa-41fe-c109-0d4fecabd40b-001.XM)
        Arguments:
            feature: Input feature object.

        Returns:
            Paths to multispectral and panchromatic XML files.
        """
        dimap_path = self._get_dimap_path(feature)
        data_paths = self._get_data_paths(dimap_path)
        return (
            data_paths.get(MS, {}).get("metadata"),
            data_paths.get(PAN, {}).get("metadata"),
        )

    def read_image_as_raster(self, feature: Feature, mode: str) -> np.ndarray:
        """
        This method returns the input image in a numpy array format.

        Arguments:
            feature: Input feature object.
            mode: `ms` or `pan` depending on the array to be returned.

        Returns:
            Imagery in numpy array format.
        """
        dimap_path = self._get_dimap_path(feature)
        if mode == "rgb-ned":
            # Opening a pleiades neo image by pointing to the DIM_*.XML file is currently not supported
            # by rasterio/gdal. We open each file separately and merge them together.
            ned_file = dimap_path.parent / dimap_path.name.replace("_RGB_", "_NED_")
            with rio.open(dimap_path) as rgb, rio.open(ned_file) as ned:
                return np.concatenate((rgb.read(), ned.read()), axis=0)

        data_paths = self._get_data_paths(dimap_path)
        metadata_path = data_paths.get(mode, {}).get("metadata")
        if metadata_path:
            with rio.open(metadata_path) as src:
                return src.read()

    # pylint: disable=too-many-locals
    def clip_and_read_image_as_raster(
        self, feature: Feature, mode: str, clipping_geometry: dict
    ):
        """
        This method returns the input image in a numpy array format.
        """

        def clip(src, shapes=[clipping_geometry]):
            data, transform = mask(dataset=src, shapes=shapes, crop=True)
            out_meta = src.meta.copy()
            out_meta.update(
                {
                    "driver": "GTiff",
                    "height": data.shape[1],
                    "width": data.shape[2],
                    "count": src.count,
                    "transform": transform,
                }
            )
            return data, out_meta

        clipping_polygon = shape(clipping_geometry)
        image_extents_polygon = shape(feature["geometry"])
        if not image_extents_polygon.intersects(clipping_polygon):
            raise UP42Error(
                SupportedErrors.INPUT_PARAMETERS_ERROR,
                "AOI must intersect image extents.",
            )

        dimap_path = self._get_dimap_path(feature)
        # Opening pleiades neo by pointing to the DIM_*.XML is still not
        # supported by rasterio/gdal. When that happens, the following can be
        # replaced by rio.open(DIM_*.XML) as for pleiades and spot in the
        # if-else section above.
        if mode == "rgb-ned":
            ned_file = dimap_path.parent / dimap_path.name.replace("_RGB_", "_NED_")
            with rio.open(dimap_path) as rgb, rio.open(ned_file) as ned:
                rgb_array, rgb_meta = clip(rgb)
                ned_array, ned_meta = clip(ned)
                data = np.concatenate((rgb_array, ned_array), axis=0)
                meta = {**rgb_meta, **ned_meta, "count": rgb.count + ned.count}
                return data, meta

        data_paths = self._get_data_paths(dimap_path)
        metadata_path = data_paths.get(mode, {}).get("metadata")
        if metadata_path:
            with rio.open(metadata_path) as src:
                return clip(src)


class NetCDFFile:
    """
    Base class for handling NETCDF files.
    """

    def __init__(self, base_path: Path = Path("/tmp/input")):
        """
        Arguments:
            base_path: Main input working folder.
        """
        self.base_path = base_path

    def path_to_nc_file(self, feature: Feature) -> Path:
        """
        This methods returns the file name based on the given params.

        Arguments:
            feature: Input feature object.

        Returns:
            Path to input NETCDF file.
        """
        nc_file_id = feature.properties.get("up42.data_path")
        nc_path = self.base_path.joinpath(nc_file_id)

        return nc_path
