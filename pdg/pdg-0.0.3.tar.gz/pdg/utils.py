"""
Utilities for PDG API.
"""

def parse_id(pdgid):
    """Parse PDG Identifier and return (normalized base identifier, edition)."""
    try:
        baseid, edition = pdgid.split('/')
    except:
        baseid = pdgid
        edition = None
    return (baseid.upper(), edition)


def base_id(pdgid):
    """Return normalized base part of PDG Identifier."""
    return parse_id(pdgid)[0]
