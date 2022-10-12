from typing import Text

from uhugo.post_install.providers import ProviderBase


class Vercel(ProviderBase):
    """
    Vercel provider
    """

    def update_config_file(self, file_name: Text):
        """
        Updates ``vercel.json`` file with Hugo's version

        :param file_name: Path of ``vercel.json``
        :return:
        """
        pass

    def update_api(self, key: Text):
        """
        Updates Cloudflare Pages environment variable of ``HUGO_VERSION``.

        :param key: API key
        :return:
        """
        pass
