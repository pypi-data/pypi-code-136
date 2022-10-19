import inspect
from concurrent.futures import ThreadPoolExecutor

from sdm.core.operators import DONE, Operator

form sdm.core.workflows import Workflow

class ThreadWF(Workflow):

    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=5)

    def send(self, operation, data):
        return self.executor.submit(operation.send, data))


class CoroutineOP(Operator):

    def __init__(self):
        super().__init__()
        self._coro = self._coroutine()

    def _coroutine(self):
        while True:
            try:
                invalue = yield
                if invalue is DONE:
                    break
                outvalue = self.operation(input)
                if self.downstream:
                    for op in self.downstream:
                        self.workflow.send(op, outvalue)
                else:
                    self.returns.append(outvalue)
            except StopIteration as e:
                # Retrieve return value from the operator
                self.returns.append(e.value)
            except GeneratorExit:
                # close command received
                raise
        return self.returns

    def run(self):
        next(self._coro)

    def close(self):
        self._coro.close()

    def send(self, value):
        self._coro.send(value)
