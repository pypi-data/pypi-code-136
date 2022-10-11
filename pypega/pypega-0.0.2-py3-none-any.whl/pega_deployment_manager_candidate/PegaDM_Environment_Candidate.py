from PegaDM_Environment import Environment
from PegaDM_Environment_Candidate_Endpoints import *
from PegaDM_Environment_Candidate_OutputStrings import *
import json


class Candidate(Environment):
    def __init__(self, system_name, environment_url, production_level):
        Environment.__production_level = production_level
        Environment.__init__(self, system_name, environment_url)

    def get_application(self, application_name: str, application_version: str):
        response = self.api_request_get(
            API_ENDPOINT_CANDIDATE_GET_APPLICATION.format(
                appName=application_name, appVersion=application_version
            )
        )
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def get_ruleset(self, ruleset_name: str, ruleset_version: str):
        response = self.api_request_get(
            API_ENDPOINT_CANDIDATE_GET_RULESET.format(
                ruleset_name=ruleset_name, ruleset_version=ruleset_version
            )
        )
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def create_ruleset(self, ruleset_name: str, ruleset_version: str):
        response = self.api_request_post(
            API_ENDPOINT_CANDIDATE_CREATE_RULESET.format(
                ruleset_name=ruleset_name, ruleset_version=ruleset_version
            ),
            "",
        )
        return response.ok

    def increase_ruleset_patch_version(self, ruleset_name: str):
        response = self.api_request_get(API_ENDPOINT_CANDIDATE_CREATE_RULESET)
        return response.ok

    def increase_ruleset_minor_version(self, ruleset_name: str):
        response = self.api_request_get(API_ENDPOINT_CANDIDATE_CREATE_RULESET)
        return response.ok
