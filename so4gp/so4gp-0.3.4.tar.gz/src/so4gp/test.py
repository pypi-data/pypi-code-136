from src.so4gp import so4gp
import json

f_path = 'DATASET.csv'
# dgp = so4gp.ClusterGP(f_path, e_prob=0.1)
dgp = so4gp.GRAANK(data_source=f_path, min_sup=0.5, eq=False)
# dgp = so4gp.AntGRAANK(f_path)
# dgp = so4gp.GeneticGRAANK(f_path)
# dgp = so4gp.ParticleGRAANK(f_path)
# dgp = so4gp.RandomGRAANK(f_path)
# dgp = so4gp.HillClimbingGRAANK(f_path)
out_json = dgp.discover()
print(out_json)
# print(so4gp.analyze_gps('DATASET.csv', 0.5, dgp.gradual_patterns, approach='dfs'))

# out_obj = json.loads(out_json)
# print(out_obj["Invalid Count"])

# gp = so4gp.ExtGP()
# gp.add_items_from_list(['3-', '1-', '0+'])
# print(gp.to_string())

# d_gp = so4gp.DfsDataGP('DATASET.csv', 0.5)
# d_gp.init_transaction_ids()
# print(d_gp.item_to_tids)
