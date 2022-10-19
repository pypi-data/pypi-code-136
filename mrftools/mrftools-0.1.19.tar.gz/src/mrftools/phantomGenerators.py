from enum import Enum
import numpy as np

class PhantomType(Enum):
    SHEPP_LOGAN = 0
    MODIFIED_SHEPP_LOGAN = 1

##############################################################
# Gach, H.; Tanase, C.; Boada, F.; 2D & 3D Shepp-Logan Phantom Standards for MRI
# 19th International Conference on Systems Engineering, p. 521.
##############################################################
TissueType = np.dtype([('T1_A', np.float32), ('T1_C', np.float32), ('T1', np.float32), ('T2', np.float32), ('PD', np.float32)])
class TissueTypes(Enum):
    SCALP = np.array([(0.324, 0.137, None, 0.070, 0.800)],dtype=TissueType)
    BONE_AND_MARROW = np.array([(0.533, 0.888, None,  0.050, 0.120)],dtype=TissueType)
    CSF = np.array([(4.20, 0.000, None, 1.99, 0.980)],dtype=TissueType)
    BLOOD_CLOT = np.array([(1.350, 0.340, None,  0.200, 0.850)],dtype=TissueType)
    GRAY_MATTER = np.array([(0.857, 0.376, None, 0.100, 0.745)],dtype=TissueType)
    WHITE_MATTER = np.array([(0.583, 0.382, None, 0.080, 0.617)],dtype=TissueType)
    TUMOR = np.array([(0.926, 0.217, None, 0.100, 0.950)],dtype=TissueType)
    
# phi : Counterclockwise rotation of the ellipse in degrees, as the angle between the x axis and the ellipse's major axis.
class TraditionalEllipse():
    def __init__(self, additiveIntensity, majorAxisLength, minorAxisLength, centerX, centerY, phi):
        self.additiveIntensity = additiveIntensity
        self.majorAxisLength  = majorAxisLength
        self.minorAxisLength = minorAxisLength
        self.centerX = centerX
        self.centerY = centerY
        self.phi = phi
        
    def addTo(self, targetMatrix):
        matrixSize = np.shape(targetMatrix)[0]
        ygrid, xgrid = np.mgrid[-1:1:(1j*matrixSize), -1:1:(1j*matrixSize)] # Create the pixel grid
        x = xgrid - self.centerX
        y = ygrid - self.centerY # Create the offset x and y values for the grid
        phiRads = self.phi * np.pi / 180  # Rotation angle in radians
        sin_p = np.sin (phiRads)
        cos_p = np.cos (phiRads) 
        locs = (((x * cos_p + y * sin_p)**2) / self.majorAxisLength**2 
                + ((y * cos_p - x * sin_p)**2) / self.minorAxisLength**2 ) <= 1 # Find the pixels within the ellipse
        targetMatrix[locs] += self.additiveIntensity # Add the ellipse intensity to those pixels
        return targetMatrix

# phi : Counterclockwise rotation of the ellipse in degrees, as the angle between the x axis and the ellipse's major axis.
class RelaxationEllipse():
    def __init__(self, tissue:TissueTypes, majorAxisLength, minorAxisLength, centerX, centerY, phi):
        self.tissue = tissue.value
        self.majorAxisLength  = majorAxisLength
        self.minorAxisLength = minorAxisLength
        self.centerX = centerX
        self.centerY = centerY
        self.phi = phi
    
    def addTo(self, targetMatrix, fieldStrengthTesla):
        matrixSize = np.shape(targetMatrix)[0]
        ygrid, xgrid = np.mgrid[-1:1:(1j*matrixSize), -1:1:(1j*matrixSize)] # Create the pixel grid
        x = xgrid - self.centerX; y = ygrid - self.centerY # Create the offset x and y values for the grid
        phiRads = self.phi * np.pi / 180  # Rotation angle in radians
        sin_p = np.sin (phiRads)
        cos_p = np.cos (phiRads) 
        locs = (((x * cos_p + y * sin_p)**2) / self.majorAxisLength**2 
                + ((y * cos_p - x * sin_p)**2) / self.minorAxisLength**2 ) <= 1 # Find the pixels within the ellipse
        self.tissue['T1'] = self.tissue['T1_A']*np.power(fieldStrengthTesla, self.tissue['T1_C']) # Apply field strength to tissue
        targetMatrix[locs] = self.tissue # Overwrite the ellipse tissueType to those pixels
        return targetMatrix

    
