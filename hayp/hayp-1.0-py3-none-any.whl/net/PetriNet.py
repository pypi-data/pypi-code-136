class PetriNet:

    def __init__(self, name, places, transitions, inputs, outputs, initial_marking):
        self.__name = name
        self.__places = places
        self.__transitions = transitions
        self.__inputs = inputs
        self.__outputs = outputs
        self.__initial_marking = initial_marking
        self.__current_marking = initial_marking

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, places):
        self.__places = places

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, transitions):
        self.__transitions = transitions

    @property
    def inputs(self):
        return self.__inputs

    @inputs.setter
    def inputs(self, inputs):
        self.__inputs = inputs

    @property
    def outputs(self):
        return self.__outputs

    @outputs.setter
    def outputs(self, outputs):
        self.__outputs = outputs

    @property
    def initial_marking(self):
        return self.__initial_marking

    @initial_marking.setter
    def initial_marking(self, initial_marking):
        self.__initial_marking = initial_marking

    @property
    def current_marking(self):
        return self.__current_marking

    @current_marking.setter
    def current_marking(self, current_marking):
        self.__current_marking = current_marking

    def __str__(self):
        return f'''
            Red Name: {self.__name}
                Places: {self.__places}
                Transitions: {self.__transitions}
                Inputs: {self.__inputs}
                Outputs: {self.__outputs}
                Initial Marking: {self.__initial_marking}
                Current Marking: {self.__current_marking}
        '''