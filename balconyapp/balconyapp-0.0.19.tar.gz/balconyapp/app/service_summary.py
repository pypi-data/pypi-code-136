from balcony import BaseBalconyApp, BalconyAWS
from typer.main import Typer
import typer
from typing import Optional
import jmespath



class BalconyServiceSummarizer(BaseBalconyApp,
        author="og", 
        app_name="service-summarizer", 
        description="Prints a summary of the given Balcony service.",
        tags=('balcony', 'service-node')
    ):
    
    def __init__(self, *args, **kwargs) -> None:
        pass
      
    def get_data(self, *args, **kwargs) -> dict:
        balcony = BalconyAWS()
        # role_data = balcony.get_service('iam').read('Role')
        return {} 
       
    def get_cli_app(self, *args, **kwargs) -> typer.main.Typer:
        app = typer.Typer(no_args_is_help=True)
        
        @app.callback()
        def _command(
            service: Optional[str] = typer.Argument(None, show_default=False,help='AWS Service Name'),
        ):
            typer.echo(service)
            typer.echo(self.get_data())
            typer.echo('-'*20)
        return app
                
    


