from generalpackager.api.localrepo.base.metadata import Metadata

class Metadata_Python(Metadata):
    """ Todo: Dynamic values in DataClass to remove LocalRepos and Metadatas. """

    install_requires = []
    extras_require = {}

    def read_hook_post(self):
        extras_require = self.halt_getattr("extras_require")
        if extras_require:
            keys = [key for key in extras_require.values() if key != "full"]
            extras_require["full"] = list(set().union(*keys))
            extras_require["full"].sort()

    def write_hook_pre(self, dict_):
        super().write_hook_pre(dict_=dict_)
        dict_.get("extras_require", {}).pop("full", None)

