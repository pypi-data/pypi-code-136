from enum import Enum
import typer
import oss2
from typing import Optional, List
import zipfile
import os
from rich.console import Console
from rich.table import Column, Table



def zip_all_files(dir,zipFile,pre_dir):
    """递归压缩文件夹下的所有文件
    参数:
    - dir: 要压缩的文件夹路径
    - zipFile: zipfile对象
    - pre_dir: 压缩文件根目录
    """
    for f in os.listdir(dir):
        absFile=os.path.join(dir,f) #子文件的绝对路径
        pre_d = os.path.join(pre_dir,f)
        if os.path.isdir(absFile): #判断是文件夹，继续深度读取。
            zipFile.write(absFile, pre_d) #在zip文件中创建文件夹
            zip_all_files(absFile,zipFile, pre_dir=pre_d) #递归操作
        else: #判断是普通文件，直接写到zip文件中。
            zipFile.write(absFile, pre_d)

default_access_key_id = 'LTAI5t6eZadbhsTd1v1pLCAk'
default_access_key_secret = '2PbNnJQ3bwiKePcLsvnbnxcBZjSJ39'
default_endpoint = 'http://oss-cn-beijing.aliyuncs.com'
hangzhou_endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'
default_data_bucket = 'deepset'
default_model_bucket = 'pretrained-model'
default_asset_bucket = 'deepasset'
default_corpus_bucket = 'deepcorpus'
default_pipeline_bucket = 'spacy-pipeline'

