import matplotlib.pyplot as plt

def plotar_imagem(imagem):
    plt.figure(figsize=(12, 4))
    plt.imshow(imagem, cmap='gray')
    plt.axis('off')
    plt.show()

def plotar_resultado(*args):
    numero_imagens = len(args)
    fig, axis = plt.subplots(nrows=1, ncols = numero_imagens, figsize=(12, 4))
    lista_nomes = ['imagem {}'.format(i) for i in range(1, numero_imagens)]
    lista_nomes.append('Resultado')
    for ax, nome, imagem in zip(axis, lista_nomes, args):
        ax.set_title(nome)
        ax.imshow(imagem, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()
    
def plotar_histograma(imagem):
    fig, axis = plt.subplots(nrows = 1, ncols = 3, figsize = (12, 4), sharex=True, sharey=True)
    lista_cores = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, lista_cores)):
        ax.set_title('{} histograma'.format(color.title()))
        ax.hist(imagem[:, :, index].ravel(), bins = 256, color = color, alpha = 0.8)
    fig.tight_layout()
    plt.show()