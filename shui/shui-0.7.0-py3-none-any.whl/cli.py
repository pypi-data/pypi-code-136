"""Command line entrypoint for shui application"""
from cleo import Application
from shui.commands import InstallCommand, VersionsCommand
from shui import __version__

application = Application("shui", __version__, complete=True)
application.add(InstallCommand())
application.add(VersionsCommand())


def main():
    """Command line entrypoint for shui application"""
    application.run()
