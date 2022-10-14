class Track():

  def __init__(self, unique_id, parent_id,pdg_id):
    self.unique_id = unique_id
    self.parent_id = parent_id
    self.pdg_id = pdg_id
    self.points = []

  def __str__(self):
    return f"UID: {self.unique_id},  parent_ID: {self.parent_id},  PDGID: {self.pdg_id}\n" + \
           f"points:\n" + \
           f"  {self.points[0]}\n" + \
           f"  ... \n" + \
           f"  {self.points[-1]}\n"

  def __repr__(self):
    return self.__str__()
            

  def AddPoint(self, point):
    self.points.append(point)



class DataBuffer():

  def __init__(self):
    self.vertices = []
    self.tracks = {}
    self.photon_cloud = []
    self.status = 'empty' # 'empty' -> 'in_progress' -> 'ready'

  def AddVertex(self, vertex):
    self.status = 'in_progress'
    self.vertices.append(vertex)

  def AddPhoton(self, photon):
    self.status = 'in_progress'
    self.photon_cloud.append(photon)

  def CreateTrack(self, uid, parent_id, pdg_id):
    self.status = 'in_progress'
    self.tracks[uid] = Track(uid, parent_id, pdg_id)

  def Clear(self):
    self.__init__()

  def Close(self):
    self.status = 'ready'

  def IsEmpty(self):
    return self.status == 'empty'

  def IsReady(self):
    return self.status == 'ready'
