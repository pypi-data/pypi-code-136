import podarr


class PLEX(podarr.BaseService):

    def __init__(self) -> None:
        super().__init__('plex')
        self.directories = {
            'base': podarr.Directory.DIR_BASE.joinpath('plex'),
            'transcode': podarr.Directory.DIR_BASE.joinpath('plex', 'transcode'),
        }
        self.container_pars = f'--device=/dev/dri:/dev/dri '\
            f'--network=host '\
            f'-e PUID={self.uid} '\
            f'-e PGID={self.gid} '\
            f'-p {self.service.ports[0].number}:32400 '\
            f'--volumes-from podarr-mergerfs '\
            f'-v {self.directories["base"]}:/config '\
            f'-v {self.directories["transcode"]}:/transcode '\
            f'{self.service.image}:{self.service.tag}'
        self.backup_pars = '"Library/Application Support/Plex Media Server/Preferences.xml" '\
            '"Library/Application Support/Plex Media Server/Plug-in Support" '\
            '"Library/Application Support/Plex Media Server/Media" '\
            '"Library/Application Support/Plex Media Server/Metadata"'
