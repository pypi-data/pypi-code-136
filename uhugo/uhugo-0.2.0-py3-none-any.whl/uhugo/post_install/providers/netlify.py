from typing import Text

from . import ProviderBase


class Netlify(ProviderBase):
    """
    Netlify provider
    """

    def update_config_file(self, file_name: Text):
        """
        Updates ``netlify.yaml`` file with Hugo's version

        :param file_name: Path of ``netlify.yaml``
        :return:
        """
        pass