class OSSStorer:
    '''阿里云oss对象存储'''
    def __init__(
        self, 
        access_key_id : str = default_access_key_id,
        access_key_secret : str = default_access_key_secret, 
        endpoint :str = default_endpoint, 
        data_bucket : str = default_data_bucket,
        model_bucket : str = default_model_bucket,
        asset_bucket : str = default_asset_bucket,
        corpus_bucket: str = default_corpus_bucket,
        pipe_bucket: str = default_pipeline_bucket
        ):
        super().__init__()
        self.auth = oss2.Auth(access_key_id, access_key_secret)
        self.data_bucket = oss2.Bucket(self.auth, endpoint, data_bucket)
        self.model_bucket = oss2.Bucket(self.auth, endpoint, model_bucket)
        self.assets_bucket = oss2.Bucket(self.auth, endpoint, asset_bucket)
        self.corpus_bucket = oss2.Bucket(self.auth, hangzhou_endpoint, corpus_bucket)
        self.pipe_bucket = oss2.Bucket(self.auth, endpoint, pipe_bucket)

    def list_all_assets(self):
        """获取数据名称"""
        all_asset = []
        for obj in oss2.ObjectIterator(self.assets_bucket):
            asset = obj.key.split('.')[0]
            all_asset.append(asset)
        return all_asset


    def list_all_datasets(self):
        """获取所有数据集名称"""
        all_data = []
        for obj in oss2.ObjectIterator(self.data_bucket):
            data = obj.key.split('.')[0]
            all_data.append(data)
        return all_data
    
    def list_all_plms(self):
        """获取所有预模型名称"""
        all_model = []
        for obj in oss2.ObjectIterator(self.model_bucket):
            model = obj.key.split('.')[0]
            all_model.append(model)
        return all_model
    
    def list_all_corpus(self):
        all_corpus = []
        for obj in oss2.ObjectIterator(self.corpus_bucket):
            corpus = obj.key.split('.')[0]
            all_corpus.append(corpus)
        return all_corpus
    
    def list_all_pipelines(self):
        all_pipelines = []
        for obj in oss2.ObjectIterator(self.pipe_bucket):
            pipe = obj.key.split('.')[0]
            all_pipelines.append(pipe)
        return all_pipelines
        


    def download_dataset(
        self, 
        dataset:str, 
        localpath: str='./datasets/'):
        """下载数据集
        - dataset: 数据集名称
        - localpath: 下载到本地的路径 默认为./datasets/
        """
        if not os.path.exists(localpath):
            os.makedirs(localpath)
        file = dataset + '.zip'
        file_path = localpath + file
        dataset_path = localpath + dataset
        if not os.path.exists(dataset_path):
            try:
                self.data_bucket.get_object_to_file(key=file, filename=file_path)
                with zipfile.ZipFile(file=file_path, mode='r') as zf:
                    zf.extractall(path=localpath)
            finally:
                if os.path.exists(file_path):
                    os.remove(path=file_path)


    def download_plm(
        self, 
        model:str, 
        localpath: str = './plms/'):
        """下载预训练模型
        - model: 模型名称
        - localpath: 下载到本地的路径 默认为./plms/
        """
        if not os.path.exists(localpath):
            os.makedirs(localpath)
        file = model + '.zip'
        file_path = localpath + file
        model_path = localpath + model
        if not os.path.exists(model_path):
            try:
                self.model_bucket.get_object_to_file(key=file, filename=file_path)
                with zipfile.ZipFile(file=file_path, mode='r') as zf:
                    zf.extractall(path=localpath)
            finally:
                if os.path.exists(file_path):
                    os.remove(path=file_path)
                


    def download_asset(
        self, 
        asset:str, 
        localpath: str = './assets/'):
        """下载assets
        - asset: 资产名称
        - localpath: 下载到本地的路径 默认为./assets/
        """
        if not os.path.exists(localpath):
            os.makedirs(localpath)
        file = asset + '.zip'
        file_path = localpath + file
        asset_path = localpath + asset
        if not os.path.exists(asset_path):
            try:
                self.assets_bucket.get_object_to_file(key=file, filename=file_path)
                with zipfile.ZipFile(file=file_path, mode='r') as zf:
                    zf.extractall(path=localpath)
            finally:
                if os.path.exists(file_path):
                    os.remove(path=file_path)
                    
    def download_corpus(self,
                        corpus: str,
                        localpath: str = './corpus'):
        localpath = os.path.join(os.getcwd(), localpath)
        if not os.path.exists(localpath):
            os.makedirs(localpath)
        file = corpus + '.zip'
        file_path = os.path.join(localpath, file)
        corpus_path = os.path.join(localpath, corpus)
        if not os.path.exists(corpus_path):
            try:
                self.corpus_bucket.get_object_to_file(key=file, filename=file_path)
                with zipfile.ZipFile(file=file_path, mode='r') as zf:
                    zf.extractall(path=localpath)
            finally:
                if os.path.exists(file_path):
                    os.remove(path=file_path)
    def download_pipeline(self, 
                          pipeline: str,
                          localpath: str = './pipelines'):
        localpath = os.path.join(os.getcwd(), localpath)
        if not os.path.exists(localpath):
            os.makedirs(localpath)
        file = pipeline + '.zip'
        file_path = os.path.join(localpath , file)
        pipeline_path = os.path.join(localpath , pipeline)
        if not os.path.exists(pipeline_path):
            try:
                self.pipe_bucket.get_object_to_file(key=file, filename=file_path)
                with zipfile.ZipFile(file=file_path, mode='r') as zf:
                    zf.extractall(path=localpath)
            finally:
                if os.path.exists(file_path):
                    os.remove(path=file_path)
        
        

                
        

    def upload_dataset(
        self, 
        dataset:str, 
        localpath: str = 'datasets/'):
        """上传数据集
        - dataset: 数据集名称
        - localpath: 数据集路径, 默认为datasets/
        """
        file = dataset + '.zip'
        file_path = os.path.join(localpath, file)
        dataset_path = os.path.join(localpath, dataset)
        with zipfile.ZipFile(file=file_path, mode='w') as z:
            zip_all_files(dataset_path, z, pre_dir=dataset)
        self.data_bucket.put_object_from_file(key=file, filename=file_path)
        if os.path.exists(file_path):
            os.remove(path=file_path)


    def upload_pretrained(
        self, 
        model, 
        localpath: str = 'plms/'):
        """上传预训练模型
        - model: 模型名称
        - localpath: 预训练模型路径, 默认为plms/
        """
        file = model + '.zip'
        file_path = os.path.join(localpath, file)
        model_path = os.path.join(localpath, model)
        # 注意如果不用with 语法, 如果没有关闭zip文件则解压会报错
        with zipfile.ZipFile(file=file_path, mode='w') as z:
            zip_all_files(model_path, z, model)
        self.model_bucket.put_object_from_file(key=file, filename=file_path)
        if os.path.exists(file_path):
            os.remove(path=file_path)


    def upload_asset(
        self,
        asset,
        localpath: str = './assets/'
    ):
        """上传原始数据
        - asset: 数据名称
        - localpath: 数据的路径, 默认为./assets/
        """
        file = asset + '.zip'
        file_path = os.path.join(localpath, file)
        asset_path = os.path.join(localpath, asset)
        with zipfile.ZipFile(file=file_path, mode='w') as z:
            zip_all_files(asset_path, z, asset)
        self.assets_bucket.put_object_from_file(key=file, filename=file_path)
        if os.path.exists(file_path):
            os.remove(path=file_path)
            
    def upload_corpus(self,
                      corpus,
                      localpath: str= './corpus'):
        file = corpus + '.zip'
        file_path = os.path.join(localpath, file)
        corpus_path = os.path.join(localpath, corpus)
        with zipfile.ZipFile(file=file_path, mode='w') as z:
            zip_all_files(corpus_path, z, corpus)
        self.corpus_bucket.put_object_from_file(key=file, filename=file_path)
        if os.path.exists(file_path):
            os.remove(path=file_path)
            
    def upload_pipeline(self,
                        pipeline,
                        localpath: str='./pipelines'):
        
        file = pipeline + '.zip'
        file_path = os.path.join(localpath, file)
        pipeline_path = os.path.join(localpath, pipeline)
        with zipfile.ZipFile(file=file_path, mode='w') as z:
            zip_all_files(pipeline_path, z, pipeline)
        self.pipe_bucket.put_object_from_file(key=file, filename=file_path)
        if os.path.exists(file_path):
            os.remove(path=file_path)
            
    def delete_object(self, bucket, file):
        file = file + '.zip'
        if bucket == 'dataset':
            self.data_bucket.delete_object(file)
        elif bucket == 'plm':
            self.model_bucket.delete_object(file)
        elif bucket == 'asset':
            self.assets_bucket.delete_object(file)
        elif bucket == 'corpus':
            self.corpus_bucket.delete_object(file)
        elif bucket == 'pipeline':
            self.pipe_bucket.delete_object(file)
            


    
