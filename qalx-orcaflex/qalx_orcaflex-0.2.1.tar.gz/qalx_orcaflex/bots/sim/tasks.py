import platform
import queue
import threading
import time
import traceback
from abc import ABC
from dataclasses import asdict
from io import BytesIO
from pathlib import Path
from queue import Queue
from random import randint
from tempfile import mkdtemp
from typing import Union, Sequence
from uuid import UUID

import OrcFxAPI
import psutil
from OrcFxAPI import Model, DLLError
from appdirs import site_data_dir
from pyqalx import Set, QalxSession, Item

from qalx_orcaflex.core import QalxSmartStaticsError
from qalx_orcaflex.data_models import (
    OrcaFlexJobState,
    OrcaFlexJobOptions,
    JobState,
    OrcaFlexJob,
    TimeHistory,
    RangeGraph,
    ModelInfo,
    ModelView,
)
from qalx_orcaflex.helpers import (
    load_model_data,
    get_tags,
    ModelWithLicence,
    model_simulation_size,
    nice_time,
    result_name,
    result_details,
    correct_parent,
)

from qalx_orcaflex.helpers.restarts import data_hash
from qalx_orcaflex.helpers.smart_statics import solved_model
from qalx_orcaflex.video.extract import video_extractor


class Task:
    entity: Set
    options: OrcaFlexJobOptions
    warnings: Item
    session: QalxSession
    orcaflex_job: OrcaFlexJob
    model: OrcFxAPI.Model

    def __init__(self, entity: Union[Set, UUID], session: QalxSession):
        """base class for a SimBot task

        :param entity: either a Set or a UUID of a Set
        :param session: a QalxSession
        """
        if isinstance(entity, Set):
            self.entity = entity
        elif isinstance(entity, UUID):
            self.entity = session.set.get(entity)
        self.session = session
        _options = self.entity.get_item_data("job_options")
        if _options:
            self.options = OrcaFlexJobOptions(**_options)
        else:
            self.options = OrcaFlexJobOptions()
        self.entity["meta"]["bot_host"] = {
            "node": platform.node(),
            "platform": platform.platform(),
        }
        self.warnings = self.add_item_data(
            "warnings", data={"warning_text": []}, meta={"_class": "orcaflex.warnings"}
        )
        self.save_entity()

        self.orcaflex_job = OrcaFlexJob(
            **self.entity["items"]
        )  # unpack the raw Set into our pre-defined model

    def save_entity(self):
        self.session.set.save(self.entity)

    def add_item_data(self, item_name, data, meta):
        """adds an item to the set and saves the set

        :param item_name: key of the item
        :param data:  item data
        :param meta: item meta
        :return:
        """
        item = self.session.item.add(data=data, meta=meta)
        self.entity["items"][item_name] = item
        self.save_entity()
        return item

    def update_task_state(self, new_state: JobState, info=None, error=None) -> None:
        """
        update the state of the task.

        :param new_state: a JobState representing the new state
        :param info: any additional info
        :param error: any error message if the new state is JobState.ERROR
        :return: None
        """
        self.entity["meta"]["state"] = OrcaFlexJobState(
            state=new_state.value, info=info, error=error
        ).__dict__
        self.save_entity()

    def update_task_warnings(self, warnings: Sequence[str]) -> None:
        """
        adds any warning text to the warnings item

        :param warnings: list of warnings
        :return: None
        """
        self.warnings["data"]["warning_text"].extend(warnings)
        self.session.item.save(self.warnings)

    def set_logging(self):
        """disables in-memory logging if the simulation is too large"""
        ram_per_core = (
            (psutil.virtual_memory().available / 1024) * 0.90 / psutil.cpu_count()
        )  # in MB
        if model_simulation_size(self.model) > ram_per_core:  # set the right logging
            self.model.DisableInMemoryLogging()

    def solve_statics(self, progress_queue) -> bool:
        """solves the model in statics and returns dict with data about the statics solution"""

        def report_statics(model: Model, progress: str) -> None:
            """handler for statics progess"""
            sp = dict(
                progress=f"statics: {progress}",
                time_to_go=model.simulationTimeToGo,
                pretty_time=nice_time(model.simulationTimeToGo),
            )
            progress_queue.put(sp)

        self.model.staticsProgressHandler = report_statics
        self.update_task_state(JobState.RUNNING_STATICS)
        statics = {}  # we save info about how well statics went

        def save_statics_data():
            self.add_item_data("statics", statics, meta={"_class": "orcaflex.statics"})

        try:
            start = time.time()  # we time how long statics takes
            try:
                solved_model(
                    self.model, self.options.max_search_attempts
                )  # solves with search if required
            except QalxSmartStaticsError:
                fn = f"{self.entity['meta']['case_name']}_FAILED_SS.dat"
                ff = self.session.item.add(
                    source=BytesIO(self.model.SaveDataMem()),
                    file_name=fn,
                    meta={"_class": "orcaflex.failed_statics"},
                )
                self.entity["items"]["failed_statics"] = ff
                self.update_task_state(JobState.STATICS_FAILED)
                return False
            end = time.time()
            statics["time_to_solve"] = end - start
            statics["solves"] = True
            save_statics_data()
            self.update_task_warnings(
                self.model.warnings
            )  # add the warnings if there were any
            return True  # this worked
        except DLLError as err:  # there was an error in OrcFxAPI
            self.update_task_state(JobState.ERROR, error=str(err))
            statics["solves"] = False
            save_statics_data()
            return False
        except Exception as err:  # there was a qalx_orcaflex error
            tb = traceback.format_exc()
            self.update_task_state(JobState.ERROR, error=str(err) + tb)
            statics["solves"] = False
            save_statics_data()
            return False

    def run_dynamics(self, progress_queue) -> bool:
        """runs the simulation"""

        def report_dynamics(
            model: Model, current_time: float, start: float, stop: float
        ):
            """progress handler for dynamics"""

            def dynamic_percent() -> float:
                """calculate the percentage completion based on start,
                stop and current time"""
                secs_in = abs((start - current_time))
                total_secs = stop - start
                if total_secs:
                    return secs_in / total_secs
                else:
                    return 0.0

            pc = dynamic_percent()
            pretty_time = nice_time(
                model.simulationTimeToGo
            )  # make a nice time from seconds
            if pretty_time is None:
                pretty_time = f"{pc:2.1%}"
            dp = dict(
                progress=f"dynamics: {pretty_time}",
                start_time=start,
                end_time=stop,
                current_time=current_time,
                time_to_go=model.simulationTimeToGo,
                percent=pc,
                pretty_time=pretty_time,
            )
            progress_queue.put(dp)

        self.model.dynamicsProgressHandler = report_dynamics
        self.update_task_state(JobState.RUNNING_DYNAMICS)
        success = False  # we might need to have a few goes at getting a licence
        while not success:
            try:
                self.model.RunSimulation()
                self.update_task_warnings(self.model.warnings)
                return True  # worked
            except OrcFxAPI.DLLError as err:
                if (
                    err.status == OrcFxAPI.stLicensingError
                ):  # if we got a licence error then wait and try again
                    time.sleep(
                        randint(20, 600)
                    )  # TODO: make this smarter, ten minis to wait could be overkill
                    self.session.log.debug("waiting for licence... " + str(err))
                else:  # some other kind of error best report it
                    tb = traceback.format_exc()
                    self.update_task_state(JobState.ERROR, str(err) + "\n\n" + tb)
                    return False  # didn't work

    def save_sim_to_qalx(self):
        """save simulation file to qalx"""
        self.update_task_state(JobState.SAVING_SIMULATION)
        try:
            model_bytes = self.model.SaveSimulationMem()
            sim_name = f"{self.entity['meta']['case_name']}.sim"
            self.entity["items"]["simulation_file"] = self.session.item.add(
                source=BytesIO(model_bytes),
                file_name=sim_name,
                meta={"_class": "orcaflex.simulation_file"},
            )
            self.save_entity()
            self.update_task_state(JobState.SIMULATION_SAVED)
        except Exception as err:
            msg = """Failed to save a simulation:\n\n""" + str(err)
            self.update_task_warnings([msg])

    def save_sim_to_disk(self, path: Path):
        """
        save simulation file to local disk

        :param path: pathlib.Path to save the simulation file to
        :return:
        """
        """save simulation file to qalx"""
        self.update_task_state(JobState.SAVING_SIMULATION)
        try:
            self.model.SaveSimulation(path)
            self.update_task_state(JobState.SIMULATION_SAVED)
            return True, None  # worked with no errors
        except Exception as err:
            msg = """Failed to save a simulation:\n\n""" + str(err)
            self.update_task_state(JobState.ERROR, error=msg)
            return False, msg  # there was a problem

    def _time_history(
        self, required_result_data: TimeHistory, result_number: int
    ) -> TimeHistory:
        """
        extract a TimeHistory from the model

        :param required_result_data: a data_models.TimeHistory
        :return: the TimeHistory object with the result data added
        """
        ofx_obj = self.model[required_result_data.object]  # get the OrcaFlexObject
        obj_ex = required_result_data.object_extra.to_orcfxapi(
            ofx_obj.type
        )  # get the ObjectExtra
        period = required_result_data.period.to_orcfxapi()  # get the Period
        th = ofx_obj.TimeHistory(
            required_result_data.variable, period=period, objectExtra=obj_ex
        )  # extract TimeHistory
        required_result_data.extracted.time = list(
            self.model.general.TimeHistory("Time", period=period)
        )  # get time for x-axis
        required_result_data.extracted.y_values = list(th)  # y axis
        required_result_data.extracted.static_value = ofx_obj.StaticResult(
            required_result_data.variable, objectExtra=obj_ex
        )  # static value
        if (
            required_result_data.meta.name is None
        ):  # if we don't have a name for this result then make one
            required_result_data.meta.name = result_name(
                result_number,
                ofx_obj,
                OrcFxAPI.rtTimeHistory,
                result_name=required_result_data.variable,
                oe=obj_ex,
            )
        else:  # or ensure it is unique
            required_result_data.meta.name = (
                f"r#{result_number}: {required_result_data.meta.name}"
            )
        required_result_data.meta.var_details = result_details(
            ofx_obj,
            OrcFxAPI.rtTimeHistory,
            result_name=required_result_data.variable,
            oe=obj_ex,
        )  # get all the gory details of the result
        return required_result_data

    def _range_graph(
        self, required_result_data: RangeGraph, result_number: int
    ) -> RangeGraph:
        """
        extract a RangeGraph from the model

        :param required_result_data: a data_models.RangeGraph
        :return: the RangeGraph object with the result data added
        """
        ofx_obj = self.model[required_result_data.object]  # get the OrcaFlexLineObject
        arc_length_range = (
            required_result_data.arc_length_range.to_orcfxapi()
        )  # get the ArcLengthRange
        obj_ex = required_result_data.object_extra.to_orcfxapi(
            ofx_obj.type
        )  # get the Period
        period = required_result_data.period.to_orcfxapi()  # get the ObjectExtra
        rg = ofx_obj.RangeGraph(
            required_result_data.variable,
            period,
            obj_ex,
            arc_length_range,
            required_result_data.storm_duration_hours,
        )  # extract RangeGraph
        required_result_data.extracted.arc = list(rg.X)  # x-axis
        required_result_data.extracted.y_static = list(
            ofx_obj.RangeGraph(
                required_result_data.variable,
                OrcFxAPI.Period(OrcFxAPI.pnStaticState),
                obj_ex,
                arc_length_range,
            ).Mean
        )  # get the static values
        required_result_data.extracted.y_max = list(rg.Max)
        required_result_data.extracted.y_mean = list(rg.Mean)
        required_result_data.extracted.y_min = list(rg.Min)
        if (
            required_result_data.meta.name is None
        ):  # if we don't have a name for this result then make one
            required_result_data.meta.name = result_name(
                result_number,
                ofx_obj,
                OrcFxAPI.rtRangeGraph,
                result_name=required_result_data.variable,
                oe=obj_ex,
            )
        else:  # or ensure it is unique
            required_result_data.meta.name = (
                f"r#{result_number}: {required_result_data.meta.name}"
            )
        required_result_data.meta.var_details = result_details(
            ofx_obj,
            OrcFxAPI.rtRangeGraph,
            result_name=required_result_data.variable,
            oe=obj_ex,
        )
        return required_result_data

    def extract_results(self):
        """extract all the required results"""
        self.update_task_state(JobState.EXTRACTING_RESULTS)
        self.session.log.debug(self.orcaflex_job.results)
        for res_n, (_, result_guid) in enumerate(
            self.orcaflex_job.results["data"].items()
        ):  # for all the results specified
            try:
                result = self.session.item.get(guid=result_guid)  # get the result item
                if result["data"]["_type"] == "th":  # if it's a time history
                    extracted_result = self._time_history(
                        TimeHistory.from_dict(result["data"]), res_n
                    )
                else:
                    extracted_result = self._range_graph(
                        RangeGraph.from_dict(result["data"]), res_n
                    )
                result[
                    "data"
                ] = (
                    extracted_result.to_valid_dict()
                )  # put our data into the result Item
                self.session.item.save(result)  # save the item back to qalx
            except Exception as err:  # something went wrong
                msg = f"Failed to extract result with guid {result_guid}:\n\n{err}"
                self.session.log.error(msg + "\n\n" + traceback.format_exc())
                self.update_task_warnings([msg])
        self.update_task_state(JobState.RESULTS_EXTRACTED)

    def extract_loadcase_info(self):
        """extract load case information"""
        for mi in self.orcaflex_job.load_case_info["data"]["model_info"]:
            mi["value"] = self.model[mi["object_name"]].GetData(
                mi["data_name"], mi["item_index"]
            )  # get the value for the given tag data

        # get all tags on general that start with "lci__"
        def _lci(key):
            # print(key)
            return key.startswith("lci__")

        for k, v in get_tags(self.model, tag_filter=_lci)["General"].items():
            self.orcaflex_job.load_case_info["data"]["model_info"].append(
                asdict(ModelInfo("general", "tag", alias=k.split("__")[-1], value=v))
            )
        self.session.item.save(self.orcaflex_job.load_case_info)

    def _model_view(self, model_view: ModelView) -> str:
        """extract a model view"""
        vp = model_view.to_orcfxapi(self.model)  # make ViewParameters
        save_bytes = self.model.SaveModelViewMem(
            viewParameters=vp
        )  # bytes of saved view
        mvi = self.session.item.add(
            source=BytesIO(save_bytes),
            file_name=model_view.view_filename,
            meta={"_class": "orcaflex.saved_view"},
        )  # save to qalx
        return mvi.guid

    def extract_model_views(self):
        """extract all model views"""
        saved_views = {}
        if (
            self.orcaflex_job.model_views
        ):  # we have some pre-defined views in the OrcaFlexJob
            self.update_task_state(JobState.EXTRACTING_MODEL_VIEWS)
            for mv_name, mv_raw in self.orcaflex_job.model_views["data"].items():
                try:
                    saved_views[mv_name] = self._model_view(ModelView(**mv_raw))
                except Exception as err:
                    self.update_task_warnings(
                        [f"{mv_name} failed. Reason\n {str(err)}"]
                    )

        mv_tags = get_tags(self.model, lambda t: t.startswith("mv__"), True)
        if mv_tags:
            flag_state = False
            for _, tags in mv_tags.items():
                # get all the views defined in the model file
                for tag, data in tags.items():
                    if flag_state is False:
                        self.update_task_state(JobState.EXTRACTING_MODEL_VIEWS)
                        flag_state = True
                    data["ViewName"] = tag.split("__")[-1]
                    try:
                        saved_views[data["ViewName"]] = self._model_view(
                            ModelView(**data)
                        )
                    except Exception as err:
                        self.update_task_warnings(
                            [f"{tag} failed. Reason\n {str(err)}"]
                        )

        if (
            saved_views
        ):  # if we saved some views then we add the item to the Job and save it
            svi = self.session.item.add(
                data=saved_views, meta={"_class": "orcaflex.saved_views"}
            )
            self.entity["items"]["saved_views"] = svi
            self.update_task_state(JobState.MODEL_VIEWS_EXTRACTED)

    def extract_model_videos(self):
        """extract model videos"""
        self.update_task_state(JobState.EXTRACTING_MODEL_VIDEOS)
        video_extractor.extract_model_videos(
            job=self, ofx=self.orcaflex_job, model=self.model
        )
        self.update_task_state(JobState.MODEL_VIDEOS_EXTRACTED)

    def ___get_kill_task(self):
        # if (
        #         self.options.killable
        # ):  # allows killing jobs/bots although this is not tested or
        #     # documented and might not work
        #     kill_signal = self.orcaflex_job.kill_signal
        #     if kill_signal["data"].get("KILL BOT"):
        #         self.publish_status(
        #             "Bot kill signal sent", kill_signal["data"]
        #         )
        #         self.update_task_state(JobState.USER_CANCELLED)
        #         self.terminate()
        #         return False
        #     if kill_signal["data"].get("KILL JOB"):
        #         self.publish_status(
        #             "Job kill signal sent", kill_signal["data"]
        #         )
        #         self.update_task_state(JobState.USER_CANCELLED)
        #         return False
        raise NotImplementedError

    def post_dynamics(self, progress_queue):
        """calls all the post-processing that is requried on the task and pushes updates to a queue

        :param progress_queue: [queue.Queue] for updates.
        :return:
        """
        if self.options.save_simulation:  # save the sim
            self.save_sim_to_qalx()
        if self.orcaflex_job.results:
            self.extract_results()
        if self.orcaflex_job.load_case_info:
            self.extract_loadcase_info()
        if self.orcaflex_job.model_views or get_tags(
            self.model, lambda t: t.startswith("mv__"), True
        ):
            self.extract_model_views()
        if self.orcaflex_job.model_videos:
            self.extract_model_videos()
        if (
            str(self.model.state) == "SimulationStoppedUnstable"
        ):  # if the simulation was unstable then let us know
            msg = "Simulation was unstable at {:2.3f}s".format(
                self.model.simulationTimeStatus.CurrentTime
            )
            self.update_task_warnings([msg])
            self.update_task_state(JobState.SIMULATION_UNSTABLE)
        self.entity["meta"]["processing_complete"] = True  # we done.
        # Signal the end of update worker thread and release the memory
        progress_queue.put(None)
        progress_queue.join()

    def run_simulation(self, progress_queue):
        self.set_logging()
        statics_solved = self.solve_statics(progress_queue)
        if statics_solved and (
            self.model.general.DynamicsEnabled == "Yes"
        ):  # statics worked
            self.run_dynamics(progress_queue)
            self.post_dynamics(progress_queue=progress_queue)
        self.entity["meta"]["processing_complete"] = True


