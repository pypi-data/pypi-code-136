import os
import pandas as pd
from dgl.data.chem import csv_dataset, smiles_to_bigraph, MoleculeCSVDataset
from PyaiVS.gnn_utils import AttentiveFPBondFeaturizer, AttentiveFPAtomFeaturizer, collate_molgraphs, \
     Meter
from torch.utils.data import DataLoader
from dgl.model_zoo.chem import MPNNModel, GCNClassifier, GATClassifier, AttentiveFP
import multiprocessing as mp
from rdkit.Chem import AllChem
from rdkit.Chem import rdmolfiles
import os
import time
s =time.time()


import torch
torch.set_num_threads(5)
def run_an_eval_epoch(model, data_loader, args):
    f = open(args['output'],'w+')

    f.write('cano_smiles,pred_prop\n')
    # print(args['output'])
    model.eval()
    # eval_metric = Meter()
    smile_list = {}
    count  = 0
    with torch.no_grad():
        for batch_id, batch_data in enumerate(data_loader):
            eval_metric = Meter()
            smiles, bg, labels, masks = batch_data
            smile_list[count]=smiles
            atom_feats = bg.ndata.pop('h')
            bond_feats = bg.edata.pop('e')
            # transfer the data to device(cpu or cuda)
            outputs = model(bg, atom_feats) if args['model'] in ['gcn', 'gat'] else model(bg, atom_feats,bond_feats)
            # smile_list.append(smiles)
            eval_metric.update(outputs, labels, torch.tensor([count]))
            roc_score = eval_metric.compute_metric('pred')
            if roc_score.tolist()[0][0] >= args['prop']:
                f.write('{},{}\n'.format(smiles[0],round(roc_score.tolist()[0][0],2)))
                # print(smiles[0],round(roc_score.tolist()[0][0],2))
            count += 1
            torch.cuda.empty_cache()
        f.close()
#file=screen_file, sep=sep,  prop=prop, out_dir=out_dir
def screen(file='', sep=',', models=None,prop=0.5, smiles_col='Smiles',out_dir=None):
    AtomFeaturizer = AttentiveFPAtomFeaturizer
    BondFeaturizer = AttentiveFPBondFeaturizer
    print(models)
    model_type = models.split('/')[-2]
    args = {'model': model_type,'prop':prop}
    outputs = os.path.join(out_dir,file.split('/')[-1].replace('.csv','_screen_{}_{}.csv'.format(args['prop'],args['model'])))
    print(outputs)
    if os.path.exists(outputs):
        print(outputs,'has done')
    else:
        args['output'] =outputs
        my_df = pd.read_csv(file,engine='python',sep=sep)
        print(my_df.columns)
        my_dataset: MoleculeCSVDataset = csv_dataset.MoleculeCSVDataset(my_df.iloc[:, :], smiles_to_bigraph, AtomFeaturizer,
                                                                            BondFeaturizer, smiles_col,
                                                                            file.replace('.csv', '.bin'))
        train_loader = DataLoader(my_dataset,shuffle=True,batch_size=1,
                                      collate_fn=collate_molgraphs)
        if 'gcn' in models:
            chf = models.split('_')[-1].split('.')[0]
            ghf = models.split('_')[-2]
            best_model = GCNClassifier(in_feats=AtomFeaturizer.feat_size('h'),
                                               gcn_hidden_feats=eval(ghf),
                                               n_tasks=1,
                                               classifier_hidden_feats=eval(chf))

        elif 'gat' in models:
            chf = models.split('_')[-1].split('.')[0]
            nh = models.split('_')[-2]
            ghf = models.split('_')[-3]

            best_model = GATClassifier(in_feats=AtomFeaturizer.feat_size('h'),
                                       gat_hidden_feats=eval(ghf),
                                       num_heads=eval(nh), n_tasks=1,
                                       classifier_hidden_feats=eval(chf))
        elif 'attentivefp' in models:
            num_layer = eval(models.split('_')[-4])
            num_timestep  = eval(models.split('_')[-3])
            graph_feat_size = eval(models.split('_')[-2])
            dropout = eval(models.split('_')[-1].split('.')[0])
            best_model = AttentiveFP(node_feat_size=AtomFeaturizer.feat_size('h'),
                                     edge_feat_size=BondFeaturizer.feat_size('e'),
                                     num_layers=num_layer,
                                     num_timesteps=num_timestep,
                                     graph_feat_size=graph_feat_size,
                                     output_size=1,
                                     dropout=dropout)
        else:
            node_hidden_dim =eval(models.split('_')[-3])
            edge_hidden_dim = eval(models.split('_')[-2])
            num_layer_set2set = eval(models.split('_')[-1].split('.')[0])
            best_model = MPNNModel(node_input_dim=AtomFeaturizer.feat_size('h'),
                                   edge_input_dim=BondFeaturizer.feat_size('e'),
                                   output_dim=1,
                                   node_hidden_dim=node_hidden_dim,
                                   edge_hidden_dim=edge_hidden_dim,
                                   num_layer_set2set=num_layer_set2set)
        best_model.load_state_dict(torch.load(models, map_location='cpu')['model_state_dict'])
        run_an_eval_epoch(best_model, train_loader, args)

