from geant4_pybind import *

class SteppingAction(G4UserSteppingAction):

  def __init__(self, data_buffer=None):
    super().__init__()
    self.data_buffer = data_buffer

  def UserSteppingAction(self, aStep):
    aTrack = aStep.GetTrack()
#    pdgid = aTrack.GetDefinition().GetPDGEncoding()
    uid = aTrack.GetTrackID()
    post_step_point = aStep.GetPostStepPoint()
    position = post_step_point.GetPosition()/m
    time = post_step_point.GetGlobalTime()/ns
    momentum = post_step_point.GetMomentum()/GeV
    Etot = post_step_point.GetTotalEnergy()/GeV
    Ekin = post_step_point.GetKineticEnergy()/GeV
    # Save every track point for particles above Cherenkov threshold
    #   for e+/e- 260 keV
    if Ekin > 0.26e-3:
      self.data_buffer.tracks[uid].AddPoint([position.x, position.y, position.z, time, 
                                             momentum.x, momentum.y, momentum.z, Etot] )
