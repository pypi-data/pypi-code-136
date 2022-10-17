from dataclasses import dataclass
from dateutil import parser as date_parser
from typing import Optional
from aslabs.utils.dataclasses import parse


@dataclass
class NftContractMetadata:
    spec: str
    name: str
    symbol: str
    icon: Optional[str]
    base_uri: Optional[str]
    reference: Optional[str]
    reference_hash: Optional[str]


@dataclass
class TokenMetadata:
    title: Optional[str]
    description: Optional[str]
    media: Optional[str]
    media_hash: Optional[str]
    copies: Optional[int]
    issued_at: Optional[int]
    expires_at: Optional[int]
    starts_at: Optional[int]
    updated_at: Optional[int]
    extra: Optional[str]
    reference: Optional[str]
    reference_hash: Optional[str]

    @classmethod
    def from_dict(cls, d):
        if (issued_at := d.get("issued_at")) is not None:
            try:
                dt = date_parser.parse(issued_at)
                d["issued_at"] = int(dt.timestamp() * 1000)
            except ValueError:
                pass
            except TypeError:
                pass
            except OverflowError:
                pass
            except Exception:
                raise

        if (expires_at := d.get("expires_at")) is not None:
            try:
                dt = date_parser.parse(expires_at)
                d["expires_at"] = int(dt.timestamp() * 1000)
            except ValueError:
                pass
            except OverflowError:
                pass
            except TypeError:
                pass

        if (starts_at := d.get("starts_at")) is not None:
            try:
                dt = date_parser.parse(starts_at)
                d["starts_at"] = int(dt.timestamp() * 1000)
            except ValueError:
                pass
            except OverflowError:
                pass
            except TypeError:
                pass

        if (updated_at := d.get("updated_at")) is not None:
            try:
                dt = date_parser.parse(updated_at)
                d["updated_at"] = int(dt.timestamp() * 1000)
            except ValueError:
                pass
            except OverflowError:
                pass
            except TypeError:
                pass

        return parse(cls, d)


@dataclass
class Token:
    token_id: str
    owner_id: str
    metadata: Optional[TokenMetadata]
    approved_account_ids: Optional[dict[str, int]]

    @classmethod
    def from_dict(cls, d):
        return cls(
            token_id=str(d["token_id"]),
            owner_id=str(d["owner_id"]),
            metadata=(m := d.get("metadata")) and TokenMetadata.from_dict(m),
            approved_account_ids=(a := d.get(
                "approved_account_ids")) and dict(a)
        )
