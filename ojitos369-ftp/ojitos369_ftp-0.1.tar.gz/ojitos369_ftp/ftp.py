from ftplib import FTP

class ConnectionFtp:
    def __init__(self, ftp_data: dict):
        "ftp data a dict with host, port, user, password"
        self.ftp = FTP()
        host = ftp_data['host']
        port = ftp_data['port']
        user = ftp_data['user']
        passwd = ftp_data['password']
        self.ftp.connect(host, port)
        self.ftp.login(user, passwd)

    def cd(self, path: str):
        """Move to dir path"""
        self.ftp.cwd(path)

    def lsf(self):
        return self.ftp.dir()

    def ls(self, path: str = None) -> list:
        """Reaturn a list with file_names in a path"""
        files = []
        if not path:
            files_full = self.ftp.nlst()
        else:
            files_full = self.ftp.nlst(path)
        # print(files_full)
        for file in files_full:
            if not path:
                if not file.startswith('.'):
                    files.append(file)
            else:
                file_name = file.split('/')[-1]
                if not file_name.startswith('.'):
                    files.append(file_name)
        return files

    def mkdir(self, path: str):
        """Create a dir"""
        self.ftp.mkd(path)

    def upload(self, path: str, new_path: str):
        """Update a File

        Args:
            path (str): Original path
            new_path (str): Destiny path
        """
        self.ftp.storbinary('STOR ' + new_path, open(path, 'rb'))

    def rmdir(self, path: str):
        """Remove dir with all files"""
        self.clear_dir(path)
        self.ftp.rmd(path)
    
    def clear_dir(self, path: str):
        """Remove all files from dir"""
        files = self.ls(path)
        # print(files)
        if files:
            for file in files:
                self.rm(path + file)

    def rm(self, path: str):
        """rm file"""
        self.ftp.delete(path)
    
    def pwd(self) -> str:
        """Return actual dir"""
        return self.ftp.pwd()

    def rename(self, path: str, new_path: str):
        """Rename a File or dir"""
        self.ftp.rename(path, new_path)
    
    def mv(self, path: str, new_path: str):
        """Move a file or dir"""
        self.ftp.rename(path, new_path)
        
    def mv_files(self, path: str, new_path: str):
        """Move all files from path

        Args:
            path (str): origin path
            new_path (str): destiny path
        """
        files = self.ls(path)
        # print(files)
        if files:
            for file in files:
                self.mv(path + file, new_path + file)
    
    def cp(self, path, new_path):
        """Copy remote file to local path"""
        self.ftp.retrbinary('RETR ' + path, open(new_path, 'wb').write)
    
    def close(self):
        """Close FTP Connection"""
        self.ftp.close()