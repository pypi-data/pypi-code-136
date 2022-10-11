from typing import *
from distributed import Client
import random


class DagNode:
    def __init__(
        self,
        client: Client,
        cb: Callable,
        name: str = None,
        parent: Optional["DagNode"] = None,
    ):
        self.client = client
        self._parent: Optional[DagNode] = parent
        self.cb = cb
        self.name = name or f"{cb.__name__}-{random.randint(0, 1_000_000)}"

        print(self)

    def result(self):
        return self._result().result()

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, val: "DagNode"):
        assert self._parent is None
        self._parent = val

    def __repr__(self):
        return f"{self.name} - cb={self.cb.__name__}, parent={self.parent.name if self.parent else '<NA>'}"

    def __or__(self, other) -> "DagNode":
        if isinstance(other, DagNode):
            other.parent = self
        elif isinstance(other, Callable):
            other = DagNode(self.client, other, parent=self)
        else:
            raise NotImplemented(f"Method not implemented for type {type(other)}")

        return other

    def __rshift__(self, name: str):
        self.name = name
        return self

    def _result(self):
        if self.parent and self.parent.cb.__name__ != self._nop.__name__:
            parent_result = self.parent._result()
            return self.client.submit(self.cb, parent_result)
        else:
            return self.client.submit(self.cb)

    @staticmethod
    def _nop():
        pass

    @classmethod
    def from_client(cls: "DagNode", client: Client) -> "DagNode":
        return DagNode(client, cls._nop, "DAG ROOT")


if __name__ == "__main__":
    from distributed import LocalCluster
    import logging

    logging.basicConfig(level=logging.DEBUG)

    cluster = LocalCluster()
    client = Client(cluster)

    dag = DagNode.from_client(client) | random.random | round
    dag_x2 = dag | (lambda x: x * 2)
    print("Dag result: ", dag.result())
    print("Dag2 result: ", dag_x2.result())
