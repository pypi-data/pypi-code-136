import warnings
import numpy as np
import pandas as pd
import itertools
import random as rn
import argparse
import time
import os
import sys
#from XGB_model import tvt_xgb
#from SVM_model import tvt_svm
#from RF_model import tvt_rf
#from KNN_model import tvt_knn
#from DNN_model import tvt_dnn
from graph_model import tvt_dl
np.set_printoptions(threshold=sys.maxsize)
#Random seeding
os.environ['PYTHONHASHSEED']='0'
np.random.seed(123)
rn.seed(123)
warnings.filterwarnings('ignore')
# loading data
def model_set(X,Y,split_type='random',FP_type='ECFP4',model_type = 'SVM',model_dir=False,file_name=None,device = 'cpu',difftasks='activity'):

    if model_type == 'gcn':
        # print(difftasks)
        par, bes = tvt_dl(X, Y, split_type=split_type,file_name=file_name,model_name='gcn',model_dir=model_dir,device =device,difftasks=difftasks)
        return par, bes
    elif model_type == 'attentivefp':
        par, bes = tvt_dl(X, Y, split_type=split_type, file_name=file_name, model_name='attentivefp', model_dir=model_dir,device =device,difftasks=difftasks)
        return par,bes
    elif model_type == 'gat':
        par, bes = tvt_dl(X, Y, split_type=split_type, file_name=file_name, model_name='gat',
                            model_dir=model_dir,device =device,difftasks=difftasks)
        return par,bes
    elif model_type == 'mpnn':
        par, bes = tvt_dl(X, Y, split_type=split_type, file_name=file_name, model_name='mpnn',
                            model_dir=model_dir,device =device,difftasks=difftasks)
        return par,bes

def pair_param(file_name,data,split_type,model_type,device,difftasks):#FP_type,
    X = data.cano_smiles
    Y = data['NR-AR']
    model_path = 'model_save/'+model_type
    model_dir = file_name.replace(file_name.split('/')[-1],model_path)
    result_path = 'result_save/' + model_type
    result_dir = file_name.replace(file_name.split('/')[-1], result_path)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    para_name, best_name = os.path.join(result_dir, '_'.join([split_type, model_type, 'para.csv'])), os.path.join(
        result_dir, '_'.join([split_type, model_type, 'best.csv']))
    if os.path.exists(para_name):
        print(para_name,"exists files")
        pass
    else:
        # print(difftasks)
        para,best = model_set(X,Y, split_type=split_type,model_type=model_type,model_dir=model_dir,file_name=file_name,device = device,difftasks=difftasks)
        para.to_csv(para_name,index=False)
        best.to_csv(best_name,index=False)
        pass
    return

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='we must give this para')
    parser.add_argument('--split', default=['scaffold'], nargs='*',choices = ['random','scaffold','cluster'])
    parser.add_argument('--model', default=['gcn'], nargs='*',choices = ['gcn','gat','mpnn','attentivefp'])
    parser.add_argument('--difftasks', default='activity', choices=['activity', 'tox21'])
    parser.add_argument('--device', default='cpu', choices=['cpu', 'gpu'])
    args = parser.parse_args()
    return args
args = parse_args()
file_name = args.file
split = args.split
model = args.model
difftasks = args.difftasks
data = pd.read_csv(file_name,error_bad_lines=False)
device = args.device
dic = {'split':split,'model':model}
hy = pd.DataFrame(list(itertools.product(*dic.values())),columns=dic.keys())

for i in range(len(hy.index.values)):
    split_type = hy.iloc[i].split
    model_type = hy.iloc[i].model
    start_time = time.time()
    a = pair_param(file_name,data,split_type,model_type,device,difftasks)
    use_time = int(time.time() - start_time)
    if use_time >= 10:
        local_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        f = open('../dataset/record_every_model.csv', 'a+')
        f.write(",".join([file_name, split_type,model_type, str(use_time),local_time,device,"\n"]))
        f.close()
