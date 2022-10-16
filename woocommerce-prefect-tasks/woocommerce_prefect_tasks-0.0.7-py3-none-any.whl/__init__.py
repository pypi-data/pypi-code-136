"""
Tasks for interacting with WooCommerce.
"""
try:
    from woocommerce.api import *
    from .aws import SecretsManagerClient, SecretsManagerStorage
    from .tasks import Create, Get, Update, Delete, Options
except ImportError:
    raise ImportError(
        'Using `prefect.tasks.woocommerce_prefect_tasks` requires Prefect to be installed with the "woocommerce" extra.'
    )
