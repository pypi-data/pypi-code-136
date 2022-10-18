"""ViSP lamp calibration task."""
import logging

import numpy as np
import scipy.ndimage as spnd
from dkist_processing_common.tasks.mixin.quality import QualityMixin
from dkist_processing_math.arithmetic import subtract_array_from_arrays
from dkist_processing_math.statistics import average_numpy_arrays

from dkist_processing_visp.models.tags import VispTag
from dkist_processing_visp.tasks.mixin.input_frame_loaders import InputFrameLoadersMixin
from dkist_processing_visp.tasks.mixin.intermediate_frame_helpers import (
    IntermediateFrameHelpersMixin,
)
from dkist_processing_visp.tasks.visp_base import VispTaskBase


class LampCalibration(
    VispTaskBase, IntermediateFrameHelpersMixin, InputFrameLoadersMixin, QualityMixin
):
    """
    Task class for calculation of the averaged lamp gain frame for a VISP calibration run.

    Parameters
    ----------
    recipe_run_id : int
        id of the recipe run used to identify the workflow run this task is part of
    workflow_name : str
        name of the workflow to which this instance of the task belongs
    workflow_version : str
        version of the workflow to which this instance of the task belongs

    """

    record_provenance = True

    def run(self):
        """
        For each beam.

            - Gather input lamp gain and averaged dark arrays
            - Calculate master lamp
            - Write master lamp
            - Record quality metrics

        Returns
        -------
        None

        """
        with self.apm_task_step(
            f"Generate lamp gains for {self.constants.num_beams} beams and {len(self.constants.lamp_exposure_times)} exposure times"
        ):
            for exp_time in self.constants.lamp_exposure_times:
                for beam in range(1, self.constants.num_beams + 1):
                    logging.info(f"Load dark for beam {beam}")
                    try:
                        dark_array = self.intermediate_frame_helpers_load_dark_array(
                            beam=beam, exposure_time=exp_time
                        )
                    except StopIteration:
                        raise ValueError(f"No matching dark found for {exp_time = } s")

                    for state_num in range(
                        1, self.constants.num_modstates + 1
                    ):  # modulator states go from 1 to n
                        logging.info(
                            f"Calculating average lamp gain for beam {beam}, modulator state {state_num}"
                        )
                        self.compute_and_write_master_lamp_gain_for_modstate(
                            modstate=state_num,
                            dark_array=dark_array,
                            beam=beam,
                            exp_time=exp_time,
                        )

        with self.apm_processing_step("Computing and logging quality metrics"):
            no_of_raw_lamp_frames: int = self.scratch.count_all(
                tags=[
                    VispTag.input(),
                    VispTag.frame(),
                    VispTag.task("LAMP_GAIN"),
                ],
            )

            self.quality_store_task_type_counts(
                task_type="LAMP_GAIN", total_frames=no_of_raw_lamp_frames
            )

    def compute_and_write_master_lamp_gain_for_modstate(
        self,
        modstate: int,
        dark_array: np.ndarray,
        beam: int,
        exp_time: float,
    ) -> None:
        """
        Compute and write master lamp gain for a given modstate and beam.

        Generally the algorithm is:
            1. Average input gain arrays
            2. Subtract average dark to get the dark corrected gain data
            3. Normalize each beam to unity mean
            4. Write to disk

        Parameters
        ----------
        modstate : int
            The modulator state to calculate the master lamp gain for

        dark_array : np.ndarray
            The master dark to be subtracted from each lamp gain file

        beam : int
            The number of the beam

        exp_time : float
            Exposure time

        Returns
        -------
        None
        """
        apm_str = f"{beam = }, {modstate = }, and {exp_time = }"
        # Get the input lamp gain arrays
        input_lamp_gain_arrays = self.input_frame_loaders_lamp_gain_array_generator(
            beam=beam, modstate=modstate, exposure_time=exp_time
        )

        with self.apm_processing_step(f"Computing gain for {apm_str}"):
            # Calculate the average of the input gain arrays
            averaged_gain_data = average_numpy_arrays(input_lamp_gain_arrays)
            # subtract dark
            dark_corrected_gain_data = next(
                subtract_array_from_arrays(averaged_gain_data, dark_array)
            )
            # normalize
            filtered_gain_data = self.high_pass_filter_gain(dark_corrected_gain_data)

        with self.apm_writing_step(f"Writing gain array for {apm_str}"):
            self.intermediate_frame_helpers_write_arrays(
                filtered_gain_data,
                beam=beam,
                task="LAMP_GAIN",
                modstate=modstate,
            )

        # These lines are here to help debugging and can be removed if really necessary
        filename = next(
            self.read(
                tags=[
                    VispTag.intermediate(),
                    VispTag.frame(),
                    VispTag.beam(beam),
                    VispTag.modstate(modstate),
                    VispTag.task("LAMP_GAIN"),
                ]
            )
        )
        logging.info(f"Wrote lamp gain for {beam=} and {modstate=} to {filename}")

    def high_pass_filter_gain(self, gain_array: np.ndarray) -> np.ndarray:
        """
        Normalize and filter gain by dividing it by a smoothed version of itself.

        The width of the smoothing kernel determines which spatial frequencies are "passed" by the filter; larger
        sigmas pass lower frequency signals.

        Parameters
        ----------
        gain_array : np.ndarray
            Dark corrected gain array for a single modulation state

        Returns
        -------
        gain_array : np.ndarray
            Normalized and filtered gain array for a single modulation state

        """
        # Identify regions that have very low flux. These are the hairlines
        med_spec = np.nanmedian(gain_array, axis=1)
        ratio = gain_array / med_spec[:, None]
        lidx = np.where(ratio < self.parameters.gain_hairline_fraction)

        logging.info(
            f"Detecting hairlines in lamp gain using hairline fraction = {self.parameters.gain_hairline_fraction}"
        )
        # Replace identified hairlines with data from the median spectrum
        gain_array[lidx] = med_spec[lidx[0]]

        # Filter out low-frequency response with a pseudo unsharp mask filter
        logging.info(
            f"High-pass filtering lamp gain with filter sigma = {self.parameters.lamp_high_pass_filter_width_px} px"
        )
        avg = spnd.gaussian_filter(gain_array, sigma=self.parameters.lamp_high_pass_filter_width_px)
        gain_array = gain_array / avg

        # Just to be safe. This probably doesn't do anything.
        gain_array /= np.nanmean(gain_array)

        return gain_array
