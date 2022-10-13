class HandleJSON:

    '''
    Clase para cargar el archivo JSON
    '''

    def __init__(self, path, type):
        '''
        Metodo inicializador de la clase, recibe los parametros:
        :param path: Indica la ruta del archivo JSON a cargar
        :param type: Indica el tipo de tratamiento que se le dara al archivo JSON
        '''
        self.path = path
        self.type = type

    def __enter__(self):
        '''
        Metodo que se ejecuta cuando se carga el archivo, abre el archivo y lo retorna, retorna:
        :return: Objeto del archivo cargado.
        '''
        self.path = open(self.path, self.type)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        Metodo que se ejecuta al momento en que termina la carga del archivo, cierra el archivo si está abierto, recibe los parametros:
        :param exc_type: Tipo de excepcion, si la hay
        :param exc_val: Valor de la expecion, si la hay
        :param exc_tb: Errores, si los hay
        '''
        if self.path:
            self.path.close()