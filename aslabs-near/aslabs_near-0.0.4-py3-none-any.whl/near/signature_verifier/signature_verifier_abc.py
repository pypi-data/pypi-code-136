from abc import ABC, abstractmethod

from .models import VerificationResult


class SignatureVerifierABC(ABC):
    @abstractmethod
    def verify(self,
               account_id,
               public_key,
               message,
               signature,
               domain=None) -> VerificationResult:
        raise NotImplementedError()
