from data.LoadJSON import LoadJSON
from net.PetriNet import PetriNet
from exception.HapyException import HapyException
from dynamism.PetriNetDynamism import PetriNetDynamism as pnd
from dynamism.PetriNetDraw import PetriNetDraw
import os

def create_petri_net(path, id_net):
    if os.path.isfile(path):
        lj = LoadJSON(path, id_net)
        if id_net in lj.load_ids():
            name = lj.load_name()
            places = lj.load_places()
            transitions = lj.load_transitions()
            inputs = lj.load_inputs()
            outputs = lj.load_outputs()
            initial_marking = lj.load_initial_marking()
            return PetriNet(name, places, transitions, inputs, outputs, initial_marking)
        else:
            raise HapyException('El id enviado no se encuentra en los datos del JSON...')
    else:
        raise HapyException('La ruta del archivo enviado no existe...')

def transitions_enabled(petri_net):
    transitions = petri_net.transitions
    places_dict = petri_net.places
    places = list(places_dict.keys())
    marking = petri_net.current_marking
    inputs = petri_net.inputs
    matrix_input = pnd.create_matrix(inputs, places, transitions, True)
    return pnd.transitions_enabled(transitions, marking, matrix_input)

def transition_enable(petri_net, transition):
    transitions = petri_net.transitions
    marking = petri_net.current_marking
    places_dict = petri_net.places
    places = list(places_dict.keys())
    inputs = petri_net.inputs
    matrix_input = pnd.create_matrix(inputs, places, transitions, True)
    if transition in transitions:
        return pnd.transition_enable(transitions, marking, matrix_input, transition)
    else:
        raise HapyException('La transicion a disparar no se encuentra establecida en la red...')

def shoot_transition(petri_net, trans_shoot):
    if transition_enable(petri_net, trans_shoot):
        transitions = petri_net.transitions
        current_marking = petri_net.current_marking
        inputs = petri_net.inputs
        outputs = petri_net.outputs
        places = list(petri_net.places.keys())
        functions = [inputs, outputs]
        matrix = pnd.create_matrix_d(functions, places, transitions)
        new_marking = pnd.shoot_transition(current_marking, transitions, matrix, trans_shoot)
        petri_net.current_marking = new_marking
    else:
        raise HapyException('La transicion a disparar no esta habilitada...')

def shoot_burst(petri_net, *args):
    transitions = petri_net.transitions
    current_marking = petri_net.current_marking
    inputs = petri_net.inputs
    outputs = petri_net.outputs
    places = list(petri_net.places.keys())
    functions = [inputs, outputs]
    matrix = pnd.create_matrix_d(functions, places, transitions)
    new_marking = pnd.shoot_burst(current_marking, transitions, matrix, args)
    petri_net.current_marking = new_marking

def draw_petri_net_with_initial_marking(petri_net):
    draw = PetriNetDraw(petri_net)
    draw.draw_petri_net_with_initial_marking(petri_net)

def draw_petri_net_with_current_marking(petri_net):
    draw = PetriNetDraw(petri_net)
    draw.draw_petri_net_with_current_marking(petri_net)

if __name__ == '__main__':
    print(create_petri_net('documentosJSON.json', '02'))


