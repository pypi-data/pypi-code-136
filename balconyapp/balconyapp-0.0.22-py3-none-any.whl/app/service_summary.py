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
        typer.echo(service)
        service_node = balcony.get_service(service)
        resource_nodes = service_node.get_resource_nodes()
        read_only_function_count = 0
        resource_node_names = []
        for rn in resource_nodes:
            resource_node_names.append(rn.name)
            read_only_function_count += len(rn.operation_names)
        return {
            'read_only_function_count':read_only_function_count,
            'resource_node_names': resource_node_names
        } 
       
    def get_cli_app(self, *args, **kwargs) -> typer.main.Typer:
        app = typer.Typer(no_args_is_help=True)
        
        
        def generate_table() -> Table:
            """Make a new table."""
            table = Table()
            table.add_column("ID")
            table.add_column("Value")
            table.add_column("Status")

            for row in range(random.randint(2, 6)):
                value = random.random() * 100
                table.add_row(
                    f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
                )
            return table



        @app.callback(invoke_without_command=True)
        def _command(
            service: str = typer.Argument(None, show_default=False,help='AWS Service Name'),
        ):
            data = self.get_data(service=service)

            # layout = Layout()
            # layout.split_column(
            #     Layout(name="upper"),
            #     Layout(name="lower")
            # )            
            # console.print(layout)
            # console.print(data)
            with Live(generate_table(), refresh_per_second=4) as live:
                for _ in range(40):
                    time.sleep(0.4)
                    live.update(generate_table())
        return app
                
    


