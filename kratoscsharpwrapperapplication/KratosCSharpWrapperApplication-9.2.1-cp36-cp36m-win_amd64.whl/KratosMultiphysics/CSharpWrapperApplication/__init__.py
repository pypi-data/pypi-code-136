from KratosMultiphysics import _ImportApplication
import KratosMultiphysics.StructuralMechanicsApplication
from KratosCSharpWrapperApplication import *
application = KratosCSharpWrapperApplication()
application_name = "KratosCSharpWrapperApplication"

_ImportApplication(application, application_name)
