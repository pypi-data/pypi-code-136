import os
import logging
import eons
import threading
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT
from threading import Thread
import jsonpickle

######## START CONTENT ########

# For validating args
class ArgumentNotProvided(Exception, metaclass=eons.ActualType): pass

# For initialization
class InitializationError(Exception, metaclass=eons.ActualType): pass

# All Device errors
class DevicesError(Exception, metaclass=eons.ActualType): pass

# Exception used for miscellaneous Device errors.
class OtherBuildError(DevicesError, metaclass=eons.ActualType): pass

# All Routine errors
class RoutineError(Exception, metaclass=eons.ActualType): pass

# Exception used for miscellaneous Routine errors.
class OtherRoutineError(RoutineError, metaclass=eons.ActualType): pass


class HWBase(eons.StandardFunctor):
    def __init__(this, name=eons.INVALID_NAME(), state=None):
        super().__init__(name)

        # See State.py
        this.state = state

        # For optional args, supply the arg name as well as a default value.
        this.optionalKWArgs['shouldRunInThread'] = True

        this.fetchFrom = [
            'this',
            'args',
            'precursor',
            'state'
            'environment',
        ]

    # Set the state of this.
    def UseState(this, state):
        this.state = state

    # Do stuff!
    # Override this or die.
    def Run(this):
        pass

    # Hook for any pre-run configuration.
    # RETURN whether or not to continue running.
    def InitializeHardware(this):
        return True

    # Hook for any post-run configuration.
    # RETURN whether or not Cleanup was successful.
    def Cleanup(this):
        return True

    def ParseInitialArgs(this):
        super().ParseInitialArgs()
        this.UseState(this.executor.state)

    # Override of eons.Functor method. See that class for details
    def Function(this):        

        if (not this.InitializeHardware()):
            errStr = f"Failed to initialize {this.name}"
            raise InitializationError(errStr)

        if (this.shouldRunInThread):
            thread = Thread(target=this.Run).start()
            thread.join()
        else:
            this.Run()

        if (not this.Cleanup()):
            logging.error(f"Failed to clean up {this.name}")


    def fetch_location_state(this, varName, default, fetchFrom):
        if (not this.state.Has(varName)):
            return default, False
        stateVar = this.state.Get(varName)
        if (stateVar is not None):
            logging.debug(f"...{this.name} got {varName} from state")
            return stateVar, True
        return default, False


class Routine(HWBase):
    def __init__(this, name=eons.INVALID_NAME()):
        super().__init__(name)

    # Do stuff!
    # Override this or die.
    def Run(this):
        pass

    # Hook for any pre-run configuration.
    # RETURN whether or not to continue running.
    def InitializeHardware(this):
        return True

    # Hook for any post-run configuration.
    # RETURN whether or not Cleanup was successful.
    def Cleanup(this):
        return True



#State is essentially just a set of global variables which will be accessible through an EHW instance.
class State:
    def __init__(this):
        this.lock = threading.Lock()

    def Has(this, name):
        ret = False
        with this.lock:
            ret = hasattr(this,name)
        return ret

    def Set(this, name, value):
        with this.lock:
            setattr(this, name, value)

    def Get(this, name):
        ret = False
        with this.lock:
            ret = getattr(name)
        return ret

class EHW(eons.Executor):

    def __init__(this):
        super().__init__(name="eons hardware", descriptionStr="Modular framework for controlling hardware devices.")

        this.defaultPrefix = "hw"

        this.state = State()

        this.requiredKWArgs.append('routines')

    #Override of eons.Executor method. See that class for details
    def Function(this):
        super().Function()
        for r in this.routines:
            this.StartRoutine(r)

    #Run some Routine.
    def StartRoutine(this, routine, *args, **kwargs):
        return this.Execute(routine, *args, **kwargs)

