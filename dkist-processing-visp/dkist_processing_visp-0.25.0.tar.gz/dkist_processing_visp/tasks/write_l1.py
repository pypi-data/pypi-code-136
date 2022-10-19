"""Visp write L1 task."""
import logging
import uuid
from datetime import datetime
from typing import Literal

import numpy as np
from astropy.io import fits
from astropy.time import Time
from dkist_processing_common.tasks import WriteL1Frame

from dkist_processing_visp.models.constants import VispConstants


class VispWriteL1Frame(WriteL1Frame):
    """
    Task class for writing out calibrated l1 ViSP frames.

    Parameters
    ----------
    recipe_run_id : int
        id of the recipe run used to identify the workflow run this task is part of
    workflow_name : str
        name of the workflow to which this instance of the task belongs
    workflow_version : str
        version of the workflow to which this instance of the task belongs
    """

    @property
    def constants_model_class(self):
        """Get Visp pipeline constants."""
        return VispConstants

    def add_dataset_headers(
        self, header: fits.Header, stokes: Literal["I", "Q", "U", "V"]
    ) -> fits.Header:
        """
        Add the VISP specific dataset headers to L1 FITS files.

        Parameters
        ----------
        header : fits.Header
            calibrated data header

        stokes :
            stokes parameter

        Returns
        -------
        fits.Header
            calibrated header with correctly written l1 headers
        """
        # Correct the headers for the number of map and scan steps per map due to potential observation aborts
        header["VSPNMAPS"] = self.constants.num_map_scans
        header["VSPNSTP"] = self.constants.num_raster_steps

        if stokes.upper() not in self.constants.stokes_params:
            raise ValueError("The stokes parameter must be one of I, Q, U, V")

        # Dynamically assign dataset axes based on CTYPEs in the L0 headers
        axis_types = [
            self.constants.axis_1_type,
            self.constants.axis_2_type,
            self.constants.axis_3_type,
        ]
        for i, axis_type in enumerate(axis_types, start=1):
            if axis_type == "HPLT-TAN":
                header[f"DNAXIS{i}"] = header[f"NAXIS{i}"]
                header[f"DTYPE{i}"] = "SPATIAL"
                header[f"DPNAME{i}"] = "spatial along slit"
                header[f"DWNAME{i}"] = "helioprojective latitude"
                header[f"DUNIT{i}"] = header[f"CUNIT{i}"]
            elif axis_type == "AWAV":
                header[f"DNAXIS{i}"] = header[f"NAXIS{i}"]
                header[f"DTYPE{i}"] = "SPECTRAL"
                header[f"DPNAME{i}"] = "dispersion axis"
                header[f"DWNAME{i}"] = "wavelength"
                header[f"DUNIT{i}"] = header[f"CUNIT{i}"]
                # The wavemin and wavemax assume that all frames in a dataset have identical wavelength axes
                header["WAVEMIN"] = header[f"CRVAL{i}"] - (
                    header[f"CRPIX{i}"] * header[f"CDELT{i}"]
                )
                header["WAVEMAX"] = header[f"CRVAL{i}"] + (
                    (header[f"NAXIS{i}"] - header[f"CRPIX{i}"]) * header[f"CDELT{i}"]
                )
            elif axis_type == "HPLN-TAN":
                header[f"DNAXIS{i}"] = self.constants.num_raster_steps
                header[f"DTYPE{i}"] = "SPATIAL"
                header[f"DPNAME{i}"] = "raster scan step number"
                header[f"DWNAME{i}"] = "helioprojective longitude"
                header[f"DUNIT{i}"] = header[f"CUNIT{i}"]
                # Current position in raster scan which counts from zero
                header[f"DINDEX{i}"] = header["VSPSTP"] + 1
            else:
                raise ValueError(
                    f"Unexpected axis type. Expected ['HPLT-TAN', 'AWAV', 'HPLN-TAN']. Got {axis_type}"
                )

        # Set the base number of dataset axes to 3
        num_axis = 3

        # ---Temporal---
        if self.constants.num_map_scans > 1:
            num_axis += 1
            header[
                f"DNAXIS{num_axis}"
            ] = self.constants.num_map_scans  # total number of raster scans in the dataset
            header[f"DTYPE{num_axis}"] = "TEMPORAL"
            header[f"DPNAME{num_axis}"] = "raster map repeat number"
            header[f"DWNAME{num_axis}"] = "time"
            header[f"DUNIT{num_axis}"] = "s"
            # Temporal position in dataset
            header[f"DINDEX{num_axis}"] = header["VSPMAP"]  # Current raster scan

        # ---Stokes---
        if self.constants.correct_for_polarization:
            num_axis += 1
            header[f"DNAXIS{num_axis}"] = 4  # I, Q, U, V
            header[f"DTYPE{num_axis}"] = "STOKES"
            header[f"DPNAME{num_axis}"] = "polarization state"
            header[f"DWNAME{num_axis}"] = "polarization state"
            header[f"DUNIT{num_axis}"] = ""
            # Stokes position in dataset - stokes axis goes from 1-4
            header[f"DINDEX{num_axis}"] = self.constants.stokes_params.index(stokes.upper()) + 1

        else:
            logging.info("Spectrographic data detected. Not adding DNAXIS information.")

        header["DNAXIS"] = num_axis
        header["DAAXES"] = 2  # Spectral, spatial
        header["DEAXES"] = num_axis - 2  # Total - detector axes

        # VISP has a wavelength axis in the frame and so FRAMEWAV is hard to define. Use LINEWAV.
        header["LEVEL"] = 1
        header["WAVEBAND"] = self.constants.spectral_line
        header["WAVEUNIT"] = -9  # nanometers
        header["WAVEREF"] = "Air"

        # Binning headers
        header["NBIN1"] = 1
        header["NBIN2"] = 1
        header["NBIN3"] = 1
        header["NBIN"] = header["NBIN1"] * header["NBIN2"] * header["NBIN3"]

        return header

    def _replace_header_values(self, header: fits.Header, data: np.ndarray) -> fits.Header:
        """
        Replace the FILE_ID and DATE keywords with new values.

        This is overloaded from dkist-processing-common because DATE-END is computed correctly in ScienceCalibration
        and the *-common version of this method would overwrite that key.
        """
        header["FILE_ID"] = uuid.uuid4().hex
        header["DATE"] = Time(datetime.now().isoformat(), precision=6).fits
        # Remove BZERO and BSCALE as their value should be recalculated by astropy upon fits write
        header.pop("BZERO", None)
        header.pop("BSCALE", None)
        # Make sure that NAXIS is set to the shape of the data in case of squeezing
        header["NAXIS"] = len(data.shape)
        return header
