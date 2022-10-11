import podarr


class SABNZBD(podarr.BaseService):

    def __init__(self) -> None:
        super().__init__('sabnzbd')
        self.directories = {
            'base': podarr.Directory.DIR_BASE.joinpath('sabnzbd'),
            'usenet': podarr.Directory.DIR_DATA_LOCAL.joinpath('usenet'),
            'incomplete': podarr.Directory.DIR_DATA_LOCAL.joinpath('usenet', 'incomplete'),
            'complete': podarr.Directory.DIR_DATA_LOCAL.joinpath('usenet', 'complete'),
            'movies': podarr.Directory.DIR_DATA_LOCAL.joinpath('usenet', 'complete', 'movies'),
            'music': podarr.Directory.DIR_DATA_LOCAL.joinpath('usenet', 'complete', 'music'),
            'series': podarr.Directory.DIR_DATA_LOCAL.joinpath('usenet', 'complete', 'tv'),
        }
        self.container_pars = f'-e PUID={self.uid} '\
            f'-e PGID={self.gid} '\
            f'-p {self.service.ports[0].number}:8080 '\
            f'-p {self.service.ports[1].number}:9090 '\
            f'--volumes-from podarr-mergerfs '\
            f'-v {self.directories["base"]}:/config '\
            f'{self.service.image}:{self.service.tag}'
        self.backup_pars = 'sabnzbd.ini'

    def get_apit_key(self):
        """
        Get the API key from the SABnzbd configuration file.
        """
        raw_cfg = podarr.Podman().unshare(
            f'cat {self.directories["base"].joinpath(self.backup_pars)}').stdout
        return [line for line in raw_cfg.split(
            '\n') if line.startswith('api_key = ')][0].replace('api_key = ', '')
