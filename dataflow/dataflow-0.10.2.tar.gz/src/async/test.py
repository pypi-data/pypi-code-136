import glob
import inspect
import os
from concurrent.futures import ThreadPoolExecutor

from sdm.core.jobs import LocalJob
from sdm.core.operators import DONE, CoroutineOP, op_decorator
from sdm.core.workflows import Workflow, wf_decorator

operator = op_decorator(CoroutineOP)


@operator
def list_folder(folder):
    return glob.glob(folder + "/*")


@operator
def loop_files(file_list):
    for filename in file_list:
        yield filename


@operator
def get_size(filename):
    return os.path.getsize(filename)


@op_decorator(CoroutineOP)
def output(data):
    return data


class ThreadWF(Workflow):
    def __init__(self):
        self.op = {"output": output()}
        super().__init__()
        self.executor = ThreadPoolExecutor(max_workers=5)

    def run(self):
        self._dag.run()

    def send(self, op, data):
        self.op[op].send(data)

    def done(self):
        self._dag.send(DONE)

    @property
    def result(self):
        return self.output.output

    @property
    def output(self):
        return self.op["output"]


workflow = wf_decorator(wf_class=ThreadWF)


@workflow
def scan(wf):
    files = list_folder()
    loop = loop_files()
    size = get_size()
    wf >> files >> loop >> size >> wf.output

    wf.op["folder"] = files

    # better idea
    # wf["folder"] >> files >> size >> wf["scan"]


job = LocalJob()
job.workflow = scan()
job.submit()
job.send("folder", "/home/gjover/workspace/sdm/sdm-core/sdm/async/")
job.done()
