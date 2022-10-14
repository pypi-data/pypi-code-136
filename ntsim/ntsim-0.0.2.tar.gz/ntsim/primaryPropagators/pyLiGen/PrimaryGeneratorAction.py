from geant4_pybind import *

class PrimaryGeneratorAction(G4VUserPrimaryGeneratorAction):

  def __init__(self):
    super().__init__()
    nofParticles = 1
    #self.fParticleGun = G4ParticleGun(nofParticles)
    self.fParticleGun = G4GeneralParticleSource()

    # default particle kinematic
    #particleDefinition = G4ParticleTable.GetParticleTable().FindParticle("mu-")
    #self.fParticleGun.SetParticleDefinition(particleDefinition)
    #self.fParticleGun.SetParticleMomentumDirection(G4ThreeVector(0, 0, 1))
    #self.fParticleGun.SetParticlePosition(G4ThreeVector(0, 0, 0))
    #self.fParticleGun.SetParticleEnergy(100*GeV)


  def GeneratePrimaries(self, anEvent):
    # This function is called at the begining of event
    self.fParticleGun.GeneratePrimaryVertex(anEvent)
