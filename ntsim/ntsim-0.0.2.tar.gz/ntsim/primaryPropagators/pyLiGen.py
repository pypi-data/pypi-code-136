from geant4_pybind import *
from ntsim.primaryPropagators.pyLiGen.DetectorConstruction import DetectorConstruction
from ntsim.primaryPropagators.pyLiGen.CustomPhysicsList import CustomPhysicsList
from ntsim.primaryPropagators.pyLiGen.PrimaryGeneratorAction import PrimaryGeneratorAction
from ntsim.primaryPropagators.pyLiGen.RunAction import RunAction
from ntsim.primaryPropagators.pyLiGen.SteppingAction import SteppingAction
from ntsim.primaryPropagators.pyLiGen.StackingAction import StackingAction
from ntsim.primaryPropagators.pyLiGen.EventAction import EventAction
from ntsim.primaryPropagators.pyLiGen.DataBuffer import DataBuffer
from ntsim.photonTransporters.mcPhotonTransport.Photon import Photon

import time as system_time
import numpy as np

import configargparse
p = configargparse.get_argument_parser()
p.add_argument("--g4particle_type", default='mu-', help="particle type")
p.add_argument("--g4particle_energy_GeV", type=float, default=10, help="particle energy (GeV)")
p.add_argument("--g4particle_position_m", nargs='+', default=[0,0,0], type=float,help="three vector for particle position (meters)")
p.add_argument("--g4particle_direction", nargs='+', default=[0,0,1], type=float,help="three vector for particle direction")
p.add_argument("--g4particle_photon_fraction", type=float, default=1.0, help="fraction of photons to generate")
p.add_argument("--g4particle_macro", default="", help="input macro file")

import logging
log = logging.getLogger('pyLiGenPropagator')

class ActionInitialization(G4VUserActionInitialization):

    def __init__(self, data_buffers):
        self.data_buffers = data_buffers
        super().__init__()

    def BuildForMaster(self):
        # create RunAction instance at the master processing unit
        runAction = RunAction(True)
        runAction.SetPrintTiming(True)
        self.SetUserAction(runAction)

    def Build(self):
        thread_data_buffer = DataBuffer()
        self.data_buffers.append(thread_data_buffer)
        # create instances at each processing unit
        self.SetUserAction(PrimaryGeneratorAction())
        self.SetUserAction(RunAction(False))
        self.SetUserAction(EventAction(data_buffer=thread_data_buffer))
        self.stackingAction = StackingAction(data_buffer=thread_data_buffer)
        self.stackingAction.SetPhotonSuppressionFactor(1)
        self.SetUserAction(self.stackingAction)
        self.SetUserAction(SteppingAction(data_buffer=thread_data_buffer))


class pyLiGen:
    def __init__(self, name):
        log.info("Initializing Geant4/pyLiGen")
        self.data_buffers = []
        self.photons = Photon() # array of photons
        self.runManager = G4RunManagerFactory.CreateRunManager(G4RunManagerType.Default)
        self.detConstruction = DetectorConstruction()
        self.physList = CustomPhysicsList()
        self.actInit = ActionInitialization(self.data_buffers)
        self.ph_fraction = 1.


    def configure(self, opts):
        self.runManager.SetUserInitialization(self.detConstruction)
        self.runManager.SetUserInitialization(self.physList)
        self.runManager.SetUserInitialization(self.actInit)
        #
        UImanager = G4UImanager.GetUIpointer()

        if True:  #TMP
            self.ptype = opts.g4particle_type
            self.energy = opts.g4particle_energy_GeV
            self.pos = opts.g4particle_position_m
            self.dir = opts.g4particle_direction
            self.ph_fraction = opts.g4particle_photon_fraction
        self.actInit.stackingAction.SetPhotonSuppressionFactor(1./self.ph_fraction)

        if opts.g4particle_macro == "":
            cmd_list  = ["/control/verbose 0",
                         "/run/verbose 0",
                         "/vis/verbose 0",
                         "/tracking/verbose 0",
                         "/process/optical/processActivation Cerenkov True",
                         "/process/optical/processActivation OpAbsorption True",
                         "/process/optical/processActivation OpRayleigh True",
                         "/process/optical/processActivation OpMieHG False",
                         "/process/optical/processActivation Cerenkov True",
                         "/process/optical/cerenkov/setStackPhotons True",
                         "/process/em/verbose 0",
                         "/run/initialize",
                         f"/gps/particle  {self.ptype}",
                         f"/gps/energy {self.energy} GeV",
                         f"/gps/position {self.pos[0]} {self.pos[1]} {self.pos[2]} m",
                         f"/gps/direction {self.dir[0]} {self.dir[1]} {self.dir[2]}"]
            for cmd in cmd_list:
                UImanager.ApplyCommand(cmd)
        else:
            UImanager.ApplyCommand(f"/control/execute {opts.g4particle_macro}")
        #
#        self.sensDet = detConstruction.GetSensitiveDetector()  # must be after run/initialize
        log.info("configured")


    def propagate(self, inputs=None):
        log.info("Running Geant4/pyLiGen")
        rnd_seed = int(system_time.time_ns())
        G4Random.setTheSeed(rnd_seed)
        log.debug(f"Random seed set to {rnd_seed}")
        self.runManager.BeamOn(1)

        ready_db_nb = sum([db.IsReady() for db in self.data_buffers])
        if ready_db_nb != 1:
            log.warning(f"Number of ready data buffers {ready_db_nb}")
        # search for a filled data buffer:
        data_buffer = None
        for idb, db in enumerate(self.data_buffers):
            if db.IsReady():
                data_buffer = db
                log.info(f"Reading data from data buffer #{idb}")
                break
        #
        vertices = data_buffer.vertices
        tracks = data_buffer.tracks
        #
        if data_buffer.photon_cloud == []:
            photons = Photon()
        else:
            #
            photon_cloud = np.array(data_buffer.photon_cloud)
            #
            n_photons = photon_cloud.shape[0]
            position = photon_cloud[:,0:3]
            time = photon_cloud[:,3]
            direction = photon_cloud[:,4:7]
            wavelength = photon_cloud[:,7]
            position = np.expand_dims(position, axis=0)
            direction = np.expand_dims(direction, axis=0)
            time = np.expand_dims(time, axis=0)
            # TMP: expand to 5 steps3
            #n_steps = 5 # temp, to be removed
            #position = np.concatenate((position, np.zeros((n_steps-1, n_photons, 3))), axis=0)
            #direction = np.concatenate((direction, np.zeros((n_steps-1, n_photons, 3))), axis=0)
            #time = np.concatenate((time, np.zeros((n_steps-1, n_photons))), axis=0)
            #
            photons = Photon()
            n_steps = 1
            photons.init(n_photons, n_steps, position, time, direction, wavelength)
        data_buffer.Clear()
        return vertices, photons, tracks
