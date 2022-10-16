import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def encontrar_diferenca(imagem1, imagem2):
    assert imagem1.shape == imagem2.shape, "Especifique 2 imagens de mesmo formato."
    imagem1_cinza = rgb2gray(imagem1)
    imagem2_cinza = rgb2gray(imagem2)
    (score, diferenca_imagem) = structural_similarity(imagem1_cinza, imagem2_cinza, full=True)
    print("Similaridade das imagens:", score)
    diferenca_imagem_normalizada =(diferenca_imagem-np.min(diferenca_imagem))/(np.max(diferenca_imagem)-np.min(diferenca_imagem))
    return diferenca_imagem_normalizada

def transferir_histograma(imagem1, imagem2):
    imagem_combinada = match_histograms(imagem1, imagem2, multichannel=True)
    return imagem_combinada