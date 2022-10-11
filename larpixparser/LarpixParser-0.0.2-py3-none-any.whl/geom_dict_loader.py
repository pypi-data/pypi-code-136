import pickle

def load_geom_dict(geom_dict_path):
    with open(geom_dict_path, "rb") as f_geom_dict:
        geom_dict = pickle.load(f_geom_dict)
    return geom_dict
