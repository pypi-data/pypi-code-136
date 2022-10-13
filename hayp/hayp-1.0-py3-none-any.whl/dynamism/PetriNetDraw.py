import graphviz as gr
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

class PetriNetDraw:
    def __init__(self, petri_net):
        self.__grph_net = gr.Digraph(petri_net.name, format='svg')

    def add_places(self, places, marking):
        self.__grph_net.attr('node', shape='circle')
        for place, mark in zip(places, marking):
            self.__grph_net.node(place, place + '\n' + str(int(mark)))

    def add_transitions(self, transitions):
        self.__grph_net.attr('node', shape='rectangle')
        for trans in transitions:
            self.__grph_net.node(trans)

    def add_functions(self, functions):
        value_functions = list(functions.values())
        functions_add = []
        for val in value_functions:
            if functions_add.count(val) == 0:
                peso = value_functions.count(val)
                self.__grph_net.edge(val[0], val[1], label=str(peso))
            functions_add.append(val)

    def draw_petri_net_with_initial_marking(self, petri_net):
        self.add_places((petri_net.places.keys()), petri_net.initial_marking)
        self.add_transitions(petri_net.transitions)
        self.add_functions(petri_net.inputs)
        self.add_functions(petri_net.outputs)
        self.__grph_net.render(directory='states-%s'%petri_net.name, view=True, filename='initial_state')

    def draw_petri_net_with_current_marking(self, petri_net):
        self.add_places((petri_net.places.keys()), petri_net.current_marking)
        self.add_transitions(petri_net.transitions)
        self.add_functions(petri_net.inputs)
        self.add_functions(petri_net.outputs)
        self.__grph_net.render(directory='states-%s' % petri_net.name, view=True, filename='current_state')