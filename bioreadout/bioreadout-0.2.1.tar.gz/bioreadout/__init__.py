"""Bio file readers, instrument schema.

Import the package::

   import bioreadout

This is the complete API reference:

.. autosummary::
   :toctree: .

   EFO
   readout
   lookup
"""

__version__ = "0.2.1"

from ._efo import EFO, readout
from ._lookup import lookup
