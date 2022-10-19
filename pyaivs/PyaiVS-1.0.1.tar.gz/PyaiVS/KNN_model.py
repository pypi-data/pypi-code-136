import time
import joblib
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
import warnings
from script.splitdater import split_dataset
from script.feature_create import create_des
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

from sklearn.metrics import roc_auc_score, confusion_matrix, precision_recall_curve, auc, mean_squared_error, \
    r2_score, mean_absolute_error

import pandas as pd
import numpy as np

def all_one_zeros(data):
    if (len(np.unique(data)) == 2):
        flag = False
    else:
        flag = True
    return flag



start = time.time()
warnings.filterwarnings("ignore")

# the metrics for classification
def statistical(y_true, y_pred, y_pro):
    c_mat = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = list(c_mat.flatten())
    se = tp / (tp + fn)
    sp = tn / (tn + fp)
    precision = tp / (tp + fp)
    acc = (tp + tn) / (tn + fp + fn + tp)
    mcc = (tp * tn - fp * fn) / np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn) + 1e-8)
    auc_prc = auc(precision_recall_curve(y_true, y_pro, pos_label=1)[1],
                  precision_recall_curve(y_true, y_pro, pos_label=1)[0])
    auc_roc = roc_auc_score(y_true, y_pro)
    return precision, se, sp, acc, mcc, auc_prc, auc_roc
def best_model_runing(seed,best_hyper,X,Y,split_type='random',FP_type='ECFP4',task_type='cla',model_dir = False):
    pd_res = []
    n_neighbors_ls = np.arange(1, 20, 2).tolist()
    leaf_size_ls = np.arange(1, 20, 2).tolist()
    if task_type == 'cla':
        while True:
            # data_tr_x, data_va_x, data_te_x, data_tr_y, data_va_y, data_te_y = split_dataset(X, Y,
            #                                                                                      split_type=split_type,
            #                                                                                      valid_need=True,
            #                                                                                      random_state=seed)
            data_x, data_te_x, data_y, data_te_y = split_dataset(X, Y, split_type='random', valid_need=False,
                                                                 random_state=42, train_size=0.90)
            data_tr_x, data_va_x, data_tr_y, data_va_y = split_dataset(data_x, data_y, split_type='random', valid_need=False,
                                                                       random_state=seed, train_size=(8 / 9))
            data_tr_x, data_tr_y = create_des(data_tr_x, data_tr_y, FP_type=FP_type,model_dir=model_dir)
            data_va_x, data_va_y = create_des(data_va_x, data_va_y, FP_type=FP_type,model_dir=model_dir)
            data_te_x, data_te_y = create_des(data_te_x, data_te_y, FP_type=FP_type,model_dir=model_dir)

            if (all_one_zeros(data_tr_y) or all_one_zeros(data_va_y) or all_one_zeros(data_te_y)):
                # print(
                #     '\ninvalid random seed {} due to one class presented in the {} splitted sets...'.format(seed,
                #                                                                                             split_type))
                # print('Changing to another random seed...\n')
                seed = np.random.randint(50, 999999)
            else:

                break
    else :
        data_tr_x, data_va_x, data_te_x, data_tr_y, data_va_y, data_te_y = split_dataset(X, Y, split_type=split_type,
                                                                                         valid_need=True,
                                                                                         random_state=seed)
        data_tr_x, data_tr_y = create_des(data_tr_x, data_tr_y, FP_type=FP_type)
        data_va_x, data_va_y = create_des(data_va_x, data_va_y, FP_type=FP_type)
        data_te_x, data_te_y = create_des(data_te_x, data_te_y, FP_type=FP_type)

    model = KNeighborsClassifier(n_neighbors=n_neighbors_ls[best_hyper['n_neighbors']],leaf_size=leaf_size_ls[best_hyper['leaf_size']],weights='uniform', algorithm='auto', p=2,
                                     metric='minkowski', metric_params=None, n_jobs=None) \
        if task_type == 'cla' else KNeighborsRegressor(n_neighbors=n_neighbors_ls[best_hyper['n_neighbors']],
                                      leaf_size=leaf_size_ls[best_hyper['leaf_size']], weights='uniform', algorithm='auto', p=2, metric='minkowski',
                                 metric_params=None, n_jobs=None)

    model.fit(data_tr_x, data_tr_y)
    num_of_compounds = X.shape[0]
    if task_type == 'cla':
        tr_pred = model.predict_proba(data_tr_x)
        tr_results = [seed, FP_type, split_type, 'tr', num_of_compounds]
        tr_results.extend(statistical(data_tr_y, np.argmax(tr_pred, axis=1), tr_pred[:, 1]))
        pd_res.append(tr_results)
        # validation set
        va_pred = model.predict_proba(data_va_x)
        va_results = [seed, FP_type, split_type, 'va', num_of_compounds]
        va_results.extend(statistical(data_va_y, np.argmax(va_pred, axis=1), va_pred[:, 1]))
        pd_res.append(va_results)
        # test set
        te_pred = model.predict_proba(data_te_x)
        te_results = [seed, FP_type, split_type, 'te', num_of_compounds]
        te_results.extend(statistical(data_te_y, np.argmax(te_pred, axis=1), te_pred[:, 1]))
        pd_res.append(te_results)
    else:
        # training set
        tr_pred = model.predict(data_tr_x)
        tr_results = [seed, FP_type, split_type, 'tr',  num_of_compounds,
                      np.sqrt(mean_squared_error(data_tr_y, tr_pred)), r2_score(data_tr_y, tr_pred),
                      mean_absolute_error(data_tr_y, tr_pred)]
        pd_res.append(tr_results)
        # validation set
        va_pred = model.predict(data_va_x)
        va_results = [seed, FP_type, split_type, 'va',  num_of_compounds,
                      np.sqrt(mean_squared_error(data_va_y, va_pred)), r2_score(data_va_y, va_pred),
                      mean_absolute_error(data_va_y, va_pred)]
        pd_res.append(va_results)
        # test set
        te_pred = model.predict(data_te_x)
        te_results = [seed, FP_type, split_type, 'te',  num_of_compounds,
                      np.sqrt(mean_squared_error(data_te_y, te_pred)), r2_score(data_te_y, te_pred),
                      mean_absolute_error(data_te_y, te_pred)]
        pd_res.append(te_results)

    return pd_res
