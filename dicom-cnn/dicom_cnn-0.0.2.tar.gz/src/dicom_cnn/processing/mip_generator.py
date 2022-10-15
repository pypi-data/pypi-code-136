import numpy as np 
import scipy.ndimage
import imageio
from multiprocessing import Pool, cpu_count
import imageio.core.util

def silence_imageio_warning(*args, **kwargs):
    pass

class MIPGeneratorSingleThread: 
    """a class to generate MIP"""

    def __init__(self, numpy_array: np.ndarray, frames: int, delay :float, projection :int) -> None:
        """constructor

        Args:
            numpy_array (np.ndarray): [3D np.ndarray of shape (z,y,x) or 4D np.ndarray of shape (z,y,x,c)]
        """
        self.numpy_array = numpy_array
        self.frames = frames
        self.delay = delay / 1000
        self.projection = projection
        imageio.core.util._precision_warn = silence_imageio_warning

    def _project(self, angle:int) -> np.ndarray:
        """function to generate 2D MIP of a 3D (or 4D) ndarray of shape (z,y,x) (or shape (z,y,x,C)) 

        Args:
            angle (int): [angle of rotation of the MIP, 0 for coronal, 90 saggital ]

        Returns:
            [np.ndarray]: [return the MIP np.ndarray]
        """
        vol_angle = scipy.ndimage.rotate(
            self.numpy_array, angle=angle, reshape=False, axes=(1, 2))
        MIP = np.amax(vol_angle, axis=1)
        MIP = np.flip(MIP, axis=0)
        return MIP

    def _create_projection_list(self) -> list:
        """Function to create a list of 2D MIP

        Returns:
            list: [list of 2D MIP]
        """
        angles = np.linspace(0, self.projection, self.frames)
        """nbCores = cpu_count() - 2
        pool = Pool(nbCores)
        projection_list = pool.map(self._project, angles)
        """
        projection_list = []
        for angle in angles:
            projection_list.append(self._project(angle))
        return projection_list

    def create_gif(self, output) -> None:
        """Function to create a gif from a 3D Array

        Args:
            output : [Where to save the gif]

        Returns:
            [None]: [None]
        """
        projection_list = self._create_projection_list()
        imageio.mimwrite(output, projection_list, format='.gif', duration=self.delay)

    @classmethod
    def transform_to_nan(cls, mip:np.ndarray) -> np.ndarray:
        """function to replace pixel with value 0 with np.NaN

        Args:
            mip (np.ndarray): [2D np.ndarray of MIP]

        Returns:
            (np.ndarray): [2D np.ndarray NaN of MIP]
        """
        mip[mip == 0] = np.NaN
        return mip

    @classmethod
    def save_projection_two_modality(cls, pet_array:np.ndarray, mask_array:np.ndarray, angle:int) -> np.ndarray:
        """function to generate a MIP of PET/MASK and save it as png image

        Args:
            pet_array (np.ndarray): [3D np.ndarray of shape (z,y,x)]
            mask_array (np.ndarray): [3D np.ndarray of shape (z,y,x)]
            angle (int): [angle of the MIP rotation]
            
        Returns:
            [np.ndarray]: [return the MIP np.ndarray]
        """
        mip_pet = MIPGenerator(pet_array, None, None, None)._project(angle)
        mip_mask = MIPGenerator(mask_array, None, None, None)._project(angle)
        mip_mask = MIPGenerator.transform_to_nan(mip_mask)
        if not np.isnan(mip_mask).all():
            mip_pet = np.where(np.isnan(mip_mask), mip_pet, mip_mask)
        return mip_pet

    @classmethod
    def create_gif_two_modality(cls, pet_array:np.ndarray, mask_array:np.ndarray, output):
        """function to generate a gif MIP of PET/MASK and save it as .gif

        Args:
            pet_array (np.ndarray): [3D np.ndarray of shape (z,y,x)]
            mask_array (np.ndarray): [3D np.ndarray of shape (z,y,x)]
            output : [Where to save the gif]

        """
        duration = 0.1
        number_images = 60
        angle_filenames = []
        angles = np.linspace(0, 360, number_images)
        """
        nbCores = cpu_count() - 2
        pool = Pool(nbCores)
        projections = pool.map(cls.save_projection_two_modality, pet_array, mask_array, angles)
        """
        projections = []
        for angle in angles:
            projections.append(cls.save_projection_two_modality(pet_array, mask_array, angle))
        imageio.mimwrite(output, projections, format='.gif', duration=duration)

class MIPGeneratorMultiThread(MIPGeneratorSingleThread):
    """a class to generate MIP"""

    def __init__(self, numpy_array: np.ndarray, frames: int, delay :float, projection :int) -> None:
        """constructor

        Args:
            numpy_array (np.ndarray): [3D np.ndarray of shape (z,y,x) or 4D np.ndarray of shape (z,y,x,c)]
        """
        super().__init__(numpy_array, frames, delay, projection)

    def _create_projection_list(self) -> list:
        """Function to create a list of 2D MIP

        Returns:
            list: [list of 2D MIP]
        """
        angles = np.linspace(0, self.projection, self.frames)
        nbCores = cpu_count() - 2
        pool = Pool(nbCores)
        projection_list = pool.map(self._project, angles)
        return projection_list

    @classmethod
    def create_gif_two_modality(cls, pet_array:np.ndarray, mask_array:np.ndarray, output):
        """function to generate a gif MIP of PET/MASK and save it as .gif

        Args:
            pet_array (np.ndarray): [3D np.ndarray of shape (z,y,x)]
            mask_array (np.ndarray): [3D np.ndarray of shape (z,y,x)]
            output : [Where to save the gif]

        """
        duration = 0.1
        number_images = 60
        angle_filenames = []
        angles = np.linspace(0, 360, number_images)
        nbCores = cpu_count() - 2
        pool = Pool(nbCores)
        projections = pool.map(cls.save_projection_two_modality, pet_array, mask_array, angles)
        imageio.mimwrite(output, projections, format='.gif', duration=duration)

        
    

if __name__ == '__main__':
    import SimpleITK as sitk
    img_dir = '/Users/theophilushomawoo/Documents/stage/galeo/python/dicom_cnn/tests/dicom_samples/mip_nifti_example.nii'
    image = sitk.ReadImage(img_dir)
    numpy_array = sitk.GetArrayFromImage(image)
    MIPGeneratorSingleThread(numpy_array, 60, 100, 360).create_gif('test.gif')
    #MIPGenerator.create_gif_two_modality(numpy_array, numpy_array, 'test2.gif')
