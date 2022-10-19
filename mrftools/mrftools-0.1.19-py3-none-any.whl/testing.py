from mrftools import *
import numpy as np
import pathlib

class Testing:
    @staticmethod
    def GenerateTestData():
        # Create a sequence parameter set programmatically
        TR = 0.01; TE = 0.005; FA_Range = [0, 20]; FA_First = 10; numTimepoints = 500; wavelength = 20; seed = 1234
        seqParam = SequenceParameters("testSeq",SequenceType.FISP)
        seqParam.Initialize(TRs=np.ones(numTimepoints)*TR, TEs=np.ones(numTimepoints)*TE, FAs=Perlin.Generate(numTimepoints, min=FA_Range[0], max=FA_Range[1], firstValue=FA_First, wavelength=wavelength, seed=seed))

        # Create a dictionary parameter set programmatically
        dictParam = DictionaryParameters.GenerateFixedPercent("testDict", percentStepSize=20, includeB1=False)

        # Perform a simulation using the generated parameter sets
        testSim = Simulation(seqParam, dictParam, phaseRange=(-1*np.pi, 1*np.pi), numSpins=8)
        testSim.Execute()

        # Perform SVD on simulation resutls
        testSim.CalculateSVD(25)

        # Export to .mrf file
        pathlib.Path("testdata").mkdir(exist_ok=True) 
        testSim.Export("testdata/test.mrf", force=True)

        # Export to .txt files 
        pathlib.Path("testdata/txt").mkdir(exist_ok=True) 
        testSim.sequenceParameters.ExportToTxt("testdata/txt/")
        testSim.dictionaryParameters.ExportToTxt("testdata/txt/")

