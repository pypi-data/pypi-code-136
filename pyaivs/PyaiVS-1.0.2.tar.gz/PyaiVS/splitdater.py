import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
import deepchem as dc
from rdkit import Chem
from rdkit import DataStructs
from rdkit.ML.Cluster import Butina
from rdkit.Chem import rdFingerprintGenerator
def tanimoto_distance_matrix(fp_list):
    """Calculate distance matrix for fingerprint list"""
    dissimilarity_matrix = []

    for i in range(1, len(fp_list)):
        # Compare the current fingerprint against all the previous ones in the list
        similarities = DataStructs.BulkTanimotoSimilarity(fp_list[i], fp_list[:i])
        # Since we need a distance matrix, calculate 1-x for every element in similarity matrix
        dissimilarity_matrix.extend([1 - x for x in similarities])
    return dissimilarity_matrix
def cluster_fingerprints(fingerprints, cutoff=0.2):
    """Cluster fingerprints
    Parameters:
        fingerprints
        cutoff: threshold for the clustering
    """
    # Calculate Tanimoto distance matrix
    distance_matrix = tanimoto_distance_matrix(fingerprints)
    # Now cluster the data with the implemented Butina algorithm:
    clusters = Butina.ClusterData(distance_matrix, len(fingerprints), cutoff, isDistData=True)
    clusters = sorted(clusters, key=len, reverse=True)
    return clusters
