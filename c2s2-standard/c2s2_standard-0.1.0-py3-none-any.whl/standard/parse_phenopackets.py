from google.protobuf.json_format import Parse
from phenopackets import Phenopacket
from glob import glob
import os
import numpy as np


def get_hpo_from_phenopacket(phenopacket):
    """
    Get HPO ids, HPO labels and diseases from a phenopacket

    :param phenopacket: phenopacket object

    """
    hpo_ids, hpo_labels = [], []
    for feature in phenopacket.phenotypic_features:
        if not feature.excluded:
            hpo_ids.append(feature.type.id)
            hpo_labels.append(feature.type.label)

    assert len(hpo_ids) == len(hpo_labels)  # these should be same length

    omim_diagnoses = []
    for disease in phenopacket.diseases:
        omim_diagnoses.append(disease.term.id)
    return hpo_ids, hpo_labels, omim_diagnoses


def process_phenopackets_directory(path_to_dir):
    """
    Get all phenopackets in a directory and extract phenotypic features and (if available) diseases
    :param path_to_dir: path to directory with phenopackets v2
    """
    files_in_dir = glob(os.path.join(path_to_dir, '*'))

    np_results = np.zeros((len(files_in_dir), 3), dtype=object)

    for i, file_path in enumerate(files_in_dir):
        encodings = ['utf-8', 'utf-16']  # can add more if necessary
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as jsfile:
                    phenopacket = Parse(message=Phenopacket(), text=jsfile.read())
                break
            except UnicodeDecodeError:
                pass
        hpo_ids, hpo_labels, omim_diagnoses = get_hpo_from_phenopacket(phenopacket)
        np_results[i, 0] = hpo_ids
        np_results[i, 1] = hpo_labels
        assert len(omim_diagnoses) == 1  # check that they only have 1 diagnoses for now
        np_results[i, 2] = omim_diagnoses[0]
    return np_results
