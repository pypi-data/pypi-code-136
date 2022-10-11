# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/crypto/multisig/v1beta1/multisig.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class MultiSignature(betterproto.Message):
    """
    MultiSignature wraps the signatures from a multisig.LegacyAminoPubKey. See
    cosmos.tx.v1betata1.ModeInfo.Multi for how to specify which signers signed
    and with which modes.
    """

    signatures: List[bytes] = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class CompactBitArray(betterproto.Message):
    """
    CompactBitArray is an implementation of a space efficient bit array. This
    is used to ensure that the encoded data takes up a minimal amount of space
    after proto encoding. This is not thread safe, and is not intended for
    concurrent usage.
    """

    extra_bits_stored: int = betterproto.uint32_field(1)
    elems: bytes = betterproto.bytes_field(2)