# if __name__ == '__main__':
#     model_path ='/data/jianping/bokey/library/dataset/GLS1/model_save/gcn/gcn_scaffold_GLS1_0_0.031623_(256, 256)_128.pth'
#     dir = '/data/jianping/web-ocaicm/bokey/BACE/BACE.csv'
#     output = '/data/jianping/bokey/library/dataset/GLS1/screen'
#     if not os.path.exists(output):
#         os.makedirs(output)
#     file = dir
#     if os.path.isdir(file):
#         p = mp.Pool(processes=6)
#         #
#         for file_content in os.listdir(file):
#             if '.csv' in file_content:
#                 file_path = os.path.join(file,file_content)
#                 param = {'file':file_path,  'prop':0.75, 'smiles_col':'smiles','output':output}
#                 get = p.apply_async(screen,kwds = param)
#         p.close()
#         p.join()
#     elif os.path.isfile(file):
#         screen(file=file,prop=0.5,smiles_col='Smiles',output =output)
#     else:
#         pass
#     # file_list = ['/data/jianping/bokey/library/database/total_db_csv/NC_320593.csv',
#     #              '/data/jianping/bokey/library/database/total_db_csv/Express_Pick _20mg_01_2019_774293_Part2.csv',
#     #              '/data/jianping/bokey/library/database/total_db_csv/Express_Pick _20mg_01_2019_774293_Part1.csv',
#     #              '/data/jianping/bokey/library/database/total_db_csv/DC03_239319.csv',
#     #              '/data/jianping/bokey/library/database/total_db_csv/DC02_350000.csv',
#     #              '/data/jianping/bokey/library/database/total_db_csv/DC01_350000.csv']
#
#     # def mol_check(smiles):
#     #     try:
#     #         mol = AllChem.MolFromSmiles(smiles)
#     #         rdmolfiles.CanonicalRankAtoms(mol)
#     #         return 1
#     #     except:
#     #         return 0
#     # def datacheck(file):
#     #
#     #     my_df = pd.read_csv(file, sep=';', usecols=[i for i in range(5)], engine='python')
#     #     my_df.columns = open(file, 'r').readline().split(';')[:5]
#     #     # print('pass')
#     #     # my_df.columns = [smiles_col]
#     #     # my_df = pd.read_csv(file,sep=';')
#     #     my_df['index'] = my_df.index
#     #     my_df = my_df[['smiles', 'index']]
#     #     my_df['check'] = my_df['smiles'].apply(mol_check)
#     #     my_df =my_df[my_df['check']==1]
#     #     output =file.replace('.csv','_graph.csv')
#     #     my_df.to_csv(output,index=False)
#     #
#     #
#     # p = mp.Pool(processes=6)
#     # for file in file_list:
#     #     file =file.replace('.csv','_graph.csv')
#     #     screen(file=file,prop=0.5,smiles_col='smiles')
#     # p.close()
#     # p.join()