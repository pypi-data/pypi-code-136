import numpy as np
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

def get_info(file_name=None,models=None,split=None, FP=None):
    dataset = file_name.split('/')[-2]
    path = os.path.join(os.path.join(file_name.split(dataset)[0],dataset),'result_save')
    des_model = [model for model in models if model in ['KNN','SVM','RF','XGB','DNN']]
    graph_model = [model for model in models if model not in ['KNN','SVM','RF','XGB','DNN']]
    info =pd.DataFrame()
    for model in des_model:
        model_dir = os.path.join(path,model)
        for des in FP:
            for sp in split:
                file = os.path.join(model_dir,'_'.join([sp,model,des,'best.csv']))
                df = pd.read_csv(file)
                data= df.groupby('type')['se','precision','auc_roc'].mean()
                data=data.reset_index()
                data['model']=model
                data['des'] = des
                data['split'] = sp
                info = pd.concat([info,data],ignore_index=True)
    for model in graph_model:
        model_dir = os.path.join(path,model)

        for sp in split:
            file = os.path.join(model_dir,'_'.join([sp,model,'best.csv']))
            df = pd.read_csv(file)
            data= df.groupby('type')['se','precision','auc_roc'].mean()
            data = data.reset_index()
            data['model']=model
            data['des'] = model
            data['split'] = sp
            info = pd.concat([info,data],ignore_index=True)
    info =info.sort_values('auc_roc',ascending=False)
    info_save = file_name.replace('.csv','_auc.csv')
    print(info_save)
    info.to_csv(info_save,index=False)

# def show_model(file_name=None,models=None,split=None, FP=None):
#     dataset = file_name.split('/')[-2]
#     model_path = os.path.join(os.path.join(file_name.split(dataset)[0], dataset), 'model_save')
#     para_path = os.path.join(os.path.join(file_name.split(dataset)[0], dataset), 'model_save')
#     des_model = [model for model in models if model in ['KNN', 'SVM', 'RF', 'XGB', 'DNN']]
#     graph_model = [model for model in models if model not in ['KNN', 'SVM', 'RF', 'XGB', 'DNN']]
#     for model in des_model:
#         if model =='DNN':
#             pass
#         else:
#             for sp in split:
#                 for des in FP:
#                     param_file = '_'.join([sp,model,des,'para.csv'])
def para(file_name):
    info_save = file_name.replace('.csv', '_auc.csv')
    data = pd.read_csv(info_save)
    data=data[data['type']=='te']
    data = data.sort_values('auc_roc', ascending=False)
    data['f1_score'] = data.apply(lambda x:(2*(x['precision']*x['se'])/(x['precision']+x['se'])),axis=1)
    data=data.sort_values('f1_score',ascending=False)
    data['dist'] = data.apply(lambda x: ((1 - x['f1_score']) ** 2 + (1 - x['auc_roc']) ** 2) ** 0.5, axis=1)
    data = data.sort_values('dist')
    data = data[['model', 'des', 'split', 'auc_roc', 'f1_score', 'dist']]
    data_save = file_name.replace('.csv', '_f1score.csv')
    data.to_csv(data_save,index=False)
    print(data)
# file = '/data/jianping/bokey/OCAICM/dataset/GLS1/GLS1.csv'
# para(file)