class NormalTask(Task, ABC):
    """
    This is the "classic" qalx task where you are running a single data file.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_task_state(JobState.LOADING_MODEL_DATA)
        self.model = load_model_data(self.orcaflex_job, self.options)

    def process(self):
        self.update_task_state(JobState.PROCESSING)

        progress_queue = queue.Queue()
        threading.Thread(
            target=update_job_progress,
            args=(self.orcaflex_job, progress_queue, self.options, self.session),
        ).start()

        self.run_simulation(progress_queue=progress_queue)


class RestartTask(Task, ABC):
    """
    This is a task where the data file requires a parent simulation to run.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_dir = Path(site_data_dir("QalxOrcaFlex", "AgileTek")).joinpath(
            "Restarts"
        )
        self.site_dir.mkdir(parents=True, exist_ok=True)

    @property
    def parent_sim_path(self):
        """
        creates a sim file name in the ``site_dir`` with hash of the data as the filename.

        :return: pathlib.Path
        """
        return self.site_dir.joinpath(f"{data_hash(self.model)}.sim")

    def save_to_disk_as_parent(self):
        parent_path = self.parent_sim_path
        self.save_sim_to_disk(parent_path)
        return parent_path

    def correct_parent_and_load_model(self, parent_path: Path):
        """change the parent filename in the data file to match the parent file name on disk. Then load the
        model into the ``Task.model`` attribute

        :param parent_path:
        :return:
        """
        with ModelWithLicence(
            self.options.licence_attempts, 10, self.options.max_wait
        ) as model:
            if self.orcaflex_job.data_file_path:  # if this is a task with a local path
                child_path = self.orcaflex_job.data_file_path["data"]["full_path"]
                correct_parent(child_path, parent_path)
                model.LoadData(child_path)
                self.model = model
            elif (
                self.orcaflex_job.data_file
            ):  # if this is a task with a data file in qalx
                data_file_suffix = self.orcaflex_job.data_file.file.name.split(".")[-1]
                child_file_name = (
                    f"{self.orcaflex_job.data_file.guid}.{data_file_suffix}"
                )
                temp_dir = mkdtemp()
                self.orcaflex_job.data_file.save_file_to_disk(temp_dir, child_file_name)
                child_path = Path(temp_dir).joinpath(child_file_name)
                correct_parent(child_path, parent_path)
                model.LoadData(child_path)
                self.model = model
            else:
                raise AttributeError(
                    "orcaflex_job must have a data_file or data_file_path"
                )


