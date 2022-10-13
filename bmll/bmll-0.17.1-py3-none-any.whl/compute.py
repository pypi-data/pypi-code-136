""" Interface to the Compute service.
"""

import pandas as pd
from typeguard import typechecked, Union

from bmll._rest import DEFAULT_SESSION
from bmll._clusters import core, validation
from bmll._clusters.components import ClusterConfig, Cluster, _get_clusters
from bmll._clusters.exceptions import InvalidArgumentError, ClusterException
from bmll._clusters.core import JobType, Area, NodeType, JobFailureAction, ClusterState


__all__ = (
    # HTTP interface
    'ComputeClient',

    # Clusters API
    'get_clusters',
    'ClusterConfig',
    'create_cluster',
    'NodeType',
    'Area',
    'JobType',
    'JobFailureAction',
    'ClusterException',
    'InvalidArgumentError',
    'ClusterState',
)


class ComputeClient:
    """
    The ComputeClient provides a convenient interface to interact with the BMLL Compute API.

    Args:
        session: :class:`bmll.Session`, optional
            if provided use this session object to communicate with the API, else use the default session.

            Note: this must be a session authenticated by the Lab Auth service.
    """

    def __init__(self, session=None):
        self._session = session or DEFAULT_SESSION
        core.SESSION = self._session

    @typechecked
    def create_cluster(
        self, name: str = None, log_path: str = None, log_area: str = 'user',
        node_type: str = NodeType.CPU, node_count: int = 1,
        cluster_config: ClusterConfig = None, spot_pricing: bool = False,
        terminate_on_idle: bool = True,
        cluster_bootstraps: Union[list, dict] = None,
        tags: dict = None
    ):
        """Create a cluster and return a :class:`Cluster <bmll._clusters.Cluster>`
        object to manage it.

        This is the first step in using /_clusters, which allow parallel computation
        at scale. There may be a delay between running the command and the cluster
        becoming active.  The status of the cluster can be checked with
        :class:`Cluster.status <bmll._clusters.Cluster.status>`
        or on the `_clusters </#app/clusters>`_ page of the BMLL site.

        This can be called without constructing a ComputeClient via `bmll.compute.create_cluster()`.
        In this case, a default ComputeClient instance is used.

        Note: You can add a default bootstrap script to your 'user' remote storage area
        that will be run when starting either a workspace or cluster.  The script must
        be named `default_bootstrap.sh` and stored in the base of your 'user' area.

        Note: the `node_type` and `spot_pricing` parameters only apply to the worker ("core")
        nodes of the cluster. The master node is chosen to be a fixed type (an `m4.large`
        instance) and it is not created in the spot-price market. The core nodes are `r4.16xlarge`
        instances. For more details on instance types, please see
        https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-supported-instance-types.html

        Args:
            name: str (optional)
                The name given to the cluster.
                The default is None, meaning created from username and timestamp.

            log_path: str (optional)
                Where to put the log files.
                The default is the cluster name.

            log_area: str (optional)
                The area to store the logs.
                Possible values are :class:`Area <bmll._clusters.core.Area>`
                The default is 'user'.

            node_type: str (optional)
                The type of processor provisioned on the nodes of the cluster.
                Possible values are :class:`NodeType <bmll._clusters.core.NodeType>`
                The default is 'cpu'.

            node_count: int (optional)
                The number of core nodes to create within the cluster.
                The default is 1

            cluster_config: :class:`ClusterConfig` (optional)
                Configuration settings for the cluster.
                The default is None, meaning the default :class:`ClusterConfig`

            spot_pricing: bool (optional)
                If True, create a cluster with spot pricing, otherwise use on demand.
                The default is False.

                This parameter is for backwards compatibility; using False gives
                better reliability in cluster nodes.

            terminate_on_idle: bool (optional)
                If True, the cluster will terminate as soon as it is idle. Note that if this option
                is set to True and no jobs are submitted to the cluster, then the cluster will
                immediately terminate.
                The default is True

            cluster_bootstraps: list(dict) or dict (optional)
                If not none, create a cluster with user specified bootstraps.  Each dictionary
                must specify the `path` of the bootstrap script.  The optional keys of the dictionary
                are `area`, `args`, and `name`, where `area` is the remote storage area the script is
                located (either 'user' or 'organisation'), `args` are a list of arguments to pass with
                the script, and `name` is the name given to the bootstrap for personal reference.

            tags: dict (optional)
                Optional tags to add to the cluster.  The dictionary `tags` must have string values
                for both keys and values.

        Returns:
            :class:`Cluster <bmll._clusters.Cluster>`
                The object through which the cluster is managed.

        See Also:
            * :class:`ClusterConfig`
        """
        if log_area not in Area:
            raise InvalidArgumentError(log_area, 'log_area', Area)

        if node_type not in NodeType:
            raise InvalidArgumentError(node_type, 'node_type', NodeType)

        if node_count < 1:
            raise ValueError('node_count must be a positive int, not {!r}.'.format(node_count))

        if cluster_config is None:
            cluster_config = ClusterConfig()
        cluster_settings = cluster_config.cluster_settings

        if name is None:
            username = getattr(self._session, "_USERNAME", "(unavailable)")
            name = f"{username}-{pd.Timestamp.now().round('s')}"

        if log_path is None:
            log_path = name

        if tags is not None:
            if 'task_id' in tags.keys():
                raise ValueError('task_id is a BMLL reserved key name.')

        if cluster_bootstraps is not None and isinstance(cluster_bootstraps, dict):
            cluster_bootstraps = [cluster_bootstraps]

        if cluster_bootstraps is not None:
            validation.check_bootstrap_format(cluster_bootstraps)

        return Cluster(name=name, node_type=node_type, node_count=node_count,
                       log_area=log_area, log_path=log_path, cluster_settings=cluster_settings,
                       spot_pricing=spot_pricing, terminate_on_idle=terminate_on_idle,
                       cluster_bootstraps=cluster_bootstraps,
                       tags=tags
                       )

    @staticmethod
    @typechecked
    def get_clusters(
        active_only: bool = True, max_n_clusters: int = 10,
        include_organisation: bool = False, tags: dict = None
    ):
        """
        Get a :class:`ClusterCollection <bmll._clusters.ClusterCollection>`
        of the max_n_clusters most recent _clusters.

        This can be called without constructing a ComputeClient via `bmll.compute.get_clusters()`.
        In this case, a default ComputeClient instance is used.

        Args:
            active_only: bool, default True
                Only show active _clusters.

            max_n_clusters: int, default 10
                Maximum number of most recent _clusters to retrieve.

            include_organisation: bool, optional
                If True will also return organisation level _clusters (for example Scheduling Service).
                The default is False.

        Returns:
            :class:`ClusterCollection <bmll._clusters.ClusterCollection>`
                Object representing a collection _clusters.

        See Also:
            * :class:`Cluster <bmll._clusters.Cluster>`
        """
        return _get_clusters(
            active_only=active_only, max_n_clusters=max_n_clusters,
            include_organisation=include_organisation, tags=tags,
        )


# we setup a default client and session so that users can still call
# bmll.compute.get_clusters() etc.

_DEFAULT_CLIENT = ComputeClient()
create_cluster = _DEFAULT_CLIENT.create_cluster
get_clusters = _DEFAULT_CLIENT.get_clusters
