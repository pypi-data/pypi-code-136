import torch
import numpy as np
import pandas as pd
from dnn_torch_utils import Meter, MyDataset, EarlyStopping, MyDNN, collate_fn, set_random_seed
from hyperopt import fmin, tpe, hp, rand, STATUS_OK, Trials, partial
import sys
import copy
from torch.utils.data import DataLoader
from torch.nn import BCEWithLogitsLoss, MSELoss
import gc
import time
start_time = time.time()
from sklearn.model_selection import train_test_split
import warnings
from splitdater import split_dataset
from feature_create  import create_des
warnings.filterwarnings('ignore')
torch.backends.cudnn.enabled = True
torch.backends.cudnn.benchmark = True
set_random_seed(seed=43)


def run_a_train_epoch(model, data_loader, loss_func, optimizer, args):
    model.train()

    train_metric = Meter()  # for each epoch
    for batch_id, batch_data in enumerate(data_loader):
        Xs, Ys, masks = batch_data

        # transfer the data to device(cpu or cuda)
        Xs, Ys, masks = Xs.to(args['device']), Ys.to(args['device']), masks.to(args['device'])

        outputs = model(Xs)
        loss = (loss_func(outputs, Ys) * (masks != 0).float()).mean()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        outputs.cpu()
        Ys.cpu()
        masks.cpu()
        loss.cpu()
#        torch.cuda.empty_cache()

        train_metric.update(outputs, Ys, masks)
    if args['reg']:
        rmse_score = np.mean(train_metric.compute_metric(args['metric']))  # in case of multi-tasks
        mae_score = np.mean(train_metric.compute_metric('mae'))  # in case of multi-tasks
        r2_score = np.mean(train_metric.compute_metric('r2'))  # in case of multi-tasks
        return {'rmse': rmse_score, 'mae': mae_score, 'r2': r2_score}
    else:
        roc_score = np.mean(train_metric.compute_metric(args['metric']))  # in case of multi-tasks
        prc_score = np.mean(train_metric.compute_metric('prc_auc'))  # in case of multi-tasks
        return {'roc_auc': roc_score, 'prc_auc': prc_score}


def run_an_eval_epoch(model, data_loader, args):
    model.eval()

    eval_metric = Meter()
    with torch.no_grad():
        for batch_id, batch_data in enumerate(data_loader):
            Xs, Ys, masks = batch_data
            # transfer the data to device(cpu or cuda)
            Xs, Ys, masks = Xs.to(args['device']), Ys.to(args['device']), masks.to(args['device'])

            outputs = model(Xs)

            outputs.cpu()
            Ys.cpu()
            masks.cpu()
#            torch.cuda.empty_cache()
            eval_metric.update(outputs, Ys, masks)
    if args['reg']:
        rmse_score = np.mean(eval_metric.compute_metric(args['metric']))  # in case of multi-tasks
        mae_score = np.mean(eval_metric.compute_metric('mae'))  # in case of multi-tasks
        r2_score = np.mean(eval_metric.compute_metric('r2'))  # in case of multi-tasks
        return {'rmse': rmse_score, 'mae': mae_score, 'r2': r2_score}
    else:
        roc_score = np.mean(eval_metric.compute_metric(args['metric']))  # in case of multi-tasks
        prc_score = np.mean(eval_metric.compute_metric('prc_auc'))  # in case of multi-tasks
        stats = eval_metric.compute_metric('statistical')
        return {'roc_auc': roc_score, 'prc_auc': prc_score,'statistical':stats}


def get_pos_weight(Ys):
    Ys = torch.tensor(np.nan_to_num(Ys), dtype=torch.float32)
    num_pos = torch.sum(Ys, dim=0)
    num_indices = torch.tensor(len(Ys))
    return (num_indices - num_pos) / num_pos


def standardize(col):
    return (col - np.mean(col)) / np.std(col)


def all_one_zeros(series):
    if (len(series.dropna().unique()) == 2):
        flag = False
    else:
        flag = True
    return flag

