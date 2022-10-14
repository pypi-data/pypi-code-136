import unittest
import numpy as np
from mensajes.hola.saludos import generar_array

class PruebasHola(unittest.TestCase):
    def test_generar_array(self):
        np.testing.assert_array_equal(
            np.array([0,1,2,3,4,5]),
            generar_array(6)
        )

"""
from mensajes.hola.saludos import *  #se puede importar todas las funciones con un "*"
from mensajes.adios.despedida import *



saludar()

saludo()

despedir()
Despedida()
"""



