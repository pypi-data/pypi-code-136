import logging
import torch


def get_device(gpu: int):
    if gpu is not None and gpu >= 0:
        logging.info("Use device: CUDA:{}".format(gpu))
        return torch.device("cuda:{}".format(gpu))
    else:
        logging.info("Use device: CPU")
        return torch.device("cpu")