class RestartFromSim(RestartTask, ABC):
    """
    This is a task where the sim file parent is stored in qalx and a reference exists in the data item.
    """

    def __init__(self, entity, session):
        super().__init__(entity=entity, session=session)
        self.data_file = entity["items"].data_file

    def process(self):
        sim_guid = self.data_file.meta.restart_parent.sim_item
        parent_path = self.site_dir.joinpath(f"{sim_guid}.sim")
        if not parent_path.exists():  # save the file to disk if it is not there
            parent_sim_item = self.session.item.get(sim_guid)
            parent_sim_item.save_file_to_disk(
                filepath=self.site_dir, filename=f"{sim_guid}.sim"
            )

        self.update_task_state(JobState.PROCESSING)
        progress_queue = queue.Queue()
        threading.Thread(
            target=update_job_progress,
            args=(self.orcaflex_job, progress_queue, self.options, self.session),
        ).start()

        self.update_task_state(JobState.LOADING_MODEL_DATA)
        self.correct_parent_and_load_model(parent_path)
        self.run_simulation(progress_queue)


class RestartFromChain(RestartTask, ABC):
    """
    This task requires a chain of parent tasks to be run before it can be processed.
    The chain is only run to generate the parent of the data_file, none of the parents are
    subjected to post-processing.
    """

    def __init__(self, entity, session):
        super().__init__(entity=entity, session=session)
        self.data_file = entity["items"].data_file

    def correct_parent_and_load_model_mid_chain(
        self, parent_path: Path, child_data_file
    ):
        """for a child data file, save the file to disk and correct the parent to point to the correct file.
        Load the model data into Task.model

        :param parent_path:
        :param child_data_file:
        :return:
        """
        with ModelWithLicence(
            self.options.licence_attempts, 10, self.options.max_wait
        ) as child_model:
            data_file_suffix = child_data_file.file.name.split(".")[-1]
            child_file_name = f"{child_data_file.guid}.{data_file_suffix}"
            temp_dir = mkdtemp()
            child_data_file.save_file_to_disk(temp_dir, child_file_name)
            child_path = Path(temp_dir).joinpath(child_file_name)
            correct_parent(child_path, parent_path)
            child_model.LoadData(child_path)
            self.model = child_model

    def process(self):
        """process a file with a chain of restarts defined in meta.chain_file_items

        :return:
        """
        chain = self.data_file.meta["chain_file_items"]

        self.update_task_state(JobState.PROCESSING)
        progress_queue = queue.Queue()
        threading.Thread(
            target=update_job_progress,
            args=(self.orcaflex_job, progress_queue, self.options, self.session),
        ).start()
        base = chain[0]
        # The first model in the chain needs to be run and saved to disk for the rest of the chain to run
        base_item = self.session.item.get(base)
        with ModelWithLicence(
            self.options.licence_attempts, 10, self.options.max_wait
        ) as base_model:
            base_model.LoadDataMem(base_item.read_file())
            self.model = base_model
            self.set_logging()
            self.solve_statics(progress_queue)
            if base_model.general.DynamicsEnabled == "Yes":
                self.run_dynamics(progress_queue)
            parent_sim_path = self.site_dir.joinpath(f"{str(base)}.sim")
            self.save_sim_to_disk(parent_sim_path)

        # now go down the chain running each model in turn
        for descendant in chain[1:]:
            descendant_item = self.session.item.get(descendant)
            self.correct_parent_and_load_model_mid_chain(
                parent_sim_path, descendant_item
            )
            self.set_logging()
            # model DynamicsEnabled ?
            self.solve_statics(progress_queue)
            if self.model.general.DynamicsEnabled == "Yes":
                self.run_dynamics(progress_queue)
            parent_sim_path = self.site_dir.joinpath(f"{str(descendant_item.guid)}.sim")
            self.save_sim_to_disk(parent_sim_path)

        # now the full chain has been processed we can run the final model.
        self.correct_parent_and_load_model(parent_sim_path)
        self.run_simulation(progress_queue)


