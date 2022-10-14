from hashflow.factory import Factory
from hashflow.router import Router
from hashflow.governance import Governance
from hashflow.erc20 import ERC20
from hashflow.pool import Pool
from hashflow.executor import Executor


class Hashflow(object):
    def __init__(
        self,
        private_key: str | bytearray,
        network_id: int,
        jsonRpcUrl: str | None = None,
    ):

        self.executor = Executor(jsonRpcUrl, private_key)
        self.contracts = Contracts(self.executor, network_id)
        self.erc20 = ERC20(self.executor, network_id)
        self.pool = Pool(self.executor)


class Contracts(object):
    def __init__(
        self,
        executor: Executor,
        chain_id: int,
    ):
        self.factory = Factory(executor, chain_id)
        self.router = Router(executor, chain_id)
        self.governance = Governance(executor, chain_id)
        self.chain_id = chain_id
