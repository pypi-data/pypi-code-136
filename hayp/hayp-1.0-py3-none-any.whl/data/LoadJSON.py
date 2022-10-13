from data.HandleJSON import HandleJSON
from logger.logger import log
import json

class LoadJSON:

    '''
    Clase encargada de cargar el archivo JSON
    '''

    def __init__(self, path, id_net):
        '''
        Metodo __init__ para inicializar los valores del Objeto, recibe los parametros:
        :param path: ruta del archivo a cargar
        :param id_net: id de la red a cargar
        '''
        self.__path = path
        self.__id_net = id_net
        self.__net = None

    def laod_net(self):
        '''
        Metodo encargado de cargar la red y asignarla a la propiedad self.__net
        '''
        try:
            with HandleJSON(self.__path, 'r') as document:
                data = json.load(document)
                self.__net = data[self.__id_net]
        except Exception as e:
            log.error(f'Load JSON Error: {e}')

    def load_places(self):
        '''
        Metodo encargado de cargar los lugares de la red, retorna
        :return: Diccionario con los lugares de la red
        '''
        if self.__net is None:
            self.laod_net()
        places = dict(self.__net['places'])
        return places

    def load_transitions(self):
        '''
        Metodo encargado de cargar las transiciones de la red, retorna
        :return: Lista con las transiciones de la red
        '''
        if self.__net is None:
            self.laod_net()
        transitions = list(self.__net['transitions'])
        return transitions

    def load_inputs(self):
        '''
        Metodo encargado de cargar las funciones de entrada de la red, retorna
        :return: Diccionario con las funciones de entrada de la red
        '''
        if self.__net is None:
            self.laod_net()
        inputs = dict(self.__net['inputs'])
        return inputs

    def load_outputs(self):
        '''
        Metodo encargado de cargar las funciones de salida de la red, retorna
        :return: Diccionario con las funciones de salida de la red
        '''
        if self.__net is None:
            self.laod_net()
        outputs = dict(self.__net['outputs'])
        return outputs

    def load_initial_marking(self):
        '''
        Metodo encargado de cargar la marcacion inicial de la red, retorna
        :return: Lista con la marcacion inicial de la red
        '''
        places = self.load_places()
        initial_marking = list(places.values())
        return initial_marking

    def load_name(self):
        if self.__net is None:
            self.laod_net()
        name = str(self.__net['name'])
        return name

    def load_ids(self):
        try:
            with HandleJSON(self.__path, 'r') as document:
                data = dict(json.load(document))
                return list(data.keys())
        except Exception as e:
            log.error(f'Error al cargar el archivo: {e}')


if __name__ == '__main__':
    loadJson = LoadJSON('../documentosJSON.json', '02')
    print(loadJson.load_ids())
