from datetime import datetime
from time import sleep

import pytz
from pyqalx import Bot, Set, Group
from pyqalx.bot import QalxJob

from qalx_orcaflex.bots.batch.summaries import ResultsSummariser
from qalx_orcaflex.data_models import BatchOptions, rehydrate_dataclass


def process_batch(job: QalxJob):
    """main batch processing function

    This will pull a batch off the queue and submit the sims if they haven't been submitted yet.
    """
    job.entity["meta"]["state"] = "processing"
    job.save_entity()
    options = rehydrate_dataclass(BatchOptions, job.entity["meta"]["options"])
    tasks = job.entity["sets"]
    if not job.entity["meta"].get(
        "sims_submitted"
    ):  # if the sims haven't been submitted yet
        sim_queue = job.session.queue.get_or_create(options.sim_queue)  # get the queue
        if job.entity.meta.get("restart_chains"):
            restart_chains = job.entity.meta.get("restart_chains")
            all_chains = [i for s in restart_chains for i in s]

            # there may be tasks that can be added to the queue that are not part of a chain
            non_chain_tasks = {k: v for k, v in tasks.items() if v not in all_chains}
            sets_to_sim_queue(job, options, sim_queue, non_chain_tasks)

            # for everything else we need to send a group to the queue
            for restart_chain in restart_chains:
                chained_tasks = {k: v for k, v in tasks.items() if v in restart_chain}
                add_sets_to_group_and_queue(
                    job, options, sim_queue, chained_tasks, restart_chain
                )
        else:
            sets_to_sim_queue(job, options, sim_queue, tasks)

        if options.notifications and options.notifications.notify_submitted:
            # Send submitted notification if specified
            options.notifications.notify_submitted.send(
                entity=job.entity, session=job.session
            )
        job.entity["meta"][
            "sims_submitted"
        ] = True  # set the flag so next time around we don't resubmit them
        job.save_entity()

    job.log.debug(f"batch {job.e['guid']} loaded.")


def sets_to_sim_queue(job, options, sim_queue, tasks):
    """adds all the sets in the tasks dict to the queue"""
    for t, s in tasks.items():
        add_set_to_queue(
            job=job, options=options, sim_queue=sim_queue, task=t, set_data=s
        )


def add_set_to_queue(job, options, sim_queue, task, set_data):
    set_data = get_full_set(job, set_data, task)
    Set.add_to_queue(payload=set_data, queue=sim_queue)
    set_data["meta"]["state"]["state"] = "Queued"
    set_data["meta"]["state"]["info"] = options.sim_queue
    job.session.set.save(set_data)
    job.log.debug(f"added {set_data['guid']} to {options.sim_queue}.")


def get_full_set(job, set_data, task):
    if not isinstance(set_data, Set):
        set_data = job.session.set.get(set_data)
        job.entity["sets"][task] = set_data
    return set_data


def add_sets_to_group_and_queue(job, options, sim_queue, chained_tasks, restart_chain):
    """adds all the sets in chained_tasks to a group and puts the group on the queue"""
    group_data = {}
    for task, set_data in chained_tasks.items():
        set_data = get_full_set(job, set_data, task)
        set_data["meta"]["state"]["state"] = "Queued"
        set_data["meta"]["state"]["info"] = options.sim_queue
        job.session.set.save(set_data)
        group_data[task] = set_data
        job.log.debug(f"added {set_data['guid']} to a task group for restarts.")

    group = job.session.group.add(
        sets=group_data,
        meta={"_class": "orcaflex.batch.restart_chain", "chain": restart_chain},
    )
    Group.add_to_queue(payload=group, queue=sim_queue)


def send_batch_to(job: QalxJob, options: BatchOptions):
    """will send the entity on the job to all the queues defined in
    options.send_batch_to

    :param job:
    :param options:
    :return: None
    """
    if options.send_batch_to:
        for q_name in options.send_batch_to:
            queue = job.session.queue.get_or_create(q_name)
            job.entity.__class__.add_to_queue(payload=job.entity, queue=queue)


def handle_notifications(job: QalxJob, options: BatchOptions, state: str):
    if options.notifications and getattr(options.notifications, f"notify_{state}"):
        # Send completed notification if specified
        getattr(options.notifications, f"notify_{state}").send(
            entity=job.entity, session=job.session
        )


def post_process_batch(job: QalxJob):
    # Reload the entity without unpacking to ensure it's on the correct state
    job.reload_entity()
    # Reload again, but this time unpack everything.  We use the results from the unpacked
    # sets to check to see if all the jobs have been processed by SimBots (or children)
    reloaded_entity = job.session.group.reload(
        job.entity, unpack=True, fields=["sets", "meta"]
    )
    options = rehydrate_dataclass(BatchOptions, job.entity["meta"]["options"])
    tasks = reloaded_entity["sets"]
    process_sets = [task["meta"].get("processing_complete") for task in tasks.values()]
    job.log.debug(process_sets)

    if all(process_sets):
        if options.summarise_results and (
            not job.entity["meta"].get("results_summary")
        ):
            job.entity["meta"]["state"] = "post-processing"
            job.save_entity()
            job.log.debug(f"batch {job.e['guid']} about to be summarised.")
            res_sum = ResultsSummariser(job)
            res_sum.summarise_batch(tasks)
            job.log.debug(f"batch {job.e['guid']} summary complete.")
        job.entity["meta"]["state"] = "processing_complete"
        job.save_entity()
        send_batch_to(job, options)
        handle_notifications(job, options, "completed")
    else:
        utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
        has_timed_out = (
            options.timeout
            and (utc_now - job.entity["info"]["created"]["on"]).seconds
            > options.timeout
        )
        if has_timed_out:
            # The batch has timed out.  Send a notification if specified but do not add
            # the batch back onto the queue to continue processing
            handle_notifications(job, options, "timed_out")
        else:
            sleep(options.wait_between_completion_checks)
            batch_queue = job.session.queue.get_or_create(options.batch_queue)
            Group.add_to_queue(payload=job.entity, queue=batch_queue)
            job.log.debug(f"put batch {job.e['guid']} back on {options.batch_queue}.")


class BatchBot(Bot):
    """batch processing bot

    Will start by submit jobs to the sim worker queue if they haven't been already.

    If `data_models.BatchOptions.summarise_results` is set to True then it will check
    if all the sims are complete. If they are not it puts the job back on the
    queue. If they are complete then it calls the summarise results functions.
    """

    def __init__(self, bot_name):
        super(BatchBot, self).__init__(bot_name)

        self.process_function = process_batch
        self.postprocess_function = post_process_batch
