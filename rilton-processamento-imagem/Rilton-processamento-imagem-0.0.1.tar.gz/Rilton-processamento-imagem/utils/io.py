import re
from skimage.io import imread, imsave

def ler_imagem(caminho, e_cinza = False):
    imagem = imread(caminho, as_gray = e_cinza)
    return imagem

def salvar_imagem(imagem, caminho):
    imsave(caminho, imagem)