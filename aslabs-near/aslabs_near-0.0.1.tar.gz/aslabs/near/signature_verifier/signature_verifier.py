import ed25519
import base58
import requests
from typing import Optional
from ..models import KeyInfo, VerificationResult
from ..config import NearRpcConfig
from .signature_verifier_abc import SignatureVerifierABC


def base58_to_hex(base58_string):
    return hex(int.from_bytes(base58.b58decode(base58_string), byteorder="big"))[2:].zfill(64).encode("ascii")


class UserKeyFetcher:
    def __init__(self, rpc_endpoint: str):
        self._rpc_endpoint = rpc_endpoint

    def get_user_key(self, account_id: str, public_key: str) -> Optional[KeyInfo]:
        result = requests.post(
            self._rpc_endpoint,
            json={
                "jsonrpc": "2.0",
                "id": "myid",
                "method": "query",
                "params": {
                    "request_type": "view_access_key_list",
                    "finality": "final",
                    "account_id": account_id
                }
            })
        keys = result.json()["result"]["keys"]
        for key in keys:
            if key["public_key"] == public_key:
                return KeyInfo.from_key(key)
        return None


class SignatureVerifier(SignatureVerifierABC):
    def __init__(self, rpc_endpoint: str):
        self._key_fetcher = UserKeyFetcher(rpc_endpoint)

    def _verify_signature(self, public_key, signature, message):
        assert public_key.startswith("ed25519:")

        try:
            pubKey = ed25519.VerifyingKey(base58_to_hex(
                public_key[8:].encode("ascii")), encoding="hex")

            pubKey.verify(signature, message, encoding='hex')
            return True
        except Exception:
            return False

    def _verify_account_own_public_key(self, account_id, public_key, domain=None) -> VerificationResult:
        key_info = self._key_fetcher.get_user_key(account_id, public_key)

        if key_info and (domain is None or key_info.receiver_id == domain):
            return VerificationResult.with_key_info(key_info)
        return VerificationResult.failed

    def verify(self,
               account_id,
               public_key,
               message,
               signature,
               domain=None) -> VerificationResult:
        sig_valid = self._verify_signature(
            public_key,
            signature.encode("ascii"),
            message.encode("ascii"))

        if not sig_valid:
            return VerificationResult.failed

        return self._verify_account_own_public_key(
            account_id,
            public_key,
            domain=domain)
