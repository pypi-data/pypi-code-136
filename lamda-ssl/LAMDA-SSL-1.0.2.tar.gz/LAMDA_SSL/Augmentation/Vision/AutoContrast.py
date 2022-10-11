from LAMDA_SSL.Base.Transformer import  Transformer
import torchvision.transforms.functional as F
import PIL
import torch
import numpy as np

class AutoContrast(Transformer):
    def __init__(self):
        super().__init__()


    def transform(self,X):
        if isinstance(X,np.ndarray):
            X=PIL.Image.fromarray(X)
        if isinstance(X,PIL.Image.Image):
            X=PIL.ImageOps.autocontrast(X)
            return X
        elif isinstance(X,torch.Tensor):
            X = F.autocontrast(X)
            return X
        else:
            raise ValueError('No data to augment')