# file_name = '/home/ubuntu/Downloads/total_data.csv'  # './dataset/bace_moe_pubsubfp.csv'
# dataset_all = pd.read_csv(file_name)
# split_type = 'random'
# FP_type= 'ECFP4'
# dataset_all = dataset_all[['id', 'canoincal', 'RBA']]
# df = dataset_all
# df['RBA'] = df['RBA'].astype('int')
# df['Activitys'] = df['RBA'].apply(lambda x: 0 if x < 95 else 1)
# X = df['canoincal']
# Y = df['Activitys']


def best_model_runing(seed, opt_res, X, Y, split_type='random', FP_type='ECFP4'):
    # construct the model based on the optimal hyper-parameters
    hidden_unit1_ls = [64, 128, 256, 512]
    hidden_unit2_ls = [64, 128, 256, 512]
    hidden_unit3_ls = [64, 128, 256, 512]
    opt_hidden_units = [hidden_unit1_ls[opt_res['hidden_unit1']], hidden_unit2_ls[opt_res['hidden_unit2']],
                        hidden_unit3_ls[opt_res['hidden_unit3']]]
    # 50 repetitions based on the best model

    pd_res = []
    epochs = 300  # training epoch

    batch_size = 128
    patience = 50
    # device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # os.environ["CUDA_VISIBLE_DEVICES"] = gpu_id
    # if device == 'cuda':
    #    torch.cuda.set_device(eval(gpu_id))  # gpu device id
    reg = False
    args = {'device': device, 'metric': 'rmse' if reg else 'roc_auc', 'epochs': epochs,
            'patience': patience, 'task': '', 'reg': reg}

    data_tr_x, data_va_x, data_te_x, data_tr_y, data_va_y, data_te_y = split_dataset(X, Y, split_type=split_type,
                                                                                     valid_need=True, random_state=seed)
    data_tr_x, data_tr_y = create_des(data_tr_x, data_tr_y, FP_type=FP_type)
    data_va_x, data_va_y = create_des(data_va_x, data_va_y, FP_type=FP_type)
    data_te_x, data_te_y = create_des(data_te_x, data_te_y, FP_type=FP_type)
    data_tr_y = data_tr_y.values.reshape(-1, 1)
    data_va_y = data_va_y.values.reshape(-1, 1)
    data_te_y = data_te_y.values.reshape(-1, 1)

    # else:
    #     training_data, data_te = train_test_split(dataset, test_size=0.1, random_state=split)
    #     # the training set was further splited into the training set and validation set
    #     data_tr, data_va = train_test_split(training_data, test_size=0.1, random_state=split)
    # prepare data for training
    # training set

    # dataloader
    train_dataset = MyDataset(data_tr_x, data_tr_y)
    validation_dataset = MyDataset(data_va_x, data_va_y)
    test_dataset = MyDataset(data_te_x, data_te_y)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    validation_loader = DataLoader(validation_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    inputs = data_tr_x.shape[1]
    best_model = MyDNN(inputs=inputs, hideen_units=opt_hidden_units, outputs=1,
                       dp_ratio=opt_res['dropout'], reg=reg)

    best_optimizer = torch.optim.Adadelta(best_model.parameters(), weight_decay=opt_res['l2'])
    file_name = './model_save/%s_%s_%s_%.4f_%d_%d_%d_%.4f_early_stop_%d.pth' % (
    FP_type, split_type, args['task'], opt_res['dropout'],
    hidden_unit1_ls[opt_res['hidden_unit1']],
    hidden_unit1_ls[opt_res['hidden_unit2']],
    hidden_unit1_ls[opt_res['hidden_unit3']],
    opt_res['l2'], seed)
    if reg:
        loss_func = MSELoss(reduction='none')
        stopper = EarlyStopping(mode='lower', patience=patience, filename=file_name)
    else:
        pos_weights = get_pos_weight(Y.values)
        loss_func = BCEWithLogitsLoss(reduction='none', pos_weight=pos_weights.to(args['device']))
        stopper = EarlyStopping(mode='higher', patience=patience, filename=file_name)
    best_model.to(device)

    for j in range(epochs):
        # training
        st = time.time()
        run_a_train_epoch(best_model, train_loader, loss_func, best_optimizer, args)
        end = time.time()
        # early stopping
        train_scores = run_an_eval_epoch(best_model, train_loader, args)
        val_scores = run_an_eval_epoch(best_model, validation_loader, args)
        early_stop = stopper.step(val_scores[args['metric']], best_model)
        if early_stop:
            break
        print(
            'task:{} repetition {:d}/{:d} epoch {:d}/{:d}, training {} {:.3f}, validation {} {:.3f}, time:{:.3f}S'.format(
                args['task'], seed, 3, j + 1, epochs, args['metric'], train_scores[args['metric']],
                args['metric'],
                val_scores[args['metric']], end - st))
        stopper.load_checkpoint(best_model)
    tr_scores = run_an_eval_epoch(best_model, train_loader, args)

    tr_results = [seed,FP_type, split_type, 'tr',tr_scores['statistical'][0], tr_scores['statistical'][1],
                  tr_scores['statistical'][2],
                  tr_scores['statistical'][2] / tr_scores['statistical'][1],
                  tr_scores['statistical'][4], tr_scores['statistical'][5],
                  tr_scores['statistical'][6], tr_scores['statistical'][7], tr_scores['statistical'][8],
                  tr_scores['statistical'][9],
                  tr_scores['statistical'][10], tr_scores['statistical'][11], tr_scores['prc_auc'],
                  tr_scores['roc_auc']]

    val_scores = run_an_eval_epoch(best_model, validation_loader, args)
    va_results = [ seed, FP_type, split_type, 'tr', val_scores['statistical'][0], val_scores['statistical'][1],
                  val_scores['statistical'][2],
                  val_scores['statistical'][2] / val_scores['statistical'][1],
                  val_scores['statistical'][4], val_scores['statistical'][5],
                  val_scores['statistical'][6], val_scores['statistical'][7], val_scores['statistical'][8],
                  val_scores['statistical'][9],
                  val_scores['statistical'][10], val_scores['statistical'][11], val_scores['prc_auc'],
                  val_scores['roc_auc']]
    te_scores = run_an_eval_epoch(best_model, test_loader, args)
    te_results = [ seed, FP_type, split_type, 'tr', te_scores['statistical'][0], te_scores['statistical'][1],
                  te_scores['statistical'][2],
                  te_scores['statistical'][2] / te_scores['statistical'][1],
                  te_scores['statistical'][4], te_scores['statistical'][5],
                  te_scores['statistical'][6], te_scores['statistical'][7], te_scores['statistical'][8],
                  te_scores['statistical'][9],
                  te_scores['statistical'][10], te_scores['statistical'][11], te_scores['prc_auc'],
                  te_scores['roc_auc']]
    pd_res.append(tr_results);pd_res.append(va_results), pd_res.append(te_results)



    return pd_res

def tvt_dnn(X,Y,split_type='random',FP_type='ECFP4'):
    hyper_paras_space = {'l2': hp.uniform('l2', 0, 0.01),
                         'dropout': hp.uniform('dropout', 0, 0.5),
                         'hidden_unit1': hp.choice('hidden_unit1', [64, 128, 256, 512]),
                         'hidden_unit2': hp.choice('hidden_unit2', [64, 128, 256, 512]),
                         'hidden_unit3': hp.choice('hidden_unit3', [64, 128, 256, 512])}

    task_type = 'cla'  # 'cla' or 'reg'
    # file_name = 'clintox_moe_pubsubfpc.csv'  # 'bace_moe_pubsubfp.csv'
    # task_type = 'cla'  # 'cla' or 'reg'
    reg = True if task_type == 'reg' else False
    epochs = 300  # training epoch

    batch_size = 128
    patience = 50
    opt_iters = 50

    # device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # os.environ["CUDA_VISIBLE_DEVICES"] = gpu_id
    # if device == 'cuda':
    #    torch.cuda.set_device(eval(gpu_id))  # gpu device id
    args = {'device': device, 'metric': 'rmse' if reg else 'roc_auc', 'epochs': epochs,
            'patience': patience, 'task': '', 'reg': reg}

    # preprocess data



    data_tr_x, data_va_x, data_te_x, data_tr_y, data_va_y, data_te_y = split_dataset(X, Y, split_type=split_type,
    valid_need=True)

    tasks = '1'

    data_tr_x, data_tr_y = create_des(data_tr_x, data_tr_y, FP_type=FP_type)
    data_va_x, data_va_y = create_des(data_va_x, data_va_y, FP_type=FP_type)
    data_te_x, data_te_y = create_des(data_te_x, data_te_y, FP_type=FP_type)
    data_tr_y = data_tr_y.values.reshape(-1,1 )
    data_va_y = data_va_y.values.reshape(-1,1 )
    data_te_y = data_te_y.values.reshape(-1,1 )
    print(len(data_tr_y),data_va_y,len(data_te_y))
    # dataloader
    train_dataset = MyDataset(data_tr_x, data_tr_y)
    validation_dataset = MyDataset(data_va_x, data_va_y)
    test_dataset = MyDataset(data_te_x, data_te_y)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    validation_loader = DataLoader(validation_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    inputs = data_tr_x.shape[1]
    if not reg:
        pos_weights = get_pos_weight(Y.values)


    def hyper_opt(hyper_paras):
        hidden_units = [hyper_paras['hidden_unit1'], hyper_paras['hidden_unit2'], hyper_paras['hidden_unit3']]
        my_model = MyDNN(inputs=inputs, hideen_units=hidden_units, dp_ratio=hyper_paras['dropout'],
                         outputs=1, reg=reg)
        optimizer = torch.optim.Adadelta(my_model.parameters(), weight_decay=hyper_paras['l2'])
        file_name = './model_save/%s_%s_%s_%.4f_%d_%d_%d_%.4f_early_stop.pth' % (FP_type,split_type,args['task'], hyper_paras['dropout'],
                                                              hyper_paras['hidden_unit1'],
                                                              hyper_paras['hidden_unit2'],
                                                              hyper_paras['hidden_unit3'],
                                                              hyper_paras['l2'])
        if reg:
            loss_func = MSELoss(reduction='none')
            stopper = EarlyStopping(mode='lower', patience=patience, filename=file_name)
        else:
            loss_func = BCEWithLogitsLoss(reduction='none', pos_weight=pos_weights.to(args['device']))
            stopper = EarlyStopping(mode='higher', patience=patience, filename=file_name)
        my_model.to(device)
        for i in range(epochs):
            # training
            run_a_train_epoch(my_model, train_loader, loss_func, optimizer, args)

            # early stopping
            val_scores = run_an_eval_epoch(my_model, validation_loader, args)

            early_stop = stopper.step(val_scores[args['metric']], my_model)

            if early_stop:
                break
        stopper.load_checkpoint(my_model)
        val_scores = run_an_eval_epoch(my_model, validation_loader, args)
        feedback = val_scores[args['metric']] if reg else (1 - val_scores[args['metric']])

        my_model.cpu()
    #    torch.cuda.empty_cache()
        gc.collect()
        return feedback


    # start hyper-parameters optimization
    trials = Trials()  # 通过Trials捕获信息
    print('******hyper-parameter optimization is starting now******')
    opt_res = fmin(hyper_opt, hyper_paras_space, algo=tpe.suggest, max_evals=opt_iters, trials=trials)

    # hyper-parameters optimization is over
    print('******hyper-parameter optimization is over******')
    print('the best hyper-parameters settings for ' + args['task'] + ' are:  ', opt_res)

    # construct the model based on the optimal hyper-parameters
    hidden_unit1_ls = [64, 128, 256, 512]
    hidden_unit2_ls = [64, 128, 256, 512]
    hidden_unit3_ls = [64, 128, 256, 512]
    opt_hidden_units = [hidden_unit1_ls[opt_res['hidden_unit1']], hidden_unit2_ls[opt_res['hidden_unit2']],
                        hidden_unit3_ls[opt_res['hidden_unit3']]]
    best_model = MyDNN(inputs=inputs, hideen_units=opt_hidden_units, outputs=1,
                       dp_ratio=opt_res['dropout'], reg=reg)
    best_file_name = './model_save/%s_%s_%s_%.4f_%d_%d_%d_%.4f_early_stop.pth' % (FP_type,split_type,args['task'], opt_res['dropout'],
                                                               hidden_unit1_ls[opt_res['hidden_unit1']],
                                                               hidden_unit1_ls[opt_res['hidden_unit2']],
                                                               hidden_unit1_ls[opt_res['hidden_unit3']],
                                                               opt_res['l2'])

    best_model.load_state_dict(torch.load(best_file_name, map_location=device)['model_state_dict'])
    best_model.to(device)
    tr_scores = run_an_eval_epoch(best_model, train_loader, args)
    val_scores = run_an_eval_epoch(best_model, validation_loader, args)
    te_scores = run_an_eval_epoch(best_model, test_loader, args)
    pd_res = []
    tr_results = [FP_type, split_type, 'tr',  tr_scores['statistical'][0], tr_scores['statistical'][1],
                              tr_scores['statistical'][2],
                              tr_scores['statistical'][2]/tr_scores['statistical'][1],
                              opt_hidden_units,[opt_res['l2'],opt_res['dropout']],tr_scores['statistical'][4],tr_scores['statistical'][5],
                  tr_scores['statistical'][6],tr_scores['statistical'][7],tr_scores['statistical'][8],tr_scores['statistical'][9],
                  tr_scores['statistical'][10],tr_scores['statistical'][11],tr_scores['prc_auc'],tr_scores['roc_auc']]
    va_results = [FP_type, split_type, 'va',  val_scores['statistical'][0], val_scores['statistical'][1],
                              val_scores['statistical'][2],
                              val_scores['statistical'][2]/val_scores['statistical'][1],
                              opt_hidden_units,[opt_res['l2'],opt_res['dropout']],val_scores['statistical'][4],val_scores['statistical'][5],
                  val_scores['statistical'][6],val_scores['statistical'][7],val_scores['statistical'][8],val_scores['statistical'][9],
                  val_scores['statistical'][10],val_scores['statistical'][11],val_scores['prc_auc'],val_scores['roc_auc']]
    te_results = [FP_type, split_type, 'te',  te_scores['statistical'][0], te_scores['statistical'][1],
                              te_scores['statistical'][2],
                              te_scores['statistical'][2]/te_scores['statistical'][1],
                              opt_hidden_units,[opt_res['l2'],opt_res['dropout']],te_scores['statistical'][4],te_scores['statistical'][5],
                  te_scores['statistical'][6],te_scores['statistical'][7],te_scores['statistical'][8],te_scores['statistical'][9],
                  te_scores['statistical'][10],te_scores['statistical'][11],te_scores['prc_auc'],te_scores['roc_auc']]
    pd_res.append(tr_results)
    pd_res.append(va_results)
    pd_res.append(te_results)
    para_res = pd.DataFrame(pd_res, columns=['FP_type', 'split_type', 'type','num_of_compounds',
                'postives',
                'negtives', 'negtives/postives',
                'para1', 'para2',
                'tn', 'fp', 'fn', 'tp', 'se', 'sp',
                'acc', 'mcc', 'auc_prc', 'auc_roc'])
    # para_res.to_csv('dnn_first.csv',index=False)
    print('training set:', tr_scores)
    print('validation set:', val_scores)
    print('test set:', te_scores)

    pd_res = []
    for i in range(3):  # pro 3
        item = best_model_runing((i + 1) * 500,opt_res, X, Y, split_type=split_type, FP_type=FP_type)
        pd_res.extend(item)
    best_res = pd.DataFrame(pd_res, columns=['seed', 'FP_type', 'split_type', 'type',
                                             'num_of_compounds', 'postives',
                                             'negtives', 'negtives/postives',
                                             'tn', 'fp', 'fn', 'tp', 'se', 'sp',
                                             'acc', 'mcc', 'auc_prc', 'auc_roc'])


    return para_res,best_res


# para,beat = tvt_dnn(X,Y,split_type='random',FP_type='ECFP4')
# print(para,beat)

