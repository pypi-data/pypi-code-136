from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dicom_cnn.reader.nifti_reader import NiftiReader


class MaskReader(NiftiReader):
    mask_path= str

    def set_location (self, mask_location):
        mask_location = self.mask_path

    def reader(self):
        if self.set_location.endswith('.nii'):
            mask_array= self.get_array(self.mask_path)
            mask_direction = self.get_direction(self.mask_path)
            mask_origin= self.get_origin(self.mask_path)
            mask_size= self.getsize(self.mask_path)

        return mask_array, mask_direction, mask_origin, mask_size