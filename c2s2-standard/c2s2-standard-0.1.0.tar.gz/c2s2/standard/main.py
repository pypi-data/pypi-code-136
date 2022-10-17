from c2s2.base.consensus.simple import SimpleConsensusClustering
from c2s2.base.cluster import KMeans
from c2s2.base.perturb import NoiseAdding, IncompletePhenotyping
from c2s2.base.semsim import DummySimilarityKernel, SimilarityMatrixCreator, Phenomizer, read_ic_mica_data
from c2s2.standard.cluster import SpectralClustering
from c2s2.standard.load_hpo_graph import get_hpo_graph_in_networkx
from c2s2.standard.parse_phenopackets import process_phenopackets_directory
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # TODO turn into unit test
    PHENOPACKETS_DIR = r"C:\Users\z184215\Downloads\phenopackets\v2"
    MICA_DICT_PATH = r"C:\Users\z184215\Downloads\term-pair-similarity.csv.gz"

    np_phenopackets = process_phenopackets_directory(PHENOPACKETS_DIR)

    #  lets start with the 4 largest diseases in the dataset
    unique, counts = np.unique(np_phenopackets[:, 2], return_counts=True)
    top_4_diseases = unique[np.argpartition(counts, -4)[-4:]]
    np_phenopackets = np_phenopackets[np.isin(np_phenopackets[:,2], top_4_diseases)]
    np_phenopackets = np_phenopackets[np.argsort(np_phenopackets[:, 2])]

    print("Loaded " + str(len(np_phenopackets)) + " phenopackets.")
    hpo_list = np_phenopackets[:, 0]
    sim_kernel = Phenomizer(read_ic_mica_data(MICA_DICT_PATH))
    sim_matrix_creator = SimilarityMatrixCreator(sim_kernel)
    hpo_graph = get_hpo_graph_in_networkx("https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.json")
    for perturb in [NoiseAdding(number_of_terms_to_add=4, nodes=hpo_graph.nodes()), IncompletePhenotyping(5)]:
        for cluster in [KMeans(), SpectralClustering()]:
            perturb_method = perturb
            clustering_algorithm = cluster
            consensus = SimpleConsensusClustering(k_clusters=6, n_resample=100, sim_matrix_creator=sim_matrix_creator,
                                                  perturb_method=perturb_method, clustering_algorithm=clustering_algorithm)
            print("Initialized, now starting consensus clustering.")
            consensus.consensus_cluster(hpo_list)

            print("Finished clustering, now visualising results...")
            fig, axs = plt.subplots(3, 2)
            axs = axs.flatten()
            for i in range(len(consensus.k_clusters)):
                sns.heatmap(consensus.connectivity_matrix[i, :, :], cmap='Blues', ax=axs[i])
                axs[i].axis('off')
                axs[i].set_title('k =' + str(i + 2))
            plt.suptitle(type(perturb).__name__ + ' & ' + type(cluster).__name__)
            print(consensus.pac)
