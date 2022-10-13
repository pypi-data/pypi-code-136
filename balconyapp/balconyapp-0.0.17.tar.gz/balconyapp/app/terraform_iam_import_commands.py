from balcony import BaseBalconyApp, BalconyAWS
from typer.main import Typer
import typer
from typing import Optional
import jmespath


balcony = BalconyAWS()
def get_role_names():
    role_data = balcony.get_service('iam').read('Role')
    expr = 'ListRoles[*].Roles[*].RoleName[]'
    role_names = jmespath.search(expr, role_data)
    return role_names

def generate_import_command(tf_aws_type, tf_resource, import_id):
    return f"terraform import {tf_aws_type}.{tf_resource} {import_id}"
      
def generate_role_import_commands():
    cmmds = []
    role_names = get_role_names()
    for i, role_name in enumerate(role_names):
        cmmds.append(generate_import_command('aws_iam_role', f"Role{str(i+1)}", role_name))
    return cmmds

class TerraformIAMImportCommandGenerator(BaseBalconyApp,
        author="og", 
        app_name="terraform-import-iam", 
        description="List the Account Ids that roles have trusted entity relation with.",
        tags=('iam', 'role', 'trusted-entity')
    ):
    
    def __init__(self, *args, **kwargs) -> None:
        pass        

    def get_data(self, *args, **kwargs) -> dict:
        return generate_role_import_commands
    
    def get_cli_app(self, *args, **kwargs) -> typer.main.Typer:
        app = typer.Typer(no_args_is_help=True)
        
        @app.command('role')
        def _role_tf_importer(
            service: Optional[str] = typer.Argument(None, show_default=False,help='argument name'),
        ):
            for role_import_cmd in generate_role_import_commands():
                typer.echo(role_import_cmd)
        return app
                
    


