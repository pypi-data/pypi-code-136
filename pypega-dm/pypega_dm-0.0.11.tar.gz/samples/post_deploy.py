import pyPega
import sys

## Orchestrator initalisation
dt1 = Pega.Candidate("dt1", "https://phosphorus.pegatsdemo.com/prweb", 2)

## Connect
if dt1.set_authentication_method(
    Pega.AUTHENTICATION_METHOD_BASIC, "rob.smart@pega.com", "Rules12345!"
):
    sys.exit(1)
else:
    sys.exit(0)
