import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def encontrar_diferenca(imagem1, imagem2):
    assert imagem1.shape == imagem2.shape, "Especifique 2 imagens com a mesma forma."
    imagem_cinza1 = rgb2gray(imagem1)
    imagem_cinza2 = rgb2gray(imagem2)
    (score, diferenca_de_imagem) = structural_similarity(imagem_cinza1, imagem_cinza2, full=True)
    print("A Similaridade das Imagens é: ", score)
    diferenca_de_imagem_normalizada = (diferenca_de_imagem-np.min(diferenca_de_imagem))/(np.max(diferenca_de_imagem)-np.min(diferenca_de_imagem))
    return diferenca_de_imagem_normalizada

def transferir_histograma(imagem1, imagem2):
    imagem_correspondente = match_histograms(imagem1, imagem2, multichannel=True)
    return imagem_correspondente