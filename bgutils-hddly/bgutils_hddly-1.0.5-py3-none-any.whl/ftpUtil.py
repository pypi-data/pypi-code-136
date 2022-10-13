import paramiko
class ftpUtil:
    # 登陆参数设置
    __hostname = "home.hddly.cn"
    __host_port = 8021
    __username_media = "ftpuser"
    __password_media = "ywq20120721"
    __username_stud ="student"
    __password_stud ="student"
    remotedir = "/media/"

    def putfile_stud(self,local_path,remote_file):
        # # 要传输文件的路径
        # filepath = "./myname.jpg"
        # # 上传后的传输文件的文件名
        # filename = "drawpic_myname.jpg" #请将myname改为本人学号
        try:
            transport = paramiko.Transport((self.__hostname, self.__host_port))
            transport.connect(self.__username_stud, self.__password_stud)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.chdir("/send/")
            sftp.put(local_path,remote_file)
            print('上传成功......')
            sftp.close()
            transport.close()
        except:
            print('连接失败......')

    def putfile_media(self,local_path,remote_file):
        t = paramiko.Transport((self.__hostname, self.__host_port))
        t.connect(username=self.__username_media, password=self.__password_media)
        sftp = paramiko.SFTPClient.from_transport(t)
        remote_path = "/media/" + remote_file  # 远程路径
        put_info = sftp.put(local_path, remote_path, confirm=True)
        print(put_info)
        print(f"finished put file:{local_path}.")
        t.close

    def getfile_media(self,remote_file,local_path):
        t = paramiko.Transport((self.__username_media, self.__host_port))
        t.connect(username=self.__username_media, password=self.__password_media)
        sftp = paramiko.SFTPClient.from_transport(t)
        remote_path = "/media/" + remote_file  # 远程路径
        sftp.get(remotepath=remote_path, localpath=local_path)
        print(f"finished get file:{local_path}.")
        t.close