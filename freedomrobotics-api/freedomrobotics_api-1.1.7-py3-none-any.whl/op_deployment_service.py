import json
from .entity import Entity

url_base = '/accounts/{}/op-deployment-services'


class OPDeploymentService(Entity):
    pk = 'id'

    @property
    def url_base(self):
        return url_base.format(self.account_id)

    @property
    def account_id(self):
        """str: Account id.
        """
        return self._data.get("account_id")

    @property
    def name(self):
        """str: Zone name.
        """
        return self._data.get("name")

    @property
    def configuration(self):
        """dict: Deployment-service configuration.
        """
        return self._data.get("configuration")


def get_opdeployment_services(
        api,
        account_id,
        opdeployment_id=None,
        attributes=None,
        params=None,
        raw=False,
        api_call_kwargs={},
):
    """:obj:`list` : Fetch a list of deployment-services for an account or a deployment.

    Args:
        api (ApiHandler): Api handler object.
        account_id (str): Account ID.
        opdeployment_id (str): Optional on prem deployment ID.
        attributes (list): Optional list of deployment-service attributes to return.
        params (dict): Optional query parameters.
        raw (bool): Will return the raw JSON if True. False by default.
        api_call_kwargs (dict): Optional keyword arguments for api call.
        **kwargs: Extra keyword arguments passed to Alert object.
    """
    if params is None:
        params = {}
    if attributes is not None:
        params["attributes"] = json.dumps(attributes)
    if opdeployment_id is not None:
        params['opdeployment_id'] = opdeployment_id

    path = url_base.format(account_id)

    deployment_services_data = api.call("GET", path, params=params, **api_call_kwargs)
    if not deployment_services_data:
        return []
    if raw:
        deployment_services = deployment_services_data
    else:
        deployment_services = [
            OPDeploymentService(ds_data["id"], ds_data) for ds_data in deployment_services_data
        ]
    return deployment_services
