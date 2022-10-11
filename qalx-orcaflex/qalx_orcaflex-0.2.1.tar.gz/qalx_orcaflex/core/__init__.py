import concurrent.futures
import threading
import time
from collections import defaultdict
from copy import deepcopy
from dataclasses import asdict
from os import PathLike
from pathlib import Path
from pprint import pformat
from tempfile import TemporaryDirectory
from typing import Union, Sequence, Mapping, List, Tuple

import OrcFxAPI
import numpy as np
import pyqalx
import yaml
from OrcFxAPI import Model
from pyqalx import QalxSession, Item, Group, Set
from pyqalx.core.errors import QalxEntityNotFound
from qalx_orcaflex.gui.batch.overview_main import run_gui, BatchOverview

from qalx_orcaflex import data_models
from qalx_orcaflex.data_models import JobState
from qalx_orcaflex.helpers import (
    data_file_paths,
    required_results_from_yaml,
    clean_set_key,
    orcaflex_file_type,
    resolve_parents,
    parse_restart_chain,
    eliminate_subsets,
)
from qalx_orcaflex.video.helpers import unpack_model_videos, check_sim_file_type

LOAD_CASE_INFO = data_models.LoadCaseInfo()

ORCA_FLEX_JOB_OPTIONS = data_models.OrcaFlexJobOptions()


class QalxOrcaFlexError(Exception):
    def __init__(self, *args, **kwargs):
        pass


class QalxSmartStaticsError(QalxOrcaFlexError):
    """Error related to the smart statics utility."""


class QalxSmartStaticsFailed(QalxSmartStaticsError):
    """We tried to do smart statics and it didn't work."""


class BaseSource:
    """base class for batch sources.

    Any child class must implement a `to_jobs` method which takes a base_job and
    temp_folder argument and returns a generator of jobs

    the temp_folder will be automatically deleted by the batch manager after the
    batch has been submitted.
    """

    def __init__(self, *args, **kwargs):
        pass

    def _update_copy(self, base, update):
        new = deepcopy(base)
        new.update(update)
        return new


