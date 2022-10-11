import requests
import json

class WithMake:
    def __init__(self, token, region):
        self.token = token
        self.region = region
        self.base_url = f"https://{region}.make.com/api/v2/"

    def getScenario(self, scenarioId):
        url = self.base_url + f"scenarios/{scenarioId}"
        headers = {"Authorization": f"Token {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def getBlueprint(self, scenario_id, blueprintId=None, draft=False):
        url = self.base_url + f"scenarios/{scenario_id}/blueprint"
        headers = {"Authorization": f"Token {self.token}"}

        params = {}
        if blueprintId:
            params["blueprintId"] = blueprintId
        if draft:
            params["draft"] = draft

        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def cloneScenario(self, scenarioId, organizationId, name, teamId, states=False):
        url = self.base_url + f"scenarios/{scenarioId}/clone"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {self.token}"}
        params = {"organizationId": organizationId}
        data = json.dumps({
            "name": name,
            "teamId": teamId,
            "states": states
        })
        response = requests.post(url, headers=headers, params=params, data=data)
        return response.json()

    def updateScenario(self, scenarioId, blueprint, name):
        url = self.base_url + f"scenarios/{scenarioId}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {self.token}"}
        data = json.dumps({
            "blueprint": json.dumps(blueprint),
            "name": name
        })
        response = requests.patch(url, headers=headers, data=data)
        return response.json()

    def startScenario(self, scenarioId):
        url = self.base_url + f"scenarios/{scenarioId}/start"
        headers = {"Authorization": f"Token {self.token}"}
        response = requests.post(url, headers=headers)
        return response.json()