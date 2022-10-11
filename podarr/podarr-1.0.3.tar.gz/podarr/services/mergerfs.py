import podarr


class MERGERFS(podarr.BaseService):

    def __init__(self) -> None:
        super().__init__('mergerfs')
        self.directories = {
            'base': podarr.Directory.DIR_BASE.joinpath('mergerfs'),
            'pool': podarr.Directory.DIR_DATA.joinpath('pool')
        }
        self.container_pars = f'--cap-add=sys_admin '\
            f'--device /dev/fuse '\
            f'-e PUID={self.uid} '\
            f'-e PGID={self.gid} '\
            f'--volumes-from podarr-rclone '\
            f'-v {self.directories["base"]}:/config '\
            f'-v {podarr.Directory.DIR_DATA_LOCAL}:/data/local '\
            f'-v {self.directories["pool"]}:/data/pool:shared '\
            f'{self.service.image}:{self.service.tag} '\
            f'/data/local:/data/remote /data/pool '\
            f'-o rw,use_ino,allow_other,nonempty,func.getattr=newest,'\
            f'category.action=all,category.create=ff,cache.files=auto-full,'\
            f'umask=002'

    def start(self) -> bool:
        """
        MergerFS also needs to set ownership of the data directory.
        """
        podarr.Directory().set_ownership(self.directories['base'])
        podarr.Directory().set_ownership(podarr.Directory.DIR_DATA)
        podarr.Directory().bind_mount(podarr.Directory.DIR_DATA)
        start = podarr.Systemd().start(self.service)
        return start

    def stop(self) -> bool:
        """
        Revokes ownership of the data directory.
        """
        stop = podarr.Systemd().stop(self.service)
        podarr.Directory().revoke_ownership(self.directories['base'])
        podarr.Directory().revoke_ownership(podarr.Directory.DIR_DATA)
        podarr.Directory().bind_unmount(podarr.Directory.DIR_DATA)
        return stop

    def backup(self) -> None:
        pass

    def restore(self) -> None:
        pass
