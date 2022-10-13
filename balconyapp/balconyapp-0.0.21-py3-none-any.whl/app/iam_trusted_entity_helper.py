from balcony import BaseBalconyApp, BalconyAWS
from typer.main import Typer
import typer
from typing import Optional
import jmespath


class IAMTrustedEntities(BaseBalconyApp,
        author="og", 
        app_name="iam-trusted-entities", 
        description="List the Account Ids that roles have trusted entity relation with.",
        tags=('iam', 'role', 'trusted-entity')
    ):
    
    def __init__(self, *args, **kwargs) -> None:
        pass
      
    def get_data(self, *args, **kwargs) -> dict:
        balcony = BalconyAWS()
        role_data = balcony.get_service('iam').read('Role')
        expr = 'ListRoles[*].Roles[*].AssumeRolePolicyDocument[].Statement[*].Principal[].AWS'
        return jmespath.search(expr, role_data)
    
    def get_cli_app(self, *args, **kwargs) -> typer.main.Typer:
        app = typer.Typer(no_args_is_help=True)
        
        @app.command('hey')
        def _hey_command(
            service: Optional[str] = typer.Argument(None, show_default=False,help='argument name'),
        ):
            typer.echo(service)
            typer.echo(self.get_data())
            typer.echo('-'*20)
            
        return app
                
    


