import logging

from .batch_rpc_provider import BatchRpcProvider, BatchRpcException
from .utils import binary_history_check

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def check_address_availability(p: BatchRpcProvider, addr):
    latest_block = await p.get_latest_block()

    chain_id = await p.get_chain_id()

    async def check(current_block):
        try:
            logger.info(f"Checking block {current_block}")
            balance = await p.get_balance(addr, f"0x{current_block:x}")
            logger.info(f"Balance at block {current_block} is {balance}")
            return True
        except BatchRpcException:
            return False

    min_succeeded_block = await binary_history_check(-1, latest_block, check)
    return min_succeeded_block, latest_block - min_succeeded_block
