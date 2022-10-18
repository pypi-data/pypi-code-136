# https://pop.readthedocs.io/en/latest/tutorial/quickstart.html#adding-configuration-data
# In this dictionary goes all the immutable values you want to show up under hub.OPT.pop_archive
CONFIG = {
    "config": {
        "default": None,
        "help": "Load extra options from a configuration file onto hub.OPT.pop_archive",
    }
}

# These are the namespaces that your project extends
# The hub will extend these keys with the modules listed in the values
DYNE = {
    "exec": ["exec"],
}
