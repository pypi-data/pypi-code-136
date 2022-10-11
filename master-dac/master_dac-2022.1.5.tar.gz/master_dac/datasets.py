import logging
import sys


def amal():
    try:
        from datamaestro import prepare_dataset
    except:
        logging.info("Datamaestro n'est pas installé (ce ne devrait pas arriver)")
        sys.exit(1)

    for dataset_id in [
        "com.lecun.mnist",
        "edu.uci.boston",
        "org.universaldependencies.french.gsd",
        "edu.stanford.aclimdb",
        "edu.stanford.glove.6b.50"
    ]:
        logging.info("Preparing %s", dataset_id)
        prepare_dataset(dataset_id)
