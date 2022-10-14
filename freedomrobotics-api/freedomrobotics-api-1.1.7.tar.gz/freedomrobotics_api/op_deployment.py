from .entity import Entity
from .op_deployment_service import get_opdeployment_services

url_base = '/accounts/{}/op-deployments'


class OPDeployment(Entity):
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
        """str: Service name.
        """
        return self._data.get("name")

    def get_opdeployment_services(self, attributes=None, params=None, raw=False, api_call_kwargs={}):
        """:obj:`list` of :obj:`OPDeploymentService`: Fetch a list of on prem deployment services for the deployment,
         according to the used params

        Args:
            attributes (list): Optional list of attributes to request.
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        return get_opdeployment_services(
            self.api,
            self.account_id,
            opdeployment_id=self._id,
            attributes=attributes,
            params=params,
            raw=raw,
            api_call_kwargs=api_call_kwargs)


def get_opdeployment(api, account_id, opdeployment_id, params=None, raw=False, api_call_kwargs={}):
    """:obj:`OPDeployment`: Returns a deployment by its ID.

    Args:
        api (ApiHandler): Api handler object.
        account_id (str): Account ID.
        opdeployment_id (string): ID of the on prem deployment
        params (dict): Optional query parameters.
        raw (bool): Will return the raw JSON if True. True by default.
        api_call_kwargs (dict): Optional keyword arguments for api call.
    """
    response = api.call(
        "GET",
        url_base.format(account_id) + '/' + opdeployment_id,
        params=params,
        **api_call_kwargs
    )
    if not response:
        return None
    elif raw:
        return response
    else:
        return OPDeployment(response['id'], response, api=api)
