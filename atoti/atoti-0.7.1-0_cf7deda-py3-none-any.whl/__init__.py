import sys

from atoti_core import BaseSession, activate_plugins, get_env_flag

# pylint: disable=wrong-import-position
from ._runtime_type_checking_utils import _instrument_typechecking, typecheck

# This needs to be done here so that the runtime type checking decoration can be done before evaluating any classes inheriting from `BaseSession`.
# Otherwise the monkey-patching mechanism used by plugins will target the incorrect method references.
typecheck(BaseSession)

from atoti_query import (
    Auth as Auth,
    BasicAuthentication as BasicAuthentication,
    ClientCertificate as ClientCertificate,
    OAuth2ResourceOwnerPasswordAuthentication as OAuth2ResourceOwnerPasswordAuthentication,
    QueryCube as QueryCube,
    QueryHierarchy as QueryHierarchy,
    QueryLevel as QueryLevel,
    QueryMeasure as QueryMeasure,
    QueryResult as QueryResult,
    QuerySession as QuerySession,
    TokenAuthentication as TokenAuthentication,
)

from . import (  # pylint: disable=redefined-builtin
    agg as agg,
    array as array,
    experimental as experimental,
    math as math,
    scope as scope,
    string as string,
    type as type,
)
from ._eula import (
    EULA as __license__,
    hide_new_eula_message as hide_new_eula_message,
    hide_new_license_agreement_message as hide_new_license_agreement_message,
    print_eula_message,
)
from ._py4j_utils import patch_databricks_py4j
from ._telemetry import telemeter
from .aggregate_provider import AggregateProvider as AggregateProvider
from .client_side_encryption_config import *
from .column import *
from .config import *
from .copy_tutorial import *
from .cube import Cube as Cube
from .directquery import *
from .function import *
from .hierarchy import *
from .level import *
from .measure import *
from .order import *

# Replace imported symbols with `*` once the deprecated scope factory functions are removed.
from .scope import (
    CumulativeScope as CumulativeScope,
    OriginScope as OriginScope,
    SiblingsScope as SiblingsScope,
)
from .session import Session as Session, _sessions as sessions
from .table import Table as Table
from .type import *

# pylint: enable=wrong-import-position

print_eula_message()


def close() -> None:
    """Close all opened sessions."""
    sessions.close()


activate_plugins()

if not get_env_flag("DISABLE_RUNTIME_TYPECHECKING"):
    _instrument_typechecking(sys.modules[__name__])

patch_databricks_py4j()
telemeter()
