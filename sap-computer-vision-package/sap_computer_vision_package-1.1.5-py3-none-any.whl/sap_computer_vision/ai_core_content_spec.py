import pathlib
import yaml

from ai_core_sdk.content import ContentPackage

HERE = pathlib.Path(__file__).parent
VERSION_TXT = HERE / 'RELEASE_INFO'


workflows_yaml = HERE / 'pipelines' / 'workflows.yaml'

with workflows_yaml.open() as stream:
    workflows = yaml.safe_load(stream)


sap_cv_repo = ContentPackage(
    name='sap-cv',
    description='Content Package for computer vision',
    workflows_base_path=workflows_yaml.parent,
    workflows=workflows,
    license="SAP DEVELOPER LICENSE AGREEMENT",
    examples=str(HERE / 'examples'),
    version=VERSION_TXT.open().read().strip() if VERSION_TXT.exists() else None
    )
