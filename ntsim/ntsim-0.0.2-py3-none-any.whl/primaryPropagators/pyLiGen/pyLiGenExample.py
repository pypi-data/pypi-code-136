from geant4_pybind import *
import sys

from DetectorConstruction import DetectorConstruction
from PrimaryGeneratorAction import PrimaryGeneratorAction
from RunAction import RunAction
from EventAction import EventAction
from StackingAction import StackingAction
from SteppingAction import SteppingAction
from CustomPhysicsList import CustomPhysicsList
from DataBuffer import DataBuffer

class ActionInitialization(G4VUserActionInitialization):

    def __init__(self, data_buffers):
        super().__init__()
        self.data_buffers = data_buffers

    def BuildForMaster(self):
        self.SetUserAction(RunAction(True))

    def Build(self):
        thread_data_buffer = DataBuffer()
        self.data_buffers.append(thread_data_buffer)
        self.SetUserAction(PrimaryGeneratorAction())
        self.SetUserAction(RunAction(False))
        self.SetUserAction(EventAction(data_buffer=thread_data_buffer))
        self.SetUserAction(StackingAction(data_buffer=thread_data_buffer))
        self.SetUserAction(SteppingAction(data_buffer=thread_data_buffer))


# Detect interactive mode (if no arguments) and define UI session
ui = None
if len(sys.argv) == 1:
    ui = G4UIExecutive(len(sys.argv), sys.argv)

# Construct the default run manager
runManager = G4RunManagerFactory.CreateRunManager(G4RunManagerType.Serial)
#runManager = G4RunManagerFactory.CreateRunManager(G4RunManagerType.MT, 4)

# Set mandatory initialization classes
runManager.SetUserInitialization(DetectorConstruction())

#runManager.SetUserInitialization(FTFP_BERT())
runManager.SetUserInitialization(CustomPhysicsList())

# Data buffers
data_buffers = []

# Set user action classes
runManager.SetUserInitialization(ActionInitialization(data_buffers))

# Initialize visualization
visManager = G4VisExecutive()
# G4VisExecutive can take a verbosity argument - see /vis/verbose guidance.
# visManager = G4VisExecutive("Quiet");
visManager.Initialize()

# Get the pointer to the User Interface manager
UImanager = G4UImanager.GetUIpointer()

# Process macro or start UI session
if ui == None:
    # batch mode
    command = "/control/execute "
    fileName = sys.argv[1]
    UImanager.ApplyCommand(command+fileName)
else:
    # interactive mode
    UImanager.ApplyCommand("/control/execute init_vis.mac")
    ui.SessionStart()
