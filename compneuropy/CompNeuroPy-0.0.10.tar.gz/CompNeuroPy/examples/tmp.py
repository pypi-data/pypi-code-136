from ANNarchy import clear
from multiprocessing import Process


def import_create_model():
    clear()
    from CompNeuroPy.examples.create_model import main as create_model

    create_model()


def import_monitor_recordings():
    clear()
    from CompNeuroPy.examples.monitor_recordings import main as monitor_recordings

    monitor_recordings()


def import_run_and_monitor_simulations():
    clear()
    from CompNeuroPy.examples.run_and_monitor_simulations import (
        main as run_and_monitor_simulations,
    )

    run_and_monitor_simulations()


print("#####proc1#####")
proc = Process(target=import_create_model)
proc.start()
proc.join()


print("\n\n#####proc2#####")
clear()
proc = Process(target=import_monitor_recordings)
proc.start()
proc.join()


print("\n\n#####proc3#####")
proc = Process(target=import_run_and_monitor_simulations)
proc.start()
proc.join()
