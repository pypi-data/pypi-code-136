import click
from fenerbahce.last_match import last_match
from fenerbahce.next_match import next_match
from click_help_colors import HelpColorsGroup


@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='blue'
)
def interface():
    """Find information on past and future games of Fenerbahçe's Professional Football Team"""
    pass


@click.command()
def next():
    """Show information on the next game"""
    info = next_match().split('\n')

    count = 0
    fg_colour = 'yellow'
    bg_colour = 'blue'

    for elem in info:
        if count is 0:
            fg_colour = 'blue'
            bg_colour = 'yellow'
            count = 1
        else:
            fg_colour = 'yellow'
            bg_colour = 'blue'
            count = 0
        click.secho(elem, fg=fg_colour, bg=bg_colour, bold=True)


@click.command()
def last():
    """Show information on the last game"""
    info = last_match()
    click.secho(info, bg='blue', fg='yellow', bold=True)


interface.add_command(next)
interface.add_command(last)
