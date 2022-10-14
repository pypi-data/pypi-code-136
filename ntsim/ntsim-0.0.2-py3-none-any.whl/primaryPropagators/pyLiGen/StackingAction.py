from geant4_pybind import *
import numpy as np

class StackingAction(G4UserStackingAction):

  def __init__(self, data_buffer=None):
    super().__init__()
    self.data_buffer = data_buffer
    self.ph_counter = 0
    self.ph_suppression_factor = 10

  def SetPhotonSuppressionFactor(self, f):
    self.ph_suppression_factor = f

  def ClassifyNewTrack(self, track):
    # By some reason tracks are stacked even in the middle of their life,
    # so this method is invoked not only on particle creation
    #
    uid = track.GetTrackID()
    parent_id = track.GetParentID()
    position = track.GetPosition()
    time = track.GetGlobalTime()
    pdg_id = track.GetDefinition().GetPDGEncoding()
    momentum = track.GetMomentum()
    Etot = track.GetTotalEnergy()
    Ekin = track.GetKineticEnergy()
    if uid == 1 and track.GetCurrentStepNumber() == 0: # only initial event vertex
      self.data_buffer.AddVertex( [ [position.x/m, position.y/m, position.z/m, time],
                                    [], 
                                    [[pdg_id, momentum.x/GeV, momentum.y/GeV, momentum.z/GeV, Etot/GeV]] ] )
    #
    # TODO: do it in stepping action via the list of secondaries
    #
    if track.GetDefinition() == G4OpticalPhoton.OpticalPhoton():
      if self.ph_counter%self.ph_suppression_factor == 0:
        position = track.GetPosition()
        direction = track.GetMomentumDirection()
        time = track.GetGlobalTime()
        wavelength = 1239.84193/(Etot/eV)*nm # in nm
        ph = np.array([position.x/m, position.y/m, position.z/m,
                       time/ns,
                       direction.x, direction.y, direction.z,
                       wavelength/nm])
        self.data_buffer.AddPhoton(ph)
      self.ph_counter += 1
      # kill optical photons
      return G4ClassificationOfNewTrack.fKill
    # kill particles below Cherenkov threshold
    elif track.GetDefinition() in [G4Electron.Electron(), G4Positron.Positron()]:
      if Ekin < 260*keV:
        return G4ClassificationOfNewTrack.fKill
    elif track.GetDefinition() in [G4MuonMinus.MuonMinus(), G4MuonPlus.MuonPlus()]:
      if Ekin < 54*MeV:
        return G4ClassificationOfNewTrack.fKill
    #
    if track.GetCurrentStepNumber() == 0:  # FIXME: by some reason ClasifyNewTrack is called on every step...
      self.data_buffer.CreateTrack(uid, parent_id, pdg_id)
      self.data_buffer.tracks[uid].AddPoint([position.x/m, position.y/m, position.z/m, time/ns, 
                                             momentum.x/GeV, momentum.y/GeV, momentum.z/GeV, Etot/GeV])
    # 
    return G4ClassificationOfNewTrack.fUrgent
