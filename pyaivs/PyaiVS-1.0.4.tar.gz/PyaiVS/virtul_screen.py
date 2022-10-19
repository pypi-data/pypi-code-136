import os
import multiprocessing as mp
from PyaiVS import ml_screener
from PyaiVS import dl_screener
from PyaiVS import dnn_screener
def model_screen(model=None,FP= None,split=None,screen_file=None,prop = 0.5,sep = ',',model_dir=None,smiles_col =None):
    split = split if type(split) != type(None) else 'random'
    model = model if type(model) != type(None) else 'SVM'
    FP = FP if type(FP) != type(None) else 'MACCS'
    FP_list = ['2d-3d', 'MACCS', 'ECFP4', 'pubchem', 'gcn', 'gat', 'attentivefp', 'mpnn']
    split_list = ['random', 'scaffold', 'cluster']
    model_list = ['SVM', 'KNN', 'DNN', 'RF', 'XGB', 'gcn', 'gat', 'attentivefp', 'mpnn']
    assert len(set(list([split])) - set(split_list)) == 0, '{} element need in {}'.format(split, split_list)
    assert len(set(list([model])) - set(model_list)) == 0, '{} element need in {}'.format(model, model_list)
    assert len(set(list([FP])) - set(FP_list)) == 0, '{} element need in {}'.format(FP, FP_list)
    assert os.path.exists(model_dir),'no such model_dir {}'.format(model_dir)
    assert len(set(list([screen_file.split('.')[-1]])) - set(
        list(['csv', 'txt', 'tsv']))) == 0, '{} need in ["csv","txt","tsv"]'.format(screen_file.split('.')[-1])
    if model in ['SVM', 'KNN',  'RF', 'XGB']:
        model_file = '_'.join([split,'cla',FP,model,'bestModel.pkl'])
        model_path = os.path.join(os.path.join(model_dir,model),model_file)
        assert os.path.exists(model_path),'no such model_path {}'.format(model_path)
        out_dir = model_dir.replace('model_save','screen')
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        if os.path.isdir(screen_file):
            p = mp.Pool(processes=4)
            for file_content in os.listdir(screen_file):
                file_path = os.path.join(screen_file, file_content)
                param = {'file': file_path, 'sep': sep, 'models': model_path, 'prop': prop, 'out_dir': out_dir}
                get = p.apply_async(ml_screener.cir_file, kwds=param)
            p.close()
            p.join()
        elif os.path.isfile(screen_file):
            ml_screener.cir_file(file=screen_file, sep=sep, models=model_path, prop=prop, out_dir=out_dir)
        else:
            print('What\'s this ?')
    elif model =='DNN':
        result_dir = model_dir.replace('model_save', 'result_save')
        result_file = os.path.join(os.path.join(result_dir, model), '_'.join([split, model, FP,'para.csv']))
        model_param = open(result_file, 'r').readlines()[1].replace(']','').replace('[','').replace('\"','').replace(' ','').split(',')[3:8]
        model_param = [param if len(param)< 5 else '{:5f}'.format(float(param))[:6] for param in model_param]
        model_path = []
        for file in os.listdir(os.path.join(model_dir, model)):
            count = 0
            for param in model_param:
                if param in file:
                    count += 1
            if count == len(model_param) :
                model_path.append(os.path.join(os.path.join(model_dir, model), file))
        if len(model_path) > 0:
            model_path = model_path[0]
            out_dir = model_dir.replace('model_save', 'screen')
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            if os.path.isdir(screen_file):
                p = mp.Pool(processes=4)
                for file_content in os.listdir(screen_file):
                    file_path = os.path.join(screen_file, file_content)
                    param = {'file': file_path, 'sep': sep, 'models': model_path, 'prop': prop, 'out_dir': out_dir,'smiles_col':smiles_col}
                    get = p.apply_async(dnn_screener.screen, kwds=param)
                p.close()
                p.join()
            elif os.path.isfile(screen_file):
                dnn_screener.screen(file=screen_file, sep=sep, models=model_path, prop=prop, out_dir=out_dir,smiles_col=smiles_col)
            else:
                print('What\'s this ?')
    else:
        result_dir = model_dir.replace('model_save','result_save')
        result_file = os.path.join(os.path.join(result_dir,model),'_'.join([split,model,'para.csv']))
        model_param = open(result_file,'r').readlines()[1].replace("\"",'').replace(" ",'').split(',')[:-9]
        model_param = [i.replace(')','').replace('(','') if len(i)<15 else i[:6]  for i in model_param]
        model_path = []
        for file in os.listdir(os.path.join(model_dir,model)):
            count=0
            for param in model_param:
                if param in file:
                    count+=1
            if count==len(model_param):
                model_path.append(os.path.join(os.path.join(model_dir,model),file))
        if len(model_path)>0:
            model_path = model_path[0]
            out_dir = model_dir.replace('model_save', 'screen')
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            if os.path.isdir(screen_file):
                p = mp.Pool(processes=4)
                for file_content in os.listdir(screen_file):
                    file_path = os.path.join(screen_file, file_content)
                    param = {'file': file_path, 'sep': sep, 'models': model_path, 'prop': prop, 'out_dir': out_dir,'smiles_col':smiles_col}
                    get = p.apply_async(dl_screener.screen, kwds=param)
                p.close()
                p.join()
            elif os.path.isfile(screen_file):
                dl_screener.screen(file=screen_file, sep=sep, models=model_path, prop=prop, out_dir=out_dir,smiles_col=smiles_col)
            else:
                print('What\'s this ?')




        else:
            assert len(model_path)==1, 'no such model file'




# model_screen(model=None,FP= None,split='cluster',screen_file='/data/jianping/web-ocaicm/bokey/BACE/BACE.csv',prop = 0.5,sep = ',',model_dir='/data/jianping/bokey/OCAICM/dataset/chembl31/model_save',smiles_col='Smiles')
