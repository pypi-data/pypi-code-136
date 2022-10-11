import podarr


class RADARR(podarr.BaseService):

    def __init__(self) -> None:
        super().__init__('radarr')
        self.directories = {
            'base': podarr.Directory.DIR_BASE.joinpath('radarr'),
        }
        self.container_pars = f'-e PUID={self.uid} '\
            f'-e PGID={self.gid} '\
            f'-p {self.service.ports[0].number}:7878 '\
            f'--volumes-from podarr-mergerfs '\
            f'-v {self.directories["base"]}:/config '\
            f'{self.service.image}:{self.service.tag}'
        self.backup_pars = '--exclude="custom-cont-init.d" --exclude="custom-services.d" .'
