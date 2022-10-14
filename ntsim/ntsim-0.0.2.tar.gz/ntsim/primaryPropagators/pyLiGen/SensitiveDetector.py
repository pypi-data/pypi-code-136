from geant4_pybind import *
#import ROOT
#ROOT.gSystem.Load("librootIO.so")
#from ROOT import iEvent

class SensitiveDetector(G4VSensitiveDetector):

  def __init__(self, name):
    super().__init__(name)
    self.process_dict = {}


  def Initialize(self, hc):
    pass


  def ProcessHits(self, aStep, rohistory):
    aTrack = aStep.GetTrack()
    particle_def = aTrack.GetDefinition()
    pname = particle_def.GetParticleName()
    if pname == "opticalphoton":
      print("photon")
    ene = aTrack.GetTotalEnergy()
    sp1 = aStep.GetPreStepPoint()
    sp2 = aStep.GetPostStepPoint()
    process = sp2.GetProcessDefinedStep()
    if process:
      process_name = process.GetProcessName()
    else:
      process_name = None
    if process_name not in self.process_dict.keys():
      self.process_dict[process_name] = 1
    else:
      self.process_dict[process_name] += 1
    return True


  def EndOfEvent(self, hc):
    #print(self.process_dict)
    pass


  def Print(self):
    self.process_dict
