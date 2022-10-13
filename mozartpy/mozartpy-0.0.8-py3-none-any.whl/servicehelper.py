import zeep  # soap 통신에 사용되는 package
import tqdm  # progress bar 표시에 사용되는 package
import os
import zipfile
from datetime import datetime
from multipledispatch import dispatch

class Downloader:
    url = ''
    subDir = ''
    client = None

    ''' url has this form ( http://192.168.1.82:8000/mozart/OutFileService ) '''
    def __init__(self, url, subDir):
        self.url = '{0}/mex?wsdl'.format(url)
        self.subDir = subDir
        try:
            self.client = zeep.Client(wsdl=self.url)
        except ConnectionError as error:
            raise Exception('Connection failed. Wrong or inaccessible hostname:'.format(error=error))

    def GetFileList(self):
        ''' OutfileService 가 제공하는 파일리스트를 반환
        :returns
            file list<string> : model file list
        '''


        files = self.client.service.GetFileList2(self.subDir)
        # with zeep.Client(wsdl=self.url) as client:
        #     files = client.service.GetFileList2(self.subDir)
        return files

    def __checkDir__(self, destination):
        filedir = destination
        if not os.path.exists(filedir):
            print('{0} is not exist path :'.format(filedir))
            pass

    @dispatch(list, str, bool)#for function overloading
    def DownloadFiles(self, filenames, destination, unzip=False):
        ''' 입력된 filenames 들을 지정한 위치에 다운로드
        :param
            filenames(list<string>) : 모델파일 이름리스트
            destination(string> : 다운로드 받을 위치
            unzip(bool) : 다운로드 받고 압축된 파일을 압축해제 할 지 여부
        :returns
            None
        '''
        
        filedir = destination
        if not os.path.exists(filedir):
            raise Exception('{0} is not exist path :'.format(filedir))

        downloadedFiles = []
        for fname in filenames:
            filesize = self.client.service.GetFileSize2(fname, self.subDir)

            offset = 0
            chunkSize = 0x10000  # 10Mbytes
            count = filesize

            progress = tqdm.tqdm(range(filesize), f"Receiving {fname}", unit="B", unit_scale=True,
                                 unit_divisor=1024)

            filePath = os.path.join(filedir, fname)
            with open(filePath, 'wb') as f:
                f.seek(offset, 0)
                while offset < filesize:
                    if filesize >= chunkSize:
                        count = chunkSize
                    buffer = self.client.service.GetFileChunk2(fname, self.subDir, offset, count)
                    if not buffer:
                        break

                    f.write(buffer)
                    offset += len(buffer)
                    progress.update(len(buffer))

                downloadedFiles.append(filePath)
                if unzip:
                    splitFileNames = os.path.splitext(fname)
                    if splitFileNames.__len__() < 2:
                        continue
                    zipdir = splitFileNames[0]
                    if not zipfile.is_zipfile(filePath):
                        continue
                    try:
                        with zipfile.ZipFile(filePath,'r') as zip_ref:
                            zip_ref.extractall(os.path.join(filedir, zipdir))
                    except ConnectionError as error:
                        print(filePath)
                        print(zipdir)
                        raise error

        # delete zipfile
        if unzip:
            for dfile in downloadedFiles:
                os.remove(dfile)

    @dispatch(datetime, datetime, str, bool)#for function overloading
    def DownloadFiles(self, fromDate, toDate, destination, unzip=False):
        ''' 입력된 from~to 기간에 생성된 모델파일들을 지정한 위치에 다운로드
        :param
            fromDate(datetime) : 시작날짜
            todate(datetime) : 끝날짜
            destination(string> : 다운로드 받을 위치
            unzip(bool) : 다운로드 받고 압축된 파일을 압축해제 할 지 여부
        :returns
            None
        '''

        filedir = destination
        if not os.path.exists(filedir):
            raise Exception('{0} is not exist path :'.format(filedir))

        files = self.GetFileList()
        if files == None:
            print('There is no data')
            pass

        downloadFiles = []
        for fname in files:
            tmp = os.path.splitext(fname)
            if tmp.__len__() < 2:
                continue

            dateStr = tmp[0][-14:]
            try:
                runTime = datetime.strptime(dateStr, '%Y%m%d%H%M%S')
            except:
                print('{0} cannot recognize date :'.format(fname))
                continue

            if fromDate > runTime or runTime > toDate:
                continue

            downloadFiles.append(fname)
        if downloadFiles.__len__() == 0:
            print('There is no data to download : {0} ~ {1}'.format(fromDate, toDate))
            pass

        self.DownloadFiles(downloadFiles, destination, unzip)

    @dispatch(int, str, bool)
    def DownloadFiles(self, count, destination, unzip = False):
        ''' 가장 최근에 생성된 모델들의 입력한 갯수 만큼 지정한 위치에 다운로드
        :param
            count(int) : 다운로드 받을 파일의 갯수
            destination(string> : 다운로드 받을 위치
            unzip(bool) : 다운로드 받고 압축된 파일을 압축해제 할 지 여부
        :returns
            None
        '''
        self.__checkDir__(destination)

        files = self.GetFileList()

        downloadFiles = []
        chkCnt = 0
        for fname in files:
            if chkCnt == count:
                break
            downloadFiles.append(fname)
            chkCnt += 1

        self.DownloadFiles(downloadFiles, destination, unzip)




