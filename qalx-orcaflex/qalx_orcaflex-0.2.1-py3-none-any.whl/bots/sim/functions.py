"""
Sim Bot Functions
~~~~~~~~~~~~~~~~~

This module contains the step functions that are called by SimBot.

`preprocess_orcaflex` simply parses the job options sets up state and warnings items

Almost all the work is done in `process_orcaflex`, the basic steps are:

1. Load the model data - this will only return once it has been able to get a licence or
    has tried multiple times to get one as defined in model.OrcaFlexJobOptions
2. Define progress handlers if required
3. Calculate the estimated size of the simulation and based on available RAM disable
    in-memory logging if required.
4. Attempt statics, use the `static_search`_ method if defined in model tags. If statics
    fails the step function returns
5. Attempt dynamics. If dynamics fails the step function returns.
6. Save the simulation file to qalx if required.
7. Extract results if required
8. Extract load case information if required
9. Extract model views if required
10. If simulation stoped due to instability then report this in the warnings and update the state
11. Put the OrcFxAPI.Model instance into the step result data so a custom post-processing function can play with it


"""

from pyqalx.bot import QalxJob
from pyqalx.core.errors import QalxError

from qalx_orcaflex.bots.sim.tasks import (
    NormalTask,
    RestartFromSim,
    RestartFromChain,
    ChainTask,
    VideoTask,
)
from qalx_orcaflex.core import QalxOrcaFlexError


def initialise_orcaflex_bot(qalx):
    try:
        import OrcFxAPI

        OrcFxAPI.Model(threadCount=1)
    except ImportError:
        raise QalxError("Could not import OrcFxAPI, is it installed?")
    return True


def on_wait_orcaflex(job):
    pass


def begin_orcaflex(job):
    pass


def preprocess_orcaflex(job: QalxJob):
    """Here we inspect the job to determine which kind of OrcaFlex task we need to process."""
    if job.entity.entity_type == "group":
        job_task = ChainTask(job.entity.sets, job.entity.meta.chain, job.session)
    elif job.entity["items"].get("data_file"):
        data_file = job.entity["items"].data_file
        if job.entity.meta.is_restart:
            data_file_meta = data_file.meta
            if data_file_meta.get("restart_parent"):
                job_task = RestartFromSim(entity=job.entity, session=job.session)
            elif data_file_meta.get("chain_file_items"):
                job_task = RestartFromChain(entity=job.entity, session=job.session)
            else:
                raise QalxOrcaFlexError(
                    "Jobs with is_restart=True must define a restart_parent or chain_file_items on the meta"
                )
        else:
            job_task = NormalTask(entity=job.entity, session=job.session)
    elif job.entity["items"].get("sim_file"):
        job_task = VideoTask(entity=job.entity, session=job.session)
    else:
        raise QalxOrcaFlexError(
            "Job structure not recognised. Needs to be a Group or a Set with data_file or sim_file."
        )
    job.context["task"] = job_task


def process_orcaflex(job: QalxJob) -> None:
    task = job.context["task"]
    if isinstance(task, (NormalTask, RestartFromSim, RestartFromChain)):
        task.process()
        job.context["model"] = task.model
    elif isinstance(task, ChainTask):
        task.process()
        job.context["model"] = None


def post_process_orcaflex(job: QalxJob):
    send_to = job.entity["meta"].get("send_to", [])
    if send_to:
        for queue_name in send_to:
            queue = job.session.queue.get_or_create(queue_name)
            job.entity.__class__.add_to_queue(payload=job.entity, queue=queue)
            job.log.debug(f"{job.entity.guid} sent to {queue_name}")
    if job.context.get("model"):
        job.context["model"].Clear()
        del job.context["model"].progressHandlerCallback
        del job.context["model"]
