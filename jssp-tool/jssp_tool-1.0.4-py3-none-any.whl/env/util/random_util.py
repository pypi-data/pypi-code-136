import os
import torch
import random
import gym
import numpy as np


def set_random_seed(random_seed: int):
    """
    Setup all possible random seeds so results can be reproduced
    """
    os.environ["PYTHONHASHSEED"] = str(random_seed)
    torch.manual_seed(random_seed)
    torch.cuda.manual_seed_all(random_seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.manual_seed(random_seed)
    # tf.set_random_seed(random_seed) # if you use tensorflow
    random.seed(random_seed)
    np.random.seed(random_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(random_seed)
        torch.cuda.manual_seed(random_seed)
    if hasattr(gym.spaces, "prng"):
        gym.spaces.prng.seed(random_seed)
