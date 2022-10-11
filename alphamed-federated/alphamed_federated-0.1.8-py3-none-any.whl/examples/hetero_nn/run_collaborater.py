import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHONPATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir, os.pardir)
sys.path.insert(0, PYTHONPATH)

if True:
    from alphafed import logger
    from alphafed.examples.hetero_nn import COLLABORATER_3_ID
    from alphafed.examples.hetero_nn.demos import get_task_id, get_collaborator


task_id = get_task_id()
collaborator = get_collaborator()
logger.debug(f'{type(collaborator)=}')
collaborator._setup_context(id=COLLABORATER_3_ID, task_id=task_id, is_initiator=True)
collaborator.data_channel._ports = [i for i in range(21000, 21010)]
logger.info(f'run collaborator on task_id = {task_id}')
collaborator._launch_process()
