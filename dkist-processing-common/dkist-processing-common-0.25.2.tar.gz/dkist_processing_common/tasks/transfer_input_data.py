"""Task(s) for the transfer in of data sources for a processing pipeline."""
import logging
from pathlib import Path
from typing import List

from dkist_processing_common.models.tags import Tag
from dkist_processing_common.tasks.base import WorkflowTaskBase
from dkist_processing_common.tasks.mixin.globus import GlobusMixin
from dkist_processing_common.tasks.mixin.globus import GlobusTransferItem
from dkist_processing_common.tasks.mixin.input_dataset import InputDatasetMixin

__all__ = ["TransferL0Data"]

logger = logging.getLogger(__name__)


class TransferL0Data(WorkflowTaskBase, GlobusMixin, InputDatasetMixin):
    """Transfers Level 0 data to the scratch store."""

    def download_input_dataset(self):
        """Get the input dataset document parts and save it to scratch with the appropriate tags."""
        if doc := self.metadata_store_input_dataset_observe_frames_part_document:
            self.write(doc.encode("utf-8"), tags=Tag.input_dataset_observe_frames())
        if doc := self.metadata_store_input_dataset_calibration_frames_part_document:
            self.write(doc.encode("utf-8"), tags=Tag.input_dataset_calibration_frames())
        if doc := self.metadata_store_input_dataset_parameters_part_document:
            self.write(doc.encode("utf-8"), tags=Tag.input_dataset_parameters())

    def format_transfer_items(self) -> List[GlobusTransferItem]:
        """Create the transfer_items list to be used by globus."""
        transfer_items = []
        for frame in self.input_dataset_frames:
            source_path = Path("/", frame.bucket, frame.object_key)
            destination_path = self.scratch.absolute_path(frame.object_key)
            transfer_items.append(
                GlobusTransferItem(
                    source_path=source_path,
                    destination_path=destination_path,
                    recursive=False,
                )
            )
        return transfer_items

    def tag_input_data(self, transfer_items: List[GlobusTransferItem]) -> None:
        """
        Tag all the input files with 'frame' and 'input' tags.

        Parameters
        ----------
        transfer_items
            List of items to be tagged
        Returns
        -------
        None
        """
        scratch_items = [
            self.scratch.scratch_base_path / ti.destination_path for ti in transfer_items
        ]
        for si in scratch_items:
            self.tag(si, tags=[Tag.input(), Tag.frame()])

    def run(self) -> None:
        """Execute the data transfer."""
        with self.apm_task_step("Change Status to InProgress"):
            self.metadata_store_change_recipe_run_to_inprogress()

        with self.apm_task_step("Download Input Dataset"):
            self.download_input_dataset()

        with self.apm_task_step("Format Transfer Items"):
            transfer_items = self.format_transfer_items()

        if not transfer_items:
            raise ValueError("No input dataset frames found")

        with self.apm_task_step("Transfer Inputs via Globus"):
            self.globus_transfer_object_store_to_scratch(
                transfer_items=transfer_items,
                label=f"Transfer Inputs for Recipe Run {self.recipe_run_id}",
            )

        with self.apm_processing_step("Tag Input Data"):
            self.tag_input_data(transfer_items=transfer_items)
