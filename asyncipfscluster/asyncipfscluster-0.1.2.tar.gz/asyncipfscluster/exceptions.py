"""File containing exceptions."""


class IPFSException(Exception):
    """Exception related to IPFS."""


class InvalidCIDException(IPFSException):
    """Invalid CID."""