##############################################################
# Shepp, L. A.; Logan, B. F.; Reconstructing Interior Head Tissue from X-Ray Transmissions
# IEEE Transactions on Nuclear Science,Feb. 1974, p. 232.
##############################################################
def _traditional_shepp_logan ():
    return [TraditionalEllipse(   2,   .69,   .92,    0,      0,   0),
            TraditionalEllipse(-.98, .6624, .8740,    0, -.0184,   0),
            TraditionalEllipse(-.02, .1100, .3100,  .22,      0, -18),
            TraditionalEllipse(-.02, .1600, .4100, -.22,      0,  18),
            TraditionalEllipse( .01, .2100, .2500,    0,    .35,   0),
            TraditionalEllipse( .01, .0460, .0460,    0,     .1,   0),
            TraditionalEllipse( .02, .0460, .0460,    0,    -.1,   0),
            TraditionalEllipse( .01, .0460, .0230, -.08,  -.605,   0),
            TraditionalEllipse( .01, .0230, .0230,    0,  -.606,   0),
            TraditionalEllipse( .01, .0230, .0460,  .06,  -.605,   0)]

##############################################################
# Toft, P.; "The Radon Transform - Theory and Implementation", 
# Ph.D. thesis, Department of Mathematical Modelling, Technical University of Denmark, June 1996.
##############################################################
def _traditional_modified_shepp_logan ():
    return [TraditionalEllipse(   1,   .69,   .92,    0,      0,   0),
            TraditionalEllipse(-.80, .6624, .8740,    0, -.0184,   0),
            TraditionalEllipse(-.20, .1100, .3100,  .22,      0, -18),
            TraditionalEllipse(-.20, .1600, .4100, -.22,      0,  18),
            TraditionalEllipse( .10, .2100, .2500,    0,    .35,   0),
            TraditionalEllipse( .10, .0460, .0460,    0,     .1,   0),
            TraditionalEllipse( .10, .0460, .0460,    0,    -.1,   0),
            TraditionalEllipse( .10, .0460, .0230, -.08,  -.605,   0),
            TraditionalEllipse( .10, .0230, .0230,    0,  -.606,   0),
            TraditionalEllipse( .10, .0230, .0460,  .06,  -.605,   0)]

##############################################################
# Shepp, L. A.; Logan, B. F.; Reconstructing Interior Head Tissue from X-Ray Transmissions
# IEEE Transactions on Nuclear Science,Feb. 1974, p. 232.
##############################################################
def _relaxation_shepp_logan ():
    return [RelaxationEllipse( TissueTypes.SCALP, 0.72, 0.95, 0, 0, 0),
            RelaxationEllipse( TissueTypes.BONE_AND_MARROW, 0.69, 0.92, 0, 0, 0),
            RelaxationEllipse( TissueTypes.CSF, 0.6624, 0.874, 0, -0.0184, 0),
            RelaxationEllipse( TissueTypes.GRAY_MATTER, 0.6524, 0.864, 0, -0.0184, 0),
            RelaxationEllipse( TissueTypes.CSF, 0.41, 0.16, -0.22, 0, -72),
            RelaxationEllipse( TissueTypes.CSF, 0.32, 0.11, 0.22, 0, 72),
            RelaxationEllipse( TissueTypes.WHITE_MATTER, 0.21, 0.25, 0, 0.35, 0),
            RelaxationEllipse( TissueTypes.TUMOR, 0.046, 0.046, 0, 0.1, 0),
            RelaxationEllipse( TissueTypes.TUMOR, 0.046, 0.023, -0.08, -0.605, 0),
            RelaxationEllipse( TissueTypes.TUMOR, 0.046, 0.023, 0.06, -0.605, -90),
            RelaxationEllipse( TissueTypes.TUMOR, 0.046, 0.046, 0, -0.1, 0),
            RelaxationEllipse( TissueTypes.TUMOR, 0.023, 0.023, 0, -0.605, 0)]

def GenerateTraditionalPhantom (matrixSize = 256, phantomType = PhantomType.SHEPP_LOGAN, ellipses = None):
    if (ellipses is None):
        if phantomType is PhantomType.SHEPP_LOGAN:
            ellipses = _traditional_shepp_logan()
        if phantomType is PhantomType.MODIFIED_SHEPP_LOGAN:
            ellipses = _traditional_modified_shepp_logan()
    p = np.zeros ((matrixSize, matrixSize)) # Blank image
    for ellip in ellipses:
       p = ellip.addTo(p)
    return p

def GenerateRelaxationPhantom (matrixSize = 256, phantomType = PhantomType.SHEPP_LOGAN, ellipses = None, fieldStrengthTesla = 3):
    if (ellipses is None):
        if phantomType is PhantomType.SHEPP_LOGAN:
            ellipses = _relaxation_shepp_logan()
        if phantomType is PhantomType.MODIFIED_SHEPP_LOGAN:
            raise Exception("Modified Shepp Logan not implemented for relaxation phantom")
    p = np.zeros ((matrixSize, matrixSize), dtype=TissueType) # Blank image
    for ellip in ellipses:
       p = ellip.addTo(p, fieldStrengthTesla)
    return p