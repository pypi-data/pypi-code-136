import sys
import SimpleITK as sitk
import numpy as np

class SimpleITKRunner:
    def __init__(self,numDOF=7, normalizeToMaxValues=False):
        self.numDOF = numDOF   
        self.normalizeToMaxValues = normalizeToMaxValues

    def performRegistration(self, fixed_data, moving_data, numIterations=200):
        print("Beginning itk registration")
        if(self.normalizeToMaxValues):
            fixed_data = fixed_data / np.max(fixed_data)
            moving_data = moving_data / np.max(moving_data)
            
        fixed_image = sitk.GetImageFromArray(fixed_data)
        moving_image = sitk.GetImageFromArray(moving_data)
        
        if(self.numDOF == 6):
             initial_transform = sitk.CenteredTransformInitializer(fixed_image, moving_image, sitk.Euler3DTransform(), sitk.CenteredTransformInitializerFilter.GEOMETRY)
        if(self.numDOF == 7):
            initial_transform = sitk.CenteredTransformInitializer(fixed_image, moving_image, sitk.Similarity3DTransform(), sitk.CenteredTransformInitializerFilter.GEOMETRY)
        if(self.numDOF == 12):
            initial_transform = sitk.CenteredTransformInitializer(fixed_image, moving_image, sitk.AffineTransform(), sitk.CenteredTransformInitializerFilter.GEOMETRY)

        registration_method = sitk.ImageRegistrationMethod()
        registration_method.SetMetricAsCorrelation()
        registration_method.SetOptimizerAsGradientDescentLineSearch(learningRate=0.05,numberOfIterations=numIterations,convergenceMinimumValue=1e-5,convergenceWindowSize=5)
        registration_method.SetInitialTransform(initial_transform, inPlace=False)
        registration_method.SetInterpolator(sitk.sitkLinear)
        final_transform = registration_method.Execute(fixed_image, moving_image)

        print('Final metric value: {0}'.format(registration_method.GetMetricValue()))
        print('Optimizer\'s stopping condition, {0}'.format(registration_method.GetOptimizerStopConditionDescription()))
        print('Final Transform Parameters: ' + str(final_transform.GetNthTransform(0).GetParameters()))

        moving_resampled = sitk.Resample(moving_image, fixed_image, final_transform, sitk.sitkNearestNeighbor, 0.0, moving_image.GetPixelID())
        moving_resampled_data = sitk.GetArrayFromImage(moving_resampled)
        print("Finished itk registration")
        return moving_resampled_data



