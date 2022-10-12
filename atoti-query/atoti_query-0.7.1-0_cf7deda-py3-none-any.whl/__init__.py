"""There are two main ways to query remote atoti sessions (or classic ActivePivot >= 5.7 servers):

* by passing measures and levels to :meth:`atoti_query.QueryCube.query`
* by passing an MDX string to :meth:`atoti_query.QuerySession.query_mdx`
"""

from ._execute_gaq import _ExecuteGaq as _ExecuteGaq
from ._query_mdx import _QueryMdx as _QueryMdx
from .auth import *
from .basic_authentication import *
from .client_certificate import *
from .oauth2_resource_owner_password_authentication import *
from .query_cube import *
from .query_cubes import *
from .query_hierarchies import *
from .query_hierarchy import *
from .query_level import *
from .query_levels import *
from .query_measure import *
from .query_measures import *
from .query_result import *
from .query_session import *
from .token_authentication import *