class DataType(str, Enum):
    dataset = 'dataset'
    asset = 'asset'
    plm = 'plm'
    corpus = 'corpus'
    pipeline = 'pipeline'
    
class ListType(str, Enum):
    dataset = 'dataset'
    asset = 'asset'
    plm = 'plm'
    corpus = 'corpus'
    pipeline = 'pipeline'
    all = 'all'


oss = OSSStorer()
app = typer.Typer(help="OSS storage")


@app.command('download')
def download(name: str, type: DataType= DataType.dataset, path: Optional[str]= None) -> None:
    """下载数据
    """
    if type == 'dataset':
        if not path:
            path = './datasets/'
        oss.download_dataset(dataset=name, localpath=path)
        
    elif type == 'asset':
        if not path:
            path = './assets/'
        oss.download_asset(asset=name, localpath=path)
    elif type == 'plm':
        if not path:
            path = './plms/'
        oss.download_plm(model=name, localpath=path)
    elif type == 'corpus':
        if not path:
            path = './corpus/'
        oss.download_corpus(corpus=name, localpath=path)
    

def pad(ls: List, max_length: int, padding = ''):
    if len(ls) > max_length:
        return ls[:max_length]
    else:
        return ls + [padding] * (max_length-len(ls))   
     
@app.command('list')
def list(type : ListType) -> None:
    """显示数据
    """
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    if type != 'all':
        table.add_column(f"{type}", style="dim", width=25) 
        if type == "dataset":
            datasets = oss.list_all_datasets()
            for ds in datasets:
                table.add_row(ds)
            console.print(table)
            # typer.echo(datasets)
        elif type == "asset":
            assets = oss.list_all_assets() 
            for asset in assets:
                table.add_row(asset) 
            console.print(table)
        elif type == "plm":
            plms = oss.list_all_plms()
            for plm in plms:
                table.add_row(plm)
            console.print(table)
        elif type == 'corpus':
            corpus = oss.list_all_corpus()
            for c in corpus:
                table.add_row(c)
            console.print(table)
        elif type == 'pipeline':
            pipelines = oss.list_all_pipelines()
            for pipe in pipelines:
                table.add_row(pipe)
            console.print(table)
    else:
        table.add_column('dataset')
        table.add_column('asset', justify='right')
        table.add_column('plm', justify='right')
        table.add_column('corpus', justify='right')
        table.add_column('pipeline', justify='right')
        datasets = oss.list_all_datasets()
        assets = oss.list_all_assets() 
        plms = oss.list_all_plms()
        corpus = oss.list_all_corpus()
        pipelines = oss.list_all_pipelines()
        max_length = max([len(datasets), len(assets), len(plms), len(corpus), len(pipelines)])
        pad_ds = pad(datasets, max_length)
        pad_asset = pad(assets, max_length)
        pad_plm = pad(plms, max_length)
        pad_corpus = pad(corpus, max_length)
        pad_pipe = pad(pipelines, max_length)
        for ds, asset, plm , corpus, pipe in zip(pad_ds, pad_asset, pad_plm, pad_corpus, pad_pipe):
            table.add_row(ds, asset, plm, corpus, pipe)
        console.print(table)

@app.command('upload')
def upload(name: str, type: DataType = DataType.dataset,  path: str = None ) -> None:
    """上传数据
    """
    console = Console()
    if type == 'dataset':
        if path is None:
            path = './datasets/'
        oss.upload_dataset(dataset=name, localpath=path)
    elif type == 'asset':
        if path is None:
            path = './assets/'
        oss.upload_asset(asset=name, localpath=path)
    elif type == 'plm':
        if path is None:
            path = './plms/'
        try:
            oss.upload_pretrained(model=name, localpath=path)
            console.print('upload plm successed')
        except Exception as e:
            console.print(e)
            console.print('upload plm failed')
    elif type == 'corpus':
        if path is None:
            path = './corpus/'
        try:
            oss.upload_corpus(corpus=name, localpath=path)
            console.print('upload corpus successed')
        except Exception as e:
            console.print(e)
            console.print('upload corpus failed')
            
@app.command('delete')
def delete(name: str, type: DataType= DataType.dataset) -> None:
    """删除数据
    Args:
        name (str): 数据名称
        type (DataType): 类型
    """
    console = Console()
    try:
        oss.delete_object(bucket=type, file=name)
        console.print('delete data successed')
    except:
        console.print('delete data failed')

    
if __name__ == "__main__":
    app()
    

    
    




