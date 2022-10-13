import zipfile
import wget
import os


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)       
    else:
        print('This is not zip')


# KGC dataset
def load_KGCdata(dataname):
    path = './data/'
    if not os.path.exists(path):
        os.makedirs(path)
    # 根据数据集名称下载对应的压缩包
    if dataname == "NELL":
        wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-KGC/ZSL_Dataset/NELL.zip", path)
        unzip_file(zip_src= path + dataname + '.zip', dst_dir= path)
    elif dataname == "Wiki":
        wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-KGC/ZSL_Dataset/Wiki.zip", path)
        unzip_file(zip_src= path + dataname + '.zip', dst_dir= path)


# IMAGE dataset
def load_IMGCdata(dataname):
    path = './data/'
    if not os.path.exists(path):
        os.makedirs(path)
    #  根据数据集名称下载对应的压缩包
    if dataname == "AWA":
        wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-IMGC/ZSL_Dataset/AwA2.zip", path)
        unzip_file(zip_src= path + 'AwA2.zip', dst_dir= path)
    else:
        path = './data/ImageNet/'
        if not os.path.exists(path):
            os.makedirs(path)
        # Res101_Features.zip
        wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-IMGC/ZSL_Dataset/ImageNet/Res101_Features.zip", path)
        unzip_file(zip_src= path + 'Res101_Features.zip', dst_dir= path)
        # split.mat
        wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-IMGC/ZSL_Dataset/ImageNet/split.mat", path)
        # w2v.mat
        wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-IMGC/ZSL_Dataset/ImageNet/w2v.mat", path)
        # ImNet_A
        wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-IMGC/ZSL_Dataset/ImageNet/ImNet_A.zip", path)
        unzip_file(zip_src= path + 'ImNet_A.zip', dst_dir= path)
        # ImNet_O
        wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-IMGC/ZSL_Dataset/ImageNet/ImNet_O.zip", path)
        unzip_file(zip_src= path + 'ImNet_O.zip', dst_dir= path)

def load_Onto_triples():
    path = './data/'
    if not os.path.exists(path):
        os.makedirs(path)
    wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-KGC/Ontological_Schema/Onto_triples.zip", path)
    unzip_file(zip_src= path + 'Onto_triples.zip', dst_dir= path)

def load_KG_triples():
    path = './data/'
    if not os.path.exists(path):
        os.makedirs(path)
    wget.download("https://krr-nas.cs.ox.ac.uk/2022/ISWC-KZSL-Tutorial/ZS-IMGC/KG/KG_triples.zip", path)
    unzip_file(zip_src= path + 'KG_triples.zip', dst_dir= path)