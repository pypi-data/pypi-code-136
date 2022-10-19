from sys import argv
from os.path import exists, dirname
import urmapi

class modules:
    executed = False
    error = ""

    class options:
        """
        Meta of URM-API
        """
        def version() -> None:
            """
            Returns version of URM-API
            """
            modules.executed = True
            print(f"URM-API Version: {urmapi.__version__}")
            print(f"URM-API Accepted Config Versions:\n {urmapi.__accepted_versions__}")
        
        def help() -> None:
            """
            Prints help message
            """
            print("Variables:")
            for vKey, vVal in variables.items():
                print(f"{vKey}\t\t{vVal[0]}")
                
            print()

            print("Options:")
            for oKey, oVal in options.items():
                print(f"{oKey}\t\t{oVal[0]}")

            print()

            print("Commands:")
            for cKey, cVal in commands.items():
                print(f"{cKey}\t\t{cVal[0]}")

            modules.executed = True



    class commands:
        """
        Interacting with the API
        """
        def install() -> None:
            """
            Installs a package
            """
            if len(argv) > 1:
                if argv[1].startswith("http"):
                    api = urmapi.API(server = argv[1])
                else:
                    api = urmapi.API(config = argv[1])
                
                if len(argv) > 2:
                    api.install(location=argv[2])

                else:
                    api.install(location=dirname(__file__))
                
                modules.executed = True

            else:
                modules.error = "Please specify a link or config file"

        def update() -> None:
            """
            Updates a Package
            """
            if len(argv) > 1:
                if exists(argv[1]):
                    api = urmapi.API(config = argv[1])
                    api.update()
                    modules.executed = True

            else:
                modules.error = "Please specify a config.urmapi.json file"

variables = {
    }
options = {
    "--version": ["Show URM-API version.", modules.options.version],
    "--help": ["Show this message or module information.", modules.options.help]
    }
commands = {
    "install": ["Install a package using URM-API.", modules.commands.install],
    "update": ["Checks for updates in all packages, then updates.", modules.commands.update]
    }

if len(argv) == 1:
    modules.options.help()

else:
    argv.pop(0)
    executed = False

    for option in options:
        if argv[0] == option:
            options[option][1]()
            executed = True

    for command in commands:
        if argv[0] == command:
            commands[command][1]()
            executed = True

    if not executed:
        print(f"Command: '{argv[0]}' not found.")
        print("For help on commands, type 'urmapi --help'")