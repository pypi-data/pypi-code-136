import matplotlib.pyplot as plt
import logging
log = logging.getLogger('HitDrawer')

class HitDrawer():

  def __init__(self):
    fig = plt.figure()
    self.ax = fig.add_subplot(projection='3d')
    self.ax.set_xlabel("x (m)")
    self.ax.set_ylabel("y (m)")
    self.ax.set_zlabel("z (m)")

  def AddVertices(self, ievents):
    pass

  def AddPhotons(self, photons, suppression_factor=1):
    pos = photons.r[0,::suppression_factor,:].T  # step 0, every Nth phton
    self.ax.scatter(pos[0], pos[1], pos[2], marker='.')
   
  def AddHits(self, hits):
    #
    time = []             # in ns
    weight = []           # = probability
    x, y, z = [], [], []  # in meters
    for om_key, om_hits in hits.items():
      for hit in om_hits:
        time.append(hit[0])
        weight.append(hit[1]*hit[2]*hit[3]*hit[4])
        x.append(hit[5])
        y.append(hit[6])
        z.append(hit[7])
    #
    self.ax.scatter(x, y, z, weight)

  def Show(self):
    plt.show()
