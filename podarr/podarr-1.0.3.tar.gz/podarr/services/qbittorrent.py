import podarr


class QBITTORRENT(podarr.BaseService):

    def __init__(self) -> None:
        super().__init__('qbittorrent')
        self.directories = {
            'base': podarr.Directory.DIR_BASE.joinpath('qbittorrent'),
            'torrent': podarr.Directory.DIR_DATA_LOCAL.joinpath('torrent'),
            'incomplete': podarr.Directory.DIR_DATA_LOCAL.joinpath('torrent', 'incomplete'),
            'complete': podarr.Directory.DIR_DATA_LOCAL.joinpath('torrent', 'complete'),
            'movies': podarr.Directory.DIR_DATA_LOCAL.joinpath('torrent', 'complete', 'movies'),
            'music': podarr.Directory.DIR_DATA_LOCAL.joinpath('torrent', 'complete', 'music'),
            'series': podarr.Directory.DIR_DATA_LOCAL.joinpath('torrent', 'complete', 'tv'),
        }
        self.container_pars = f'-e PUID={self.uid} '\
            f'-e PGID={self.gid} '\
            f'-e WEBUI_PORT={self.service.ports[0].number} '\
            f'-p 6881:6881 '\
            f'-p 6881:6881/udp '\
            f'-p {self.service.ports[0].number}:{self.service.ports[0].number} '\
            f'--volumes-from podarr-mergerfs '\
            f'-v {self.directories["base"]}:/config '\
            f'{self.service.image}:{self.service.tag}'
        self.backup_pars = '--exclude="custom-cont-init.d" --exclude="custom-services.d" .'
