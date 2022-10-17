from dataclasses import dataclass
from typing import Generator, Optional
import requests
import json
import base64
from aslabs.utils import retriable
from aslabs.utils.dataclasses import parse
from concurrent.futures import ThreadPoolExecutor
from .config import NearRpcConfig
from .models.nft import Token, NftContractMetadata

class RpcException(Exception):
    pass


class NearNft:
    def __init__(self, config: NearRpcConfig) -> None:
        self._config = config

    @retriable(exceptions=(ConnectionError, requests.JSONDecodeError, requests.exceptions.ConnectionError))
    def _rpc_query(self, query):
        resp = requests.post(
            self._config.provider_url,
            json={
                "method": "query",
                "params": query,
                "id": "fuckoff",
                "jsonrpc": "2.0"
            })

        rpc_raw = resp.json()
        rpc_result = rpc_raw["result"]

        if "error" in rpc_result:
            raise RpcException(rpc_result["error"])

        data = rpc_result["result"]
        return json.loads(''.join([chr(x) for x in data]))

    def _view_function(self, contract_id, method_name, args={}, finality="optimistic"):
        return self._rpc_query({
            "request_type": "call_function",
            "account_id": contract_id,
            "method_name": method_name,
            "args_base64": base64.b64encode(json.dumps(args).encode('utf8')).decode('utf8'),
            "finality": finality
        })

    def nft_token(self, contract_id: str, token_id: str):
        token = self._view_function(contract_id, "nft_token", {"token_id": token_id})
        if token is None:
            return None
        return Token.from_dict(token)

    def nft_supply_for_owner(self, contract_id: str, account_id: str):
        return int(self._view_function(contract_id, "nft_supply_for_owner", {"account_id": account_id}))

    def nft_metadata(self, contract_id):
        return parse(NftContractMetadata, self._view_function(contract_id, "nft_metadata"))

    def nft_tokens(self, contract_id: str, from_index: str, limit: Optional[int]) -> list[Token]:
        return list(map(
            lambda a: Token.from_dict(a),
            self._view_function(contract_id, "nft_tokens", {"from_index": from_index, "limit": limit})))

    def nft_total_supply(self, contract_id: str) -> int:
        return int(self._view_function(contract_id, "nft_total_supply"))

    def get_all_nft_tokens(
            self,
            contract_id: str,
            initial_index: int = 0,
            default_step: int = 64) -> Generator[Token, None, None]:
        total_supply = self.nft_total_supply(contract_id)
        index = initial_index
        step = default_step
        while index < total_supply:
            try:
                tokens = self.nft_tokens(contract_id, str(index), step)
                yield from tokens
                index += step
            except RpcException:
                if step > 1:
                    step = step // 2
                else:
                    raise

    def get_all_tokens_naive(self, contract_id: str) -> Generator[Token, None, None]:
        total_supply = self.nft_total_supply(contract_id)
        i = 0
        count = 0
        while count < total_supply:
            try:
                yield self.nft_token(contract_id, str(i))
                count += 1
            except AttributeError:
                pass
            finally:
                i += 1

    def enumerate_tokens(self, contract_id: str, tokens_per_partition: int = 128) -> list[Token]:
        total_supply = self.nft_total_supply(contract_id)

        def _enumerate_partition(start_index, partition_size):
            if partition_size > 1:
                try:
                    return self.nft_tokens(contract_id, str(start_index), partition_size)
                except RpcException:
                    half = partition_size // 2
                    return [
                        *_enumerate_partition(start_index, half),
                        *_enumerate_partition(start_index + half, partition_size - half)
                    ]

            # Naive fetching
            return [self.nft_token(contract_id, str(start_index))]

        with ThreadPoolExecutor(max_workers=12) as pool:
            futures = [
                pool.submit(_enumerate_partition, i, tokens_per_partition)
                for i in range(0, total_supply, tokens_per_partition)
            ]
            result = [future.result() for future in futures]
        return [r for rs in result for r in rs]

    def get_tokens_in_collection(self, contract_id: str, token_ids: list[str]) -> list[Token]:
        def _get_token(token_id):
            return self.nft_token(contract_id, token_id)

        with ThreadPoolExecutor(max_workers=12) as pool:
            futures = [
                pool.submit(_get_token, token_id)
                for token_id in token_ids
            ]
            result = [future.result() for future in futures]
        return [r for r in result]