class ChainTask:
    """
    This is a task where all the tasks in the chain require full processing.
    """

    def __init__(self, tasks_sets, chain, session):
        """build a list of RestartTask in the correct order

        :param tasks_sets: all the sets on the task
        :param chain: the guids that specify the order of the chain
        :param session: the job session
        """
        self.tasks = []
        for task_guid in reversed(chain):
            # https://stackoverflow.com/a/2569076
            sub_task_name = next(
                key for key, value in tasks_sets.items() if value == task_guid
            )
            task_set = tasks_sets[sub_task_name]
            self.tasks.append(RestartTask(entity=task_set, session=session))

    def process(self):
        # Process the base task and save the sim to disk
        base_task = self.tasks[0]
        base_task.update_task_state(JobState.PROCESSING)
        base_progress_queue = queue.Queue()
        threading.Thread(
            target=update_job_progress,
            args=(
                base_task.orcaflex_job,
                base_progress_queue,
                base_task.options,
                base_task.session,
            ),
        ).start()
        base_task.model = load_model_data(base_task.orcaflex_job, base_task.options)
        base_task.run_simulation(base_progress_queue)
        parent_sim_path = base_task.save_to_disk_as_parent()
        base_progress_queue.join()

        # iterate over the descendant tasks performing full processing
        for descendant_task in self.tasks[1:]:
            descendant_task.correct_parent_and_load_model(parent_sim_path)
            descendant_task.update_task_state(JobState.PROCESSING)
            progress_queue = queue.Queue()
            threading.Thread(
                target=update_job_progress,
                args=(
                    descendant_task.orcaflex_job,
                    progress_queue,
                    descendant_task.options,
                    descendant_task.session,
                ),
            ).start()
            descendant_task.run_simulation(progress_queue=progress_queue)
            parent_sim_path = descendant_task.save_to_disk_as_parent()
            progress_queue.join()


def update_job_progress(
    orcaflex_job: OrcaFlexJob,
    update_queue: Queue,
    options: OrcaFlexJobOptions,
    session: QalxSession,
):
    """update the progress and save the item"""
    time_of_last_update = time.time()
    if orcaflex_job.progress:
        should_exit = False
        while not should_exit:
            progress = update_queue.get()
            update_queue.task_done()
            if progress is None:
                should_exit = True
            else:
                time_since_last_update = time.time() - time_of_last_update
                if time_since_last_update > options.update_interval:
                    orcaflex_job.progress["data"] = progress
                    session.item.save(orcaflex_job.progress)
                    time_of_last_update = time.time()


class VideoTask(Task):
    def __init__(self, entity: Union[Set, UUID], session: QalxSession):
        super().__init__(entity, session)

    def process(self):
        self.extract_model_videos()