def split_dataset(X,Y,split_type='random',valid_need = False,train_size=0.80,random_state=42):
    if valid_need is True:
        if split_type == 'random':
            X_train, X_rest, Y_train, Y_rest = train_test_split(X, Y, train_size=train_size, random_state=random_state)
            X_valid, X_test, Y_valid, Y_test = train_test_split(X_rest, Y_rest, train_size=0.5, random_state=random_state)
        elif split_type == 'scaffold':
            chembl_data = pd.concat([X, Y], axis=1)
            chembl_data.columns = ['Smiles', 'activity']
            with dc.utils.UniversalNamedTemporaryFile(mode='w') as tmpfile:
                chembl_data.to_csv(tmpfile.name)
                featurizer = dc.feat.CircularFingerprint(size=1024)
                loader = dc.data.CSVLoader(["activity"], feature_field="Smiles", featurizer=featurizer)
                active = loader.create_dataset(tmpfile.name)
                scaffoldsplitter = dc.splits.ScaffoldSplitter()
                train, rest = scaffoldsplitter.train_test_split(active,seed=random_state,frac_train=train_size)
                train_df = pd.DataFrame(train.ids, columns=['Smiles'])
                rest_df = pd.DataFrame(rest.ids, columns=['Smiles'])
                train = chembl_data[chembl_data['Smiles'].isin(train_df['Smiles'].tolist())]
                rest = chembl_data[chembl_data['Smiles'].isin(rest_df['Smiles'].tolist())]
                X_train = train.Smiles
                X_rest = rest.Smiles
                Y_train = train['activity']
                Y_rest = rest['activity']
                X_valid, X_test, Y_valid, Y_test = train_test_split(X_rest, Y_rest, train_size=0.5,
                                                                    random_state=random_state)

        elif split_type == 'cluster':
            compound_df = pd.concat([X, Y], axis=1)
            compound_df.columns = ['Smiles', 'activity']
            compounds = []
            for _, chembl_id, smiles in compound_df[["activity", "Smiles"]].itertuples():
                compounds.append((Chem.MolFromSmiles(smiles), chembl_id))
            rdkit_gen = rdFingerprintGenerator.GetRDKitFPGenerator(maxPath=5)
            fingerprints = [rdkit_gen.GetFingerprint(mol) for mol, idx in compounds]
            clusters = cluster_fingerprints(fingerprints, cutoff=0.2)
            cluster_centers = [compounds[c[0]] for c in clusters]
            sorted_clusters = []
            Singletons = []
            for cluster in clusters:
                if len(cluster) <= 1:
                    Singletons.append(cluster)
                    continue  # Singletons
                sorted_fingerprints = [rdkit_gen.GetFingerprint(compounds[i][0]) for i in cluster]
                similarities = DataStructs.BulkTanimotoSimilarity(
                    sorted_fingerprints[0], sorted_fingerprints[1:]
                )
                similarities = list(zip(similarities, cluster[1:]))
                similarities.sort(reverse=True)
                sorted_clusters.append((len(similarities), [i for _, i in similarities]))
                sorted_clusters.sort(reverse=True)
            selected_molecules = cluster_centers.copy()
            index = 0
            pending = int(len(compounds) * train_size) - len(selected_molecules)
            while pending > 0 and index < len(sorted_clusters):
                tmp_cluster = sorted_clusters[index][1]
                if sorted_clusters[index][0] > 10:
                    num_compounds = int(sorted_clusters[index][0] * train_size)
                else:
                    num_compounds = len(tmp_cluster)
                if num_compounds > pending:
                    num_compounds = pending
                selected_molecules += [compounds[i] for i in tmp_cluster[:num_compounds]]
                index += 1
                pending = int(len(compounds) * train_size) - len(selected_molecules)
            test = [i for i in compounds if i not in selected_molecules]

            train = selected_molecules
            X_train = pd.DataFrame(train, columns=['Smiles', 'activity'])['Smiles']
            X_train = X_train.apply(lambda x: Chem.MolToSmiles(x))
            Y_train = pd.DataFrame(train, columns=['Smiles', 'activity'])['activity']
            X_rest = pd.DataFrame(test, columns=['Smiles', 'activity'])
            X_rest = sklearn.utils.shuffle(X_rest, random_state=random_state)
            X_valid = X_rest.iloc[:int(len(X_rest) / 2), :]['Smiles']
            X_valid = X_valid.apply(lambda x: Chem.MolToSmiles(x))
            X_test = X_rest.iloc[int(len(X_rest) / 2):, :]['Smiles']
            X_test = X_test.apply(lambda x: Chem.MolToSmiles(x))
            Y_valid = X_rest.iloc[:int(len(X_rest) / 2), :]['activity']
            Y_test = X_rest.iloc[int(len(X_rest) / 2):, :]['activity']
        return X_train,X_valid,X_test,Y_train,Y_valid,Y_test
    else:
        if split_type == 'random':
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = train_size, random_state=random_state)
        elif split_type == 'scaffold':
            chembl_data = pd.concat([X, Y], axis=1)
            chembl_data.columns = ['Smiles', 'activity']
            with dc.utils.UniversalNamedTemporaryFile(mode='w') as tmpfile:
                chembl_data.to_csv(tmpfile.name)
                featurizer = dc.feat.CircularFingerprint(size=1024)
                loader = dc.data.CSVLoader(["activity"], feature_field="Smiles", featurizer=featurizer)
                active = loader.create_dataset(tmpfile.name)
                scaffoldsplitter = dc.splits.ScaffoldSplitter()
                train, test = scaffoldsplitter.train_test_split(active,frac_train = train_size,seed=random_state)
                train_df = pd.DataFrame(train.ids, columns=['Smiles'])
                test_df = pd.DataFrame(test.ids, columns=['Smiles'])
                train = chembl_data[chembl_data['Smiles'].isin(train_df['Smiles'].tolist())]
                test = chembl_data[chembl_data['Smiles'].isin(test_df['Smiles'].tolist())]
                X_train = train.Smiles
                X_test = test.Smiles
                Y_train = train.activity
                Y_test = test.activity
        elif split_type == 'cluster':
            compound_df = pd.concat([X, Y], axis=1)
            compound_df.columns = ['Smiles', 'activity']
            compound_df['inter_smiles'] = compound_df['Smiles'].apply(lambda x: Chem.MolToSmiles(Chem.MolFromSmiles(x)))
            compounds = []
            for _, chembl_id, smiles in compound_df[["activity", "inter_smiles"]].itertuples():
                compounds.append((Chem.MolFromSmiles(smiles), chembl_id))
            rdkit_gen = rdFingerprintGenerator.GetRDKitFPGenerator(maxPath=5)
            fingerprints = [rdkit_gen.GetFingerprint(mol) for mol, idx in compounds]
            clusters = cluster_fingerprints(fingerprints, cutoff=0.2)
            cluster_centers = [compounds[c[0]] for c in clusters]
            sorted_clusters = []
            Singletons = []
            for cluster in clusters:
                if len(cluster) <= 1:
                    Singletons.append(cluster)
                    continue  # Singletons
                sorted_fingerprints = [rdkit_gen.GetFingerprint(compounds[i][0]) for i in cluster]
                similarities = DataStructs.BulkTanimotoSimilarity(
                    sorted_fingerprints[0], sorted_fingerprints[1:]
                )
                similarities = list(zip(similarities, cluster[1:]))
                similarities.sort(reverse=True)
                sorted_clusters.append((len(similarities), [i for _, i in similarities]))
                sorted_clusters.sort(reverse=True)
            selected_molecules = cluster_centers.copy()
            index = 0
            pending = int(len(compounds) * train_size) - len(selected_molecules)
            while pending > 0 and index < len(sorted_clusters):
                tmp_cluster = sorted_clusters[index][1]
                if sorted_clusters[index][0] > 10:
                    num_compounds = int(sorted_clusters[index][0] * train_size)
                else:
                    num_compounds = len(tmp_cluster)
                if num_compounds > pending:
                    num_compounds = pending
                selected_molecules += [compounds[i] for i in tmp_cluster[:num_compounds]]
                index += 1
                pending = int(len(compounds) * train_size) - len(selected_molecules)
            test = [i for i in compounds if i not in selected_molecules]
            train = selected_molecules
            X_train = pd.DataFrame(train, columns=['Smiles', 'activity'])['Smiles']
            X_train = X_train.apply(lambda x: Chem.MolToSmiles(x))
            Y_train = pd.DataFrame(train, columns=['Smiles', 'activity'])['activity']
            X_test = pd.DataFrame(test, columns=['Smiles', 'activity'])['Smiles']
            X_test = X_test.apply(lambda x: Chem.MolToSmiles(x))
            Y_test = pd.DataFrame(test, columns=['Smiles', 'activity'])['activity']
        return  X_train, X_test, Y_train, Y_test




