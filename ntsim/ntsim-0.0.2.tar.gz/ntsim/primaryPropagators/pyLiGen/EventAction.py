from geant4_pybind import *

class EventAction(G4UserEventAction):

  def __init__(self, data_buffer=None):
    super().__init__()
    self.data_buffer = data_buffer


  def BeginOfEventAction(self, evt):
    self.data_buffer.Clear()

  def EndOfEventAction(self, evt):
    self.data_buffer.Close()
    #print(f" Number of tracks: {len(self.data_buffer.tracks)}")
    #print(f" Number of photons: {len(self.data_buffer.photon_cloud)}")
