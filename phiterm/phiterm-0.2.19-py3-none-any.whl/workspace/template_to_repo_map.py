from typing import Dict

from phiterm.workspace.ws_enums import WorkspaceStarterTemplate

template_to_repo_map: Dict[WorkspaceStarterTemplate, str] = {
    WorkspaceStarterTemplate.aws: "https://github.com/phidatahq/phidata-starter-aws.git",
    WorkspaceStarterTemplate.aws_snowflake_jupyter: "https://github.com/phidatahq/aws-snowflake-jupyter-starter.git",
}
