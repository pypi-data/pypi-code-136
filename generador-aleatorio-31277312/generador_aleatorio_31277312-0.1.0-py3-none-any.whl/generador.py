import random

from .frases import frases


def obtener_frase() -> dict:
    """
    Devuelve una frase aleatoria

    Obtiene una frase aletoria de nuestro repositorio de frases celebres

    :return: la frase seleccionada
    :rtype: dict
    """

    return frases[random.randint(0, len(frases) - 1)]
