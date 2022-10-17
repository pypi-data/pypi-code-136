"""Generated implementation of branch."""

# WARNING DO NOT EDIT
# This code was generated from branch.mcn

from __future__ import annotations

import abc  # noqa: F401
import dataclasses  # noqa: F401
import datetime  # noqa: F401
import enum  # noqa: F401
import isodate  # noqa: F401
import json  # noqa: F401
import jsonschema  # noqa: F401
import logging  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
try:
    from anaml_client.utils.serialisation import JsonObject  # noqa: F401
except ImportError:
    pass

from ..commit import Commit, CommitId
from ..user import UserId


@dataclasses.dataclass(frozen=True)
class BranchName:
    """Unique name of a branch.
    
    Args:
        value (str): A data field.
    """
    
    value: str
    
    def __str__(self) -> str:
        """Return a str of the wrapped value."""
        return str(self.value)
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for BranchName data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "string"
        }
    
    @classmethod
    def from_json(cls, data: dict) -> BranchName:
        """Validate and parse JSON data into an instance of BranchName.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of BranchName.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return BranchName(str(data))
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug("Invalid JSON data received while parsing BranchName", exc_info=ex)
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return str(self.value)
    
    @classmethod
    def from_json_key(cls, data: str) -> BranchName:
        """Parse a JSON string such as a dictionary key."""
        return BranchName(str(data))
    
    def to_json_key(self) -> str:
        """Serialise as a JSON string suitable for use as a dictionary key."""
        return str(self.value)


@dataclasses.dataclass(frozen=True)
class BranchRequest:
    """Request to create a new branch.
    
    Args:
        name (str): A data field.
        commit (CommitId): A data field.
    """
    
    name: str
    commit: CommitId
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for BranchRequest data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "commit": CommitId.json_schema()
            },
            "required": [
                "name",
                "commit",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> BranchRequest:
        """Validate and parse JSON data into an instance of BranchRequest.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of BranchRequest.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return BranchRequest(
                name=str(data["name"]),
                commit=CommitId.from_json(data["commit"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing BranchRequest",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "name": str(self.name),
            "commit": self.commit.to_json()
        }


@dataclasses.dataclass(frozen=True)
class BranchUpdateRequest:
    """Request to update a branch to point to a new commit.
    
    Args:
        commit (CommitId): A data field.
        force (typing.Optional[bool]): A data field.
    """
    
    commit: CommitId
    force: typing.Optional[bool]
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for BranchUpdateRequest data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "commit": CommitId.json_schema(),
                "force": {
                    "oneOf": [
                        {"type": "null"},
                        {"type": "boolean"},
                    ]
                }
            },
            "required": [
                "commit",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> BranchUpdateRequest:
        """Validate and parse JSON data into an instance of BranchUpdateRequest.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of BranchUpdateRequest.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return BranchUpdateRequest(
                commit=CommitId.from_json(data["commit"]),
                force=(lambda v: v and bool(v))(data.get("force", None)),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing BranchUpdateRequest",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "commit": self.commit.to_json(),
            "force": (lambda v: v and v)(self.force)
        }


@dataclasses.dataclass(frozen=True)
class BranchStatistics:
    """Branch Statistics.

    Args:
        commitsAhead (int): A data field.
        commitsBehind (int): A data field.
    """
    
    commitsAhead: int
    commitsBehind: int
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for BranchStatistics data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "commitsAhead": {
                    "type": "integer"
                },
                "commitsBehind": {
                    "type": "integer"
                }
            },
            "required": [
                "commitsAhead",
                "commitsBehind",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> BranchStatistics:
        """Validate and parse JSON data into an instance of BranchStatistics.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of BranchStatistics.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return BranchStatistics(
                commitsAhead=int(data["commitsAhead"]),
                commitsBehind=int(data["commitsBehind"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing BranchStatistics",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "commitsAhead": int(self.commitsAhead),
            "commitsBehind": int(self.commitsBehind)
        }


@dataclasses.dataclass(frozen=True)
class Branch:
    """Branch.

    Args:
        name (BranchName): A data field.
        created (typing.Optional[datetime.datetime]): A data field.
        author (typing.Optional[UserId]): A data field.
        head (Commit): A data field.
        statistics (typing.Optional[BranchStatistics]): A data field.
    """
    
    name: BranchName
    created: typing.Optional[datetime.datetime]
    author: typing.Optional[UserId]
    head: Commit
    statistics: typing.Optional[BranchStatistics]
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for Branch data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "name": BranchName.json_schema(),
                "created": {
                    "oneOf": [
                        {"type": "null"},
                        {"type": "string", "format": "date-time"},
                    ]
                },
                "author": {
                    "oneOf": [
                        {"type": "null"},
                        UserId.json_schema(),
                    ]
                },
                "head": Commit.json_schema(),
                "statistics": {
                    "oneOf": [
                        {"type": "null"},
                        BranchStatistics.json_schema(),
                    ]
                }
            },
            "required": [
                "name",
                "head",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> Branch:
        """Validate and parse JSON data into an instance of Branch.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of Branch.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return Branch(
                name=BranchName.from_json(data["name"]),
                created=(lambda v: v and isodate.parse_datetime(v))(data.get("created", None)),
                author=(lambda v: v and UserId.from_json(v))(data.get("author", None)),
                head=Commit.from_json(data["head"]),
                statistics=(
                    lambda v: v and BranchStatistics.from_json(v)
                )(
                    data.get("statistics", None)
                ),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing Branch",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "name": self.name.to_json(),
            "created": (lambda v: v and v.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))(self.created),
            "author": (lambda v: v and v.to_json())(self.author),
            "head": self.head.to_json(),
            "statistics": (lambda v: v and v.to_json())(self.statistics)
        }
