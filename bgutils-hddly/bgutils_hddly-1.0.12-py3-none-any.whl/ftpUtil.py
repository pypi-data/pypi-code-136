import os

import paramiko
from bgutils.mysqlUtil import mysqlUtil


class ftpUtil:
    # 登陆参数设置
    __hostname = "home.hddly.cn"
    __host_port = 8021
    __username_media = "ftpuser"
    __password_media = "ywq20120721"
    __username_stud ="student"
    __password_stud ="student"
    __remotedir_media = "/media/"
    __remotedir_stud = "/send/"
    __url_head="http://home.hddly.cn:90/stud/"
    __mutil= mysqlUtil()

    def putfile_stud(self,local_path,prj_id,stud_id,no_file):
        # # 要传输文件的路径
        # filepath = "./myname.jpg"
        # # 上传后的传输文件的文件名
        # remote_file = 项目ID(6位)+学生ID（11位）+文件ID(2位)+文件类型
        # 如P22001_20190010011_01.jpg
        try:
            file_type=os.path.splitext(local_path)[-1]
            transport = paramiko.Transport((self.__hostname, self.__host_port))
            transport.connect(username=self.__username_stud, password=self.__password_stud)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.chdir(self.__remotedir_stud)
            prj="P"+prj_id.zfill(6)
            stud=stud_id.zfill(11)
            no=no_file.zfill(2)
            remote_file=prj+"_" + stud +"_" + no+"."+file_type
            sftp.put(local_path,remote_file)
            print('上传成功......')
            sftp.close()
            transport.close()
        except Exception as ex:
            print("连接出现如下异常%s" % ex)

        try:
            #记录文件列表
            # item = entSftpFile()
            # item['filename'] = local_path
            # item['url'] = self.__url_head+remote_file
            # item['stud'] = stud
            self.__mutil.sftp_file_ins(local_path,self.__url_head+remote_file,stud)
        except Exception as ex:
            print("日志记录出现如下异常%s"%ex)

    def putfile_media(self,local_path,remote_file):
        t = paramiko.Transport((self.__hostname, self.__host_port))
        t.connect(username=self.__username_media, password=self.__password_media)
        sftp = paramiko.SFTPClient.from_transport(t)
        remote_path = self.__remotedir_media + remote_file  # 远程路径
        put_info = sftp.put(local_path, remote_path, confirm=True)
        print(put_info)
        print(f"finished put file:{local_path}.")
        t.close

    def getfile_media(self,remote_file,local_path):
        t = paramiko.Transport((self.__username_media, self.__host_port))
        t.connect(username=self.__username_media, password=self.__password_media)
        sftp = paramiko.SFTPClient.from_transport(t)
        remote_path = self.__remotedir_media + remote_file  # 远程路径
        sftp.get(remotepath=remote_path, localpath=local_path)
        print(f"finished get file:{local_path}.")
        t.close