def tvt_knn(X,Y,split_type='random',FP_type='ECFP4',task_type='cla',model_dir=False):
    random_state = 42
    while True:

        # data_tr_x, data_va_x, data_te_x, data_tr_y, data_va_y, data_te_y = split_dataset(X, Y,
        #                                                                                  split_type=split_type,
        #                                                                                  valid_need=True,
        #                                                                                  random_state=random_state)
        data_x, data_te_x, data_y, data_te_y = split_dataset(X, Y, split_type='random', valid_need=False,
                                                             random_state=random_state, train_size=0.90)
        
        data_tr_x, data_va_x, data_tr_y, data_va_y = split_dataset(data_x, data_y, split_type=split_type, valid_need=False,
                                                                   random_state=random_state, train_size=(8 / 9))

        data_tr_x, data_tr_y = create_des(data_tr_x, data_tr_y, FP_type=FP_type, model_dir=model_dir)
        data_va_x, data_va_y = create_des(data_va_x, data_va_y, FP_type=FP_type, model_dir=model_dir)
        data_te_x, data_te_y = create_des(data_te_x, data_te_y, FP_type=FP_type, model_dir=model_dir)

        if (all_one_zeros(data_tr_y) or all_one_zeros(data_va_y) or all_one_zeros(data_te_y)):
            # print(
            #     '\ninvalid random seed {} due to one class presented in the {} splitted sets...'.format('None',
            #                                                                                             split_type))
            #
            random_state += np.random.randint(50, 999999)
            #
            # print('Changing to another random seed {}\n'.format(random_state))
        else:


            break

    pd_res = []
    OPT_ITERS = 50

    space_ = {'n_neighbors': hp.choice('n_neighbors', np.arange(1, 20, 2).tolist()),
              'leaf_size': hp.choice('leaf_size', np.arange(1, 20, 2).tolist()),

              }
    n_neighbors_ls = np.arange(1, 20, 2).tolist()
    leaf_size_ls = np.arange(1, 20, 2).tolist()
    trials = Trials()
    def hyper_opt(args):
        model = KNeighborsClassifier(**args,weights='uniform', algorithm='auto', p=2, metric='minkowski', metric_params=None, n_jobs=None)\
            if task_type == 'cla' else KNeighborsRegressor(**args,weights='uniform', algorithm='auto', p=2, metric='minkowski', metric_params=None, n_jobs=None)

        model.fit(data_tr_x, data_tr_y)

        val_preds = model.predict_proba(data_va_x) if task_type == 'cla' else model.predict(data_va_x)
        loss = 1 - roc_auc_score(data_va_y, val_preds[:, 1]) if task_type == 'cla' else np.sqrt(
            mean_squared_error(data_va_y, val_preds))
        return {'loss': loss, 'status': STATUS_OK}


    # start hyper-parameters optimization
    best_results = fmin(hyper_opt, space_, algo=tpe.suggest, max_evals=OPT_ITERS, trials=trials, show_progressbar=False)

    best_model = KNeighborsClassifier(n_neighbors=n_neighbors_ls[best_results['n_neighbors']],
                                      leaf_size=leaf_size_ls[best_results['leaf_size']], weights='uniform', algorithm='auto', p=2, metric='minkowski',
                                 metric_params=None, n_jobs=None)\
        if task_type == 'cla' else KNeighborsRegressor(n_neighbors=n_neighbors_ls[best_results['n_neighbors']],
                                      leaf_size=leaf_size_ls[best_results['leaf_size']], weights='uniform', algorithm='auto', p=2, metric='minkowski',
                                 metric_params=None, n_jobs=None)
    best_model.fit(data_tr_x, data_tr_y)
    if model_dir :
        model_name = str(model_dir) +'/%s_%s_%s_%s'%(split_type,task_type,FP_type,'KNN_bestModel.pkl')
        joblib.dump(best_model,model_name)
    num_of_compounds = len(X)
    if task_type == 'cla':
        tr_pred = best_model.predict_proba(data_tr_x)
        tr_results = [FP_type, split_type, 'tr', num_of_compounds,
                      n_neighbors_ls[best_results['n_neighbors']],
                      leaf_size_ls[best_results['leaf_size']]]
        tr_results.extend(statistical(data_tr_y, np.argmax(tr_pred, axis=1), tr_pred[:, 1]))
        pd_res.append(tr_results)
        # validation set
        va_pred = best_model.predict_proba(data_va_x)
        va_results = [FP_type, split_type, 'va', num_of_compounds,
                      n_neighbors_ls[best_results['n_neighbors']],
                      leaf_size_ls[best_results['leaf_size']],]
        va_results.extend(statistical(data_va_y, np.argmax(va_pred, axis=1), va_pred[:, 1]))
        pd_res.append(va_results)
        # test set
        te_pred = best_model.predict_proba(data_te_x)
        te_results = [FP_type, split_type, 'te', num_of_compounds,
                      n_neighbors_ls[best_results['n_neighbors']],
                      leaf_size_ls[best_results['leaf_size']]]
        te_results.extend(statistical(data_te_y, np.argmax(te_pred, axis=1), te_pred[:, 1]))
        pd_res.append(te_results)
        para_res = pd.DataFrame(pd_res, columns=['FP_type', 'split_type', 'type','num_of_compounds',
               'n_neighbors', 'leaf_size', 'precision',
                 'se', 'sp','acc', 'mcc', 'auc_prc', 'auc_roc'])
    else:
        tr_pred = best_model.predict(data_tr_x)
        tr_results = [FP_type, split_type, 'tr', num_of_compounds,
                      n_neighbors_ls[best_results['n_neighbors']],
                      leaf_size_ls[best_results['leaf_size']],np.sqrt(mean_squared_error(data_tr_y, tr_pred)), r2_score(data_tr_y, tr_pred),
                      mean_absolute_error(data_tr_y, tr_pred)]

        pd_res.append(tr_results)
        # validation set
        va_pred = best_model.predict(data_va_x)
        va_results = [FP_type, split_type, 'va', num_of_compounds,
                      n_neighbors_ls[best_results['n_neighbors']],
                      leaf_size_ls[best_results['leaf_size']],np.sqrt(mean_squared_error(data_va_y, va_pred)), r2_score(data_tr_y, tr_pred),
                      mean_absolute_error(data_va_y, va_pred)]

        pd_res.append(va_results)
        # test set
        te_pred = best_model.predict(data_te_x)
        te_results = [FP_type, split_type, 'te', num_of_compounds,
                      n_neighbors_ls[best_results['n_neighbors']],
                      leaf_size_ls[best_results['leaf_size']],np.sqrt(mean_squared_error(data_te_y, te_pred)), r2_score(data_te_y, te_pred),
                      mean_absolute_error(data_te_y, te_pred)]

        pd_res.append(te_results)

        para_res = pd.DataFrame(pd_res, columns=['FP_type', 'split_type', 'type', 'num_of_compounds',
                                                 'n_neighbors', 'leaf_size','rmse', 'r2', 'mae'])


    pd_res = []
    for i in range(10):
        item = best_model_runing((i+1)*500,best_results,X,Y,split_type=split_type,FP_type=FP_type,task_type=task_type,model_dir=model_dir)
        pd_res.extend(item)

    if task_type == 'cla':
        best_res = pd.DataFrame(pd_res, columns=['seed', 'FP_type', 'split_type', 'type',
                                                 'num_of_compounds', 'precision', 'se', 'sp',
                                                 'acc', 'mcc', 'auc_prc', 'auc_roc'])
    else:
        best_res = pd.DataFrame(pd_res, columns=['seed', 'FP_type', 'split_type', 'type',
                                                 'num_of_compounds', 'rmse', 'r2', 'mae'])
    return  para_res,best_res

# df= pd.read_csv('/data/jianping/bokey/OCAICM/dataset/TEN/TEN_pro.csv')
# b,p = tvt_knn(df['Smiles'],df['oppo'])
# print(b.columns)
