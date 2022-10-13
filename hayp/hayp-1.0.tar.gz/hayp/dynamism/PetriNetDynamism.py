import numpy as np

class PetriNetDynamism:

    @staticmethod
    def create_matrix(functions, places, transitions, type):
        matrix = np.zeros(shape=(len(transitions), len(places)))
        row = 0 if type else 1
        col = 1 if type else 0
        for key, function in functions.items():
            place_ind = places.index(function[row])
            transitions_ind = transitions.index(function[col])
            matrix[transitions_ind][place_ind] += 1
        return matrix

    @staticmethod
    def get_ej(transitions, trans_shoot):
        ej = np.zeros(shape=len(transitions))
        ind_trans = transitions.index(trans_shoot)
        ej[ind_trans] += 1
        return ej

    @staticmethod
    def get_ejs(transitions, shoots):
        ej = np.zeros(shape=len(transitions))
        for shoot in shoots:
            ind_trans = transitions.index(shoot[0])
            ej[ind_trans] = shoot[1]
        return ej

    @staticmethod
    def transition_enable(transitions, marking, matrix_input, trans_shoot):
        ej = PetriNetDynamism.get_ej(transitions, trans_shoot)
        array_aux = np.dot(ej, matrix_input)
        return np.all(np.less_equal(array_aux, marking))

    @staticmethod
    def transitions_enabled(transitions, marking, matrix_input):
        enabled = []
        for transition in transitions:
            if PetriNetDynamism.transition_enable(transitions, marking, matrix_input, transition):
                enabled.append(transition)
        return enabled

    @staticmethod
    def shoot_transition(marking, transitions, matrix, trans_shoot):
        ej = PetriNetDynamism.get_ej(transitions, trans_shoot)
        new_marking = marking + (np.dot(ej, matrix))
        return new_marking

    @staticmethod
    def shoot_burst(marking, transitions, matrix, trans):
        ejs = PetriNetDynamism.get_ejs(transitions, trans)
        new_marking = marking + (np.dot(ejs, matrix))
        return new_marking

    @staticmethod
    def create_matrix_d(functions, places, transitions):
        return PetriNetDynamism.create_matrix(functions[1], places, transitions, False) - PetriNetDynamism.create_matrix(functions[0], places, transitions, True)
