from balcony import BaseBalconyApp, BalconyAWS, get_rich_console
from typer.main import Typer
import typer
from typing import Optional
import jmespath
import random
import time
from rich.layout import Layout
from rich.live import Live
from rich.table import Table
from rich.panel import Panel



console = get_rich_console()

class BalconyServiceSummarizer(BaseBalconyApp,
        author="og", 
        app_name="service-summarizer", 
        description="Prints a summary of the given Balcony service.",
        tags=('balcony', 'service-node')
    ):
    
    def __init__(self, *args, **kwargs) -> None:
        pass
      
    def get_data(self, *args, **kwargs) -> dict:
        service=kwargs.get('service')
        balcony = BalconyAWS()
        service_node = balcony.get_service(service)

        read_only_function_count = 0
        generated_resource_nodes = []
        for rn in service_node.get_resource_nodes():
            operation_names = rn.get_operation_names() 
            generated_resource_nodes.append({
                'name': rn.name,
                'operation_names': operation_names
            })
            read_only_function_count += len(operation_names)
        return {
            'read_only_function_count':read_only_function_count,
            'resource_nodes': generated_resource_nodes
        } 
       
    def get_cli_app(self, *args, **kwargs) -> typer.main.Typer:
        app = typer.Typer(no_args_is_help=True)
        
        
        def kayan_yazi(_list, window=5):
            length = len(_list)
            until = length - window
            for i in range(until+1):
                yield _list[i:i+window]
        
        def generate_live_render(data):
            nonlocal self
            resource_node_names = [r.get('name') for r in data.get('resource_nodes')]
            for ky in kayan_yazi(resource_node_names):
                str_ky = '\n'.join(ky)
                layout = Layout(Panel(str_ky), name="main")
                yield layout


        @app.callback(invoke_without_command=True)
        def _command(
            service: str = typer.Argument(None, show_default=False,help='AWS Service Name'),
        ):
            balcony = BalconyAWS()
            available_services = balcony.get_available_service_node_names()
            selected_service = random.choice(available_services)
            data = self.get_data(service=selected_service)
            print(data)
            with Live(selected_service, refresh_per_second=2) as live:
                for rendered in generate_live_render(data):
                    live.update(rendered)
                    time.sleep(0.4)
                    
        return app
                
    


