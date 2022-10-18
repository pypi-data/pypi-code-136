import sys
from functools import cached_property

from jira import JIRA

from git_jira.config import Config
from git_jira.utils import singleton


# TODO: username/token tuple Only valid for Jira Cloud
# We need to support self hosted Jira, where auth is done with
# token auth, with the PAT token: token_auth="API token"
@singleton
class Jira:
    def __init__(self):
        self.config = Config().jira

    @cached_property
    def jira(self):
        return JIRA(
            self.config["server_url"],
            basic_auth=(self.config["username"], self.config["api_token"]),
        )
        
class JiraProject:
    def __init__(self, project_code=None):
        self.project_code = (
            self.project_code if project_code else Jira().config["default_project_key"]
        )

    def get_issues(self, status='Planned'):
        """
        Get issues from project. Do not get Epics.
        #TODO Return up to 25 ordered by date?
        """
        return [JiraIssue(issue_key=i.raw['key']) for i in Jira().jira.search_issues(f"project = {self.project_code} AND status = '{status}' AND type != Epic")]


class JiraMetaIssue:
    def __init__(self, project_code=None):
        self.project_code = (
            self.project_code if project_code else Jira().config["default_project_key"]
        )
        self.meta_issue = [p for p in Jira().jira.createmeta(expand='projects.issuetypes.fields')['projects'] if p['key'] == self.project_code][0]
        self.issue_type_names = [issue['name'] for issue in self.meta_issue['issuetypes']]
    
    def available_fields(self, issue_type):
        fields = [i['fields'] for i in self.meta_issue['issuetypes'] if i['name'] == issue_type][0]
        fields_metadata = list()
        for field_key in fields.keys():
            field = fields[field_key]
            field_metadata = dict()
            field_metadata["key"] = field_key
            field_metadata["name"] = field["name"]
            field_metadata["required"] = field["required"]
            field_metadata["type"] = field["schema"]["type"]
            if field_metadata["type"] in ["option", "array"]:
            #Some arrays can have empty options (no key allowedvalues)
                try:
                    field_metadata["options"] = [{"value":opt["value"], "id":opt["id"]} for opt in field["allowedValues"]]
                except:
                    field_metadata["options"] = None
            fields_metadata.append(field_metadata)
        return fields_metadata

    def required_fields(self, issue_type):
        return [field for field in self.available_fields(issue_type) if field['required']]

class JiraIssue:
    def __init__(self, input_fields=None, issue_key = None):
        if input_fields:
            self.issue = Jira().jira.create_issue(input_fields)
            self.key = self.issue.key
            self.type = input_fields["issuetype"]["name"]
            self.summary = self.issue.fields.summary
            self.url = f"{Jira().config['server_url']}/browse/{self.issue.key}"
        if issue_key:
            try:
                self.issue = Jira().jira.issue(issue_key)
                self.key = self.issue.key
                self.type = self.issue.fields.issuetype.name
                self.summary = self.issue.fields.summary
                self.url = f"{Jira().config['server_url']}/browse/{self.issue.key}"
                self.status = self.issue.fields.status.name
                self.available_statuses = [{"display_name":status['to']['name'], "name":status['name']} for status in Jira().jira.transitions(self.issue) if status['isAvailable'] and status['to']['name'] != self.status]
                try:
                    self.assignee = self.issue.fields.assignee.displayName
                except:
                    self.assignee = 'Unassigned'
            except Exception as e:
                print(e.text)
                sys.exit(1)