class NewSource(BaseSource):
    """base class for batch sources with new data files. These also need to support restarts.

    Any child class must implement a `to_jobs` method which takes a base_job and
    temp_folder argument and returns a generator of jobs

    The `use_orcfxapi` keyword argument can be set false to avoid using an OrcaFlex licence when inspecting the job.

    the temp_folder will be automatically deleted by the batch manager after the
    batch has been submitted.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_orcfxapi = kwargs.get("use_orcfxapi", True)
        if self.use_orcfxapi:
            self.model = OrcFxAPI.Model(threadCount=1)

    def _link_restart_parent(self, data_file: dict, data_file_path: Path) -> None:
        """establish the chain of restart parents for the file at ``data_file_path`` and if it exists store the
        information in the ``data_file``

        :param data_file: dict with infor on the data file
        :param data_file_path: path of data file
        :return: None
        """
        if self.use_orcfxapi:
            self.model.LoadData(str(data_file_path))
            chain = [str(Path(p).resolve()) for p in self.model.restartParentFileNames]
        else:
            chain = resolve_parents(data_file_path)
        if chain:
            parse_restart_chain(data_file, chain)

    def _data_file_type(self, path: Path) -> OrcFxAPI.ModelType:
        """gets the type of data OrcaFlex data file at the path.

        If use_orcaflex is False then the yml will be inspected for keys that indicate the model type.

        :param path:
        :return: OrcFxAPI.ModelType
        """
        if self.use_orcfxapi and (path.suffix in (".yml", ".yaml")):
            data_file_type = orcaflex_file_type(self.model, path)
        elif (not self.use_orcfxapi) and (path.suffix in (".yml", ".yaml")):
            with open(path, "rb") as fp:
                yaml_data = yaml.load(fp)
            if "RestartingFrom" in yaml_data:
                data_file_type = OrcFxAPI.ModelType.Restart
            elif "BaseFile" in yaml_data:
                data_file_type = OrcFxAPI.ModelType.Variation
            else:
                data_file_type = OrcFxAPI.ModelType.Standard
        else:
            data_file_type = OrcFxAPI.ModelType.Standard
        return data_file_type

    def _inspect_file(
        self, data_file: dict, path: PathLike
    ) -> Tuple[Path, type(OrcFxAPI.ModelType)]:
        """extract detail about the data file and its model type

        :param data_file: dict of details about the data file
        :param path: path to the data file
        :return: tuple of pathlib.Path to the file and the OrcFxAPI.ModelType
        """
        dfp = Path(path)
        data_file["meta"]["_class"] = "orcaflex.job.data_file"
        data_file["meta"]["data_file_path"] = str(dfp)
        data_file["meta"]["data_file_name"] = dfp.name
        data_file["meta"]["data_file_drive"] = dfp.drive
        data_file["meta"]["data_file_uri"] = dfp.as_uri()
        data_file_type = self._data_file_type(dfp)
        if data_file_type == OrcFxAPI.ModelType.Restart:
            self._link_restart_parent(data_file, dfp)
        data_file["meta"]["data_file_type"] = str(data_file_type)
        return dfp, data_file_type


class DataFileItemsSource(BaseSource):
    def __init__(self, items: Sequence[Item]):
        """an iterable of existing data file items.

        This is useful when re-running a batch with some updated info or settings.

        :param items:
        """
        super(DataFileItemsSource, self).__init__(items)
        self.items = items

    def to_jobs(self, base_job: Mapping, temp_folder: Path) -> Mapping:
        for dfi in self.items:
            job = self._update_copy(
                base_job,
                {
                    "data_file": dfi,
                    "case_name": dfi["meta"]["data_file_name"].split(".")[0],
                },
            )
            yield job


class ModelSource(NewSource):
    def __init__(self, model: Model, name: str):
        """an OrcFxAPI.Model instance as the source, requires a model name

        :param model: an OrcFxAPI.Model instance that you want to add to the batch
        :param name: the name of the model, used as the file name to save back later.
        """
        super(ModelSource, self).__init__(model, name)
        self.model = model
        self.name = name
        self._clean_name = clean_set_key(name)

    def to_jobs(self, base_job: Mapping, temp_folder: Path) -> Mapping:
        filename = f"{self.name}.dat"
        model_path = temp_folder.joinpath(filename)
        self.model.SaveData(model_path)

        data_file = {
            "source": model_path,
            "meta": {"_class": "orcaflex.job.data_file", "data_file_name": filename},
        }
        if self.model.type == OrcFxAPI.ModelType.Restart:
            chain = [str(Path(p).resolve()) for p in self.model.restartParentFileNames]
            parse_restart_chain(data_file, chain)
        job = self._update_copy(
            base_job, {"data_file": data_file, "case_name": self._clean_name}
        )
        yield job


class FileSource(NewSource):
    def __init__(self, path: PathLike, use_orcfxapi: bool = True):
        """a file source

        :param path:
        :param use_orcfxapi: if True then will use an OrcaFlex licence to check the data_file_type and
                             get information about restart parents.
        """
        super(FileSource, self).__init__(path, use_orcfxapi=use_orcfxapi)
        self.path = path

    def to_jobs(self, base_job: Mapping, temp_folder: Path) -> Mapping:
        data_file = {"source": self.path, "meta": {}}
        data_file_path, data_file_type = self._inspect_file(data_file, self.path)
        job = self._update_copy(
            base_job,
            {"data_file": data_file, "case_name": clean_set_key(data_file_path.stem)},
        )
        yield job


class DirectorySource(NewSource):
    def __init__(
        self,
        directory: Union[PathLike, Sequence[PathLike]],
        skip_fails: bool = False,
        recursive: bool = False,
        use_orcfxapi: bool = True,
    ):
        """takes a directory of files and adds them all.

        :param directory: path to search for data files
        :param skip_fails: don't error if there is a failed path e.g. it is deleted while searching (default=False)
        :param recursive: search all subdirectories (default=False)
        :param use_orcfxapi: will make sure only OrcaFlex yaml files are added - THIS USES AN ORCAFLEX LICENCE
                           (default=True)
        """
        super(DirectorySource, self).__init__(
            directory, skip_fails, recursive, use_orcfxapi=use_orcfxapi
        )
        self.directory = directory
        self.skip_fails = skip_fails
        self.recursive = recursive
        if self.use_orcfxapi:
            self.model = OrcFxAPI.Model(threadCount=1)

    def to_jobs(self, base_job: Mapping, _) -> Mapping:
        for dfp in data_file_paths(self.directory, self.skip_fails, self.recursive):
            if self.use_orcfxapi and (dfp.suffix in (".yml", ".yaml")):
                data_file_type = orcaflex_file_type(self.model, dfp)
                if not data_file_type:
                    continue  # this is not an OrcaFlex yml file, so we can ignore it

            data_file = {
                "source": str(dfp),
                "meta": {"_class": "orcaflex.job.data_file"},
            }
            self._inspect_file(data_file, dfp)
            job = self._update_copy(
                base_job, {"data_file": data_file, "case_name": clean_set_key(dfp.stem)}
            )
            yield job


class OrcaFlexBatchManager:
    """manager class for collecting batch info"""

    def __init__(self, temp_folder):
        """instance is returned by :ref:OrcaFlexBatch as context manager

        This collects all the sources for the jobs added to the batch.
        """
        self.orcaflex_jobs = []
        self._temp_folder = Path(temp_folder)

    def add(
        self,
        source: Union[BaseSource, NewSource],
        job_options: data_models.OrcaFlexJobOptions = ORCA_FLEX_JOB_OPTIONS,
        required_results: Union[
            PathLike, Sequence[Union[data_models.TimeHistory, data_models.RangeGraph]]
        ] = (),
        model_views: Sequence[data_models.ModelView] = (),
        model_videos: Sequence[data_models.VideoSpecification] = None,
        load_case_info: data_models.LoadCaseInfo = LOAD_CASE_INFO,
    ):
        """add data files to a batch based on a source and extra options.

        :param source: a child of :ref:BaseSource or :ref:NewSource that implements `to_jobs`
        :param job_options: various options and settings see
            :ref:data_models.OrcaFlexJobOptions
        :param required_results: an iterator containing :ref:data_models.TimeHistory
            or :ref:data_models.RangeGraph
            (a mix of both is allowed) or a path to a yaml file with the correct
            Results structure.
        :param model_views: an iterator containing :ref:data_models.ModelView
        :param model_videos: An list of VideoSpecification instances
        :param load_case_info: information about the load case to be used during
            presentation of results
            see :ref:data_models.LoadCaseInfo
        :return: None
        """
        if isinstance(required_results, PathLike):
            required_results = required_results_from_yaml(required_results)
        base_job = {
            "job_options": job_options,
            "required_results": required_results,
            "load_case_info": load_case_info,
            "model_views": model_views,
            "model_videos": model_videos,
        }
        for job in source.to_jobs(base_job, self._temp_folder):
            self.orcaflex_jobs.append(job)


class OrcaFlexBatch:
    """
    .. _OrcaFlexBatch:
    .. auto

    """

    def __init__(
        self,
        name,
        session: QalxSession,
        batch_options: data_models.BatchOptions,
        dry_run: bool = False,
        meta: Mapping = None,
        verbose: bool = False,
    ):
        """a batch of OrcaFlex data files

        :param name: name of the batch
        :param session: a QalxSession
        :param batch_options: see :ref:data_models.BatchOptions
        :param dry_run: if True will not build or submit the batch but will print name
            of each case
        :param meta: additional metadata to add to the group entitiy
        :param verbose: print statements of progress as build is in progress
        """
        self.name = name
        self.session = session
        self.batch_options = batch_options
        self.temp_dir = TemporaryDirectory()
        self.dry_run = dry_run
        standard_meta = {
            "_class": "orcaflex.batch",
            "name": self.name,
            "options": self.batch_options.to_valid_dict(),
            "state": "new",
        }
        if meta is None:
            self.meta = standard_meta
        else:
            self.meta = standard_meta
            self.meta.update(meta)
        self.verbose = verbose
        self.contains_restarts = None

    @classmethod
    def get_and_check_progress(cls, batch_name, ofx_session=None):
        """Given a name of a batch, run the GUI tool for batch progress"""
        if ofx_session is None:
            ofx_session = QalxOrcaFlex()
        run_gui(ofx_session=ofx_session, batch_name=batch_name)

    def _add_case(self, case_n: int, job: Mapping) -> str:
        """adds a case to qalx

        :param case_n: case number
        :param job: job data
        :return: str of the case_name
        """
        case_name = f"[{case_n + 1}] {job['case_name']}"  # build a unique case name
        if (
            self.dry_run
        ):  # we don't want to create anything just show that we would have been
            # able to (probably)
            print(f"[DRY_RUN] Building {case_name}")
            return case_name

        # make the set but it will be empty for now. This allows us to reference the
        # parent set in the items
        self.built_sets[case_name] = self.session.set.add(
            items={},
            meta={
                "batch": self.name,
                "_class": "orcaflex.job",
                "case_name": case_name,
                "state": asdict(data_models.OrcaFlexJobState()),
                "send_to": self.batch_options.send_sim_to,
                "is_restart": False,
            },
        )

        # make dicts with data and meta
        opts = dict(
            data=job["job_options"].__dict__, meta={"_class": "orcaflex.job.options"}
        )

        progress = dict(
            data=asdict(data_models.JobProgress("new job")),
            meta={"_class": "orcaflex.job.progress"},
        )
        job_items = {"job_options": opts, "progress": progress}

        # process the data file
        if "data_file" in job:
            if isinstance(
                job["data_file"], Item
            ):  # this is an existing item, update it's batch guid
                existing_item = job["data_file"]
                existing_item["meta"]["case_guid"] = self.built_sets[case_name].guid
            else:
                existing_item = None
                job_items["data_file"] = dict(**job["data_file"])
                job["data_file"]["meta"]["case_guid"] = self.built_sets[case_name].guid

            # here we need to flag a set that restarts from another simulation
            if job["data_file"]["meta"].get("data_file_type") == "Restart":
                self.contains_restarts = True
                self.built_sets[case_name]["meta"]["is_restart"] = True
            else:
                self.built_sets[case_name]["meta"]["is_restart"] = False
        else:
            existing_item = None

        # add all the required results
        if "required_results" in job:
            result_items = {}
            for rn, rr in enumerate(job["required_results"]):
                res_item = dict(
                    data=rr.to_valid_dict(),
                    meta={
                        "_class": "orcaflex.job.required_result",
                        "case_guid": self.built_sets[case_name].guid,
                    },
                )
                # give the result a name of some kind incase it never actually gets processed
                if rr.meta.name:
                    res_name = f"[{rn}] {rr._type} {rr.meta.name}"
                else:
                    res_name = (
                        f"[{rn}] {rr._type} {rr.object} {rr.variable} {str(rr.period)}"
                    )
                    if hasattr(rr, "arc_length_range"):
                        res_name += f" {str(rr.arc_length_range)}"
                result_items[res_name] = res_item
            if result_items:
                many_results = self.session.item.add_many(
                    list(result_items.values())
                )  # add items
                result_items = dict(
                    zip(result_items.keys(), [r["guid"] for r in many_results["items"]])
                )  # re-pack
                # results is a mapping of result name to guid of item
                job_items["results"] = dict(
                    data=result_items,
                    meta={
                        "_class": "orcaflex.job.required_results",
                        "case_guid": self.built_sets[case_name].guid,
                    },
                )
        if "load_case_info" in job:
            job_items["load_case_info"] = dict(
                data=asdict(job["load_case_info"]),
                meta={
                    "_class": "orcaflex.job.load_case_info",
                    "case_guid": self.built_sets[case_name].guid,
                },
            )
        if job.get("model_views"):
            model_views = {}
            for _, mv in enumerate(job["model_views"]):
                model_views[mv.ViewName] = asdict(mv)
            # model views data is mapping of view name to ViewParamters type info
            job_items["model_views"] = dict(
                data=model_views,
                meta={
                    "_class": "orcaflex.job.model_views",
                    "case_guid": self.built_sets[case_name].guid,
                },
            )
        if job.get("model_videos"):
            model_videos = unpack_model_videos(job)
            job_items["model_videos"] = dict(
                data=model_videos,
                meta={
                    "_class": "orcaflex.job.model_videos",
                    "case_guid": self.built_sets[case_name].guid,
                },
            )
        job_item_many = self.session.item.add_many(
            list(job_items.values())
        )  # add all the items
        if job_item_many["errors"]:
            # if there were errors here then we need to raise an exception
            # otherwise the zipping back together will put things in the wrong place.
            raise QalxOrcaFlexError(
                f"There was an error adding one of the items."
                f"More information can be found below:\n\n"
                f"{pformat(job_item_many['errors'])}"
            )
        job_items_zipped = dict(
            zip(job_items.keys(), job_item_many["items"])
        )  # re-pack
        if existing_item is not None:
            job_items_zipped[
                "data_file"
            ] = existing_item  # the existing item didn't need to be added so we add it here
        if self.verbose:  # print
            print(f"added {case_name}")
        self.session.log.info(f"created {case_name}")
        self.built_sets[case_name]["items"] = job_items_zipped  # put items on the set
        self.session.set.save(
            self.built_sets[case_name]
        )  # save the set now it has the items
        return case_name

    def _build(self):
        """build the group

        :return:
        """
        self.session.log.info("Building batch...")
        self.built_sets = {}
        # because the time to write to qalx can be slow depending on system load we
        # need to make sure we are adding
        # all our cases concurrently. This can be done with lots of threads because
        # typically we are waiting for
        # a response from the API and not using CPU or io
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.batch_options.build_threads
        ) as executor:
            future_to_job = {
                executor.submit(self._add_case, case_n, job): case_n
                for (case_n, job) in enumerate(self.batch_manager.orcaflex_jobs)
            }
            for future in concurrent.futures.as_completed(future_to_job):
                case_n = future_to_job[future]
                try:
                    case_name = future.result()
                except Exception as exc:
                    self.session.log.error(
                        "%r generated an exception: %s" % (case_n, exc)
                    )
                    raise exc
                else:
                    self.session.log.debug(f"future {case_name}")

    def _submit(self):
        """this is the method that gets called by the BatchManager to submit the batch to a queue"""

        # check if there are restarts to worry about
        if self.contains_restarts:
            sets_to_run = self._collate_restarts()
            self.meta["restart_chains"] = sets_to_run
            self.meta["contains_restarts"] = True

        self.session.log.info(f"Submitting batch to {self.batch_options.batch_queue}")
        self.group_batch = self.session.group.add(
            sets=self.built_sets, meta=self.meta
        )  # add the group
        self.session.queue.get_or_create(
            self.batch_options.sim_queue
        )  # create the sim queue if required
        batch_queue = self.session.queue.get_or_create(
            self.batch_options.batch_queue
        )  # do batch queue
        # submit batch
        Group.add_to_queue(payload=self.group_batch, queue=batch_queue)

    def _collate_restarts(self) -> List:
        """If the batch contains restarts then we need to ensure that all the parent data or simulation files are
        available to the sim bot. This function ensures that the data or simulation files are stored in qalx for
        any parent of any restart.

        We distinguish between two types of restart in this function:

        - inside: this is a parent in the batch of another data file in the batch
        - outside: this a parent which is not included in the batch

        :return: List
        """
        self.session.log.info("Batch contains restarts")
        all_paths = {
            s["items"].data_file.meta.data_file_path: s.guid
            for n, s in self.built_sets.items()
        }
        restart_sets = list(
            filter(lambda ks: ks[1].meta.is_restart, self.built_sets.items())
        )

        # If the parent of a restart is not part of the batch then we will need to do some work to make sure that the
        # data or simulation file is stored in qalx and is referenced from the set

        inside_chains = (
            []
        )  # chains that are completely inside the batch require further processing

        for name, set_ in restart_sets:
            if set_["items"].data_file.meta.data_file_parent not in all_paths:
                # here we have an outside parent
                self.session.log.info(f"{name} contains a parent outside the batch")
                data_file_meta = set_["items"].data_file.meta
                self.session.log.debug(
                    "Chain of restart ancestors all being added to qalx."
                )
                out_chain = reversed(data_file_meta.data_file_chain)
                # we add all of these to qalx and ensure the set has details about where to get the chain
                chain_file_items = []
                for ancestor in out_chain:
                    fi = self.session.item.add(
                        source=ancestor,
                        meta={"_class": "orcaflex.job.parent_data_file"},
                    )
                    chain_file_items.append(fi.guid)

                set_[
                    "items"
                ].data_file.meta.chain_file_items = (
                    chain_file_items  # save the chain of restart data files
                )
            elif not set_["items"].data_file.meta.get("restart_parent"):
                # these are all inside parents
                inside_chain = set_["items"].data_file.meta.data_file_chain
                inside_chains.append(
                    [set_["items"].data_file.meta.data_file_path] + inside_chain
                )

            if set_["items"].data_file.meta.get(
                "restart_parent"
            ):  # in this case the parent sim file is available on disk
                parent = set_["items"].data_file.meta.get("restart_parent")
                try:  # that sim might already exist on qalx, so we attempt to retrieve it
                    sim_item = self.session.item.find_one(
                        query={
                            "meta": {
                                "_class": "orcaflex.simulation_file",
                                "sim_hash": parent["sim_hash"],
                            }
                        }
                    )
                except QalxEntityNotFound:  # if it's not in qalx then we'll send it
                    sim_item = self.session.item.add(
                        source=parent["sim_path"],
                        meta={
                            "_class": "orcaflex.simulation_file",
                            "sim_hash": parent["sim_hash"],
                        },
                    )
                set_["items"].data_file.meta.restart_parent.sim_item = sim_item.guid
            self.session.item.save(set_["items"].data_file)

        # The code below aims to solve the problem of having large batches with complex restart hierarchies.
        # We want to be able to run independent chains concurrently to simulate most efficiently across a distributed
        # computing network.

        # first, reduce the chains to the smallest number of complete sequences
        maximal_chains = eliminate_subsets(inside_chains)

        # then find the chains that contain common sequences
        common = defaultdict(list)
        for chain in maximal_chains:
            common_elements = [not set(chain).isdisjoint(_s) for _s in maximal_chains]
            common[tuple(common_elements)].append(chain)

        # finally, flatten the chain and remove duplicates while maintaining the order
        sets_to_run = []
        for v in common.values():
            flat_common_guids = [
                all_paths[i] for s in v for i in s
            ]  # we want a chain of UUID here rather than paths
            sets_to_run.append(list(dict.fromkeys(flat_common_guids)))
        return sets_to_run

    def __enter__(self):
        self.temp_dir.__enter__()
        self.batch_manager = OrcaFlexBatchManager(self.temp_dir.name)
        return self.batch_manager

    def __exit__(self, *args):
        if not args[1]:  # if there is an error this argument will be True
            self._build()
            self._submit()
        self.temp_dir.__exit__(*args)

    def check_progress(self):
        """Run the check progress GUI in a separate thread"""
        gui_thread = threading.Thread(target=run_gui, args=(self.session, self.name))
        gui_thread.start()

    def when_complete(self, interval=15, timeout=None, run_with_gui=True):
        """
        Returns a waiter for the batch that is instantiated with the same
        arguments

        :param interval:        The interval to use for the waiter
        :param timeout:     The timeout of the waiter in sec
        :param run_with_gui:    Flag to run or not the GUI for batch overview
                                apart from the waiter
        """
        batches = BatchOverview.get_batches(self.session, self.name)
        batch_overview = BatchOverview(self.session, self.name, batches)
        return Waiter(self, batch_overview, interval, timeout, run_with_gui)


class Waiter:
    """
    Implements "freezing" functionality that stops code execution until a batch
    is complete

    Instance attributes
        batch:          The batch to wait on. The batch should have been added
                        before the waiter is run
        batch_overview: Instance of BatchOverview
        interval:       The interval in seconds to use between checking for
                        updates on the batch. Defaults to 15 seconds
        timeout:        The timeout in seconds to use in order to override the
                        waiting and just exit. This parameter is optional.
        run_with_gui:   Boolean flag to run or not the batch overview GUI
                        in addition. Defaults to True
    """

    def __init__(
        self, batch, batch_overview, interval=15, timeout=None, run_with_gui=True
    ):
        self.batch = batch
        self.batch_overview = batch_overview
        self.index = len(self.batch_overview.batches) - 1
        self.interval = interval
        self.timeout = timeout
        self.run_with_gui = run_with_gui
        self.start_time = time.time()

    def _check_timeout(self):
        """Check if the timeout has been exceeded"""
        if self.timeout is None:
            return False
        return (time.time() - self.start_time) > self.timeout

    def __enter__(self):
        if self.run_with_gui:
            self.batch.check_progress()
        all_complete = False
        while not (all_complete or self._check_timeout()):
            summary_df, _ = self.batch_overview.get_summary_df(self.index)
            complete_array = summary_df.complete.to_numpy()
            all_complete = np.all(complete_array)
            time.sleep(self.interval)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class QalxOrcaFlex(pyqalx.QalxSession):
    """we define a sublcass of QalxSession so there is no need to import from pyqalx

    .. warning::

        There are a load of terrible instance methods defined here just because we
        needed some way of doing these things. They need to be superseded by a better
        API

    """

    def __init__(self, *args, **kwargs):
        super(QalxOrcaFlex, self).__init__(*args, **kwargs)

    def get_batch(self, batch_name: str, many: bool = False):
        if many:
            return self.group.find(
                query={
                    "metadata.data._class": "orcaflex.batch",
                    "metadata.data.name": batch_name,
                }
            )["data"]
        else:
            return self.group.find_one(
                query={
                    "metadata.data._class": "orcaflex.batch",
                    "metadata.data.name": batch_name,
                }
            )

    def get_batch_results_summary(
        self, batch_name: str, many: bool = False
    ) -> Union[Sequence[Mapping], Mapping]:
        if many:
            return [
                self.item.get(g["meta"].get("results_summary", {}).get("data", {}))
                for g in self.get_batch(batch_name, many)["data"]
            ]
        else:
            return self.item.get(
                self.get_batch(batch_name, many)["meta"].get("results_summary", {})
            ).get("data", {})

    def get_batch_results_map(
        self, batch_name: str
    ) -> Mapping[str, Mapping[str, Mapping]]:
        res_map = {}
        batch = self.get_batch(batch_name)
        for case_name, j in batch["sets"].items():
            res_map[case_name] = {}
            if j["items"].get("results"):
                for res_name, res_guid in j["items"].get("results")["data"].items():
                    res_map[j.meta.case_name][res_name] = self.item.get(res_guid)[
                        "data"
                    ]
        return res_map

    def save_batch_views(self, batch_name: str, save_dir: PathLike):
        batch = self.get_batch(batch_name)
        for case_name, job in batch["sets"].items():
            if job["items"].get("saved_views"):
                if not isinstance(job["items"].get("saved_views"), Mapping):
                    views = self.item.get(job["items"].get("saved_views"))["data"]
                else:
                    views = job["items"].get("saved_views")["data"]
                for _, view_guid in views.items():
                    view_file = self.item.get(view_guid)
                    save_name = f"{case_name}-{view_file['file']['name']}"
                    view_file.save_file_to_disk(save_dir, filename=save_name)

    def send_to_video_sim_queue(self, queue_name, ofx_job):
        if ofx_job.sim_file is None and ofx_job.sim_file_path is None:
            raise AttributeError("The job must have a sim_file or sim_file_path")
        if ofx_job.sim_file is None:
            # If the file does not exist, then add it to qalx
            check_sim_file_type(ofx_job.sim_file_path)
            ofx_job.sim_file = self.item.add(
                source=ofx_job.sim_file_path, meta={"_class": "orcaflex.job.sim_file"}
            )
        else:
            check_sim_file_type(ofx_job.sim_file["file"]["name"])
        model_videos = unpack_model_videos(ofx_job.__dict__)
        job_items = {
            "model_videos": dict(
                data=model_videos, meta={"_class": "orcaflex.job.model_videos"}
            ),
            "job_options": dict(
                data=asdict(ofx_job.job_options),
                meta={"_class": "orcaflex.job.options"},
            ),
        }
        job_item_many = self.item.add_many(list(job_items.values()))
        job_items_zipped = dict(zip(job_items.keys(), job_item_many["items"]))
        job_items_zipped["sim_file"] = ofx_job.sim_file
        video_job = self.set.add(
            items=job_items_zipped,
            meta={"_class": "orcaflex.job.video_extraction_from_sim"},
        )
        video_queue = self.queue.get_or_create(queue_name)
        Set.add_to_queue(payload=video_job, queue=video_queue)
        return video_job.guid

    def jobs_by_state(
        self,
        batch_name,
        include: List[JobState] = None,
        exclude: List[JobState] = None,
        unpack=True,
    ):
        if (include is not None) and (exclude is not None):
            raise QalxOrcaFlexError("Only include or exclude can be supplied")
        elif include:
            includes = [i.value for i in include]
            jobs_q = self.set.find(
                query={
                    "metadata.data._class": "orcaflex.job",
                    "metadata.data.state.state": {"$in": includes},
                    "metadata.data.batch": batch_name,
                }
            )
            return jobs_q["data"]
        elif exclude:
            excludes = [e.value for e in exclude]
            jobs_q = self.set.find(
                query={
                    "metadata.data._class": "orcaflex.job",
                    "metadata.data.state.state": {"$nin": excludes},
                    "metadata.data.batch": batch_name,
                }
            )
            return jobs_q["data"]

    def save_job_videos(self, job, save_dir, case_name=""):
        if not isinstance(job, Set):
            job = self.set.get(job)
        if job["items"].get("saved_videos"):
            if not isinstance(job["items"].get("saved_videos"), Mapping):
                videos = self.item.get(job["items"].get("saved_videos"))["data"]
            else:
                videos = job["items"].get("saved_videos")["data"]
            for _, video_guid in videos.items():
                video_file = self.item.get(video_guid)
                save_name = f"{video_file['file']['name']}"
                if case_name:
                    save_name = f"{case_name}-" + save_name
                video_file.save_file_to_disk(save_dir, filename=save_name)

    def save_batch_videos(self, batch_name: str, save_dir: PathLike):
        batch = self.get_batch(batch_name)
        for case_name, job in batch["sets"].items():
            self.save_job_videos(job, save_dir, case_name)

    def _get_progress(self, job):
        if job["items"].get("progress"):
            if not job["meta"].get("processing_complete"):
                if not isinstance(job["items"].get("progress"), Mapping):
                    prog = self.item.get(job["items"].get("progress"))["data"]
                else:
                    prog = job["items"].get("progress")["data"]
                if prog.get("pretty_time"):
                    return prog["pretty_time"] + " to go."
                else:
                    return prog["progress"]
            else:
                return "complete."

    def _get_state(self, job):
        st_str = job["meta"].get("state", {}).get("state")
        if job["meta"].get("state", {}).get("error"):
            st_str += "\nERROR:"
            st_str += job["meta"].get("state", {}).get("error")
        return st_str

    def _get_warn(self, job):
        if job["items"].get("warnings"):
            if not isinstance(job["items"].get("warnings"), Mapping):
                warns = self.item.get(job["items"].get("warnings"))["data"]
            else:
                warns = job["items"].get("warnings")["data"]
            if warns["warning_text"]:
                return "\n".join(warns["warning_text"])
            else:
                return ""
        else:
            return ""

    def print_batch_progress(self, batch_name: str):
        batch = self.get_batch(batch_name)
        for case_name, job in batch["sets"].items():
            print(case_name, self._get_progress(job))

    def print_batch_state(self, batch_name: str):
        batch = self.get_batch(batch_name)
        for case_name, job in batch["sets"].items():
            print(case_name, self._get_state(job))

    def print_batch_warnings(self, batch_name: str):
        batch = self.get_batch(batch_name)
        for case_name, job in batch["sets"].items():
            print(case_name, self._get_warn(job))

    def print_batch_case_info(self, batch_name: str):
        batch = self.get_batch(batch_name)
        for case_name, job in batch["sets"].items():
            print(case_name, self._get_state(job))
            print(self._get_progress(job))
            print(self._get_warn(job))
