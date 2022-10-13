

from syndp.functions import *
from syndp.bounded_laplace_mechanism import *
from syndp.laplace_mechanism import *

class TimeDP:
    
    def __init__(self, epsilon, delta, mechanism_type : str, sensitivity=0.1, seed=0):
        '''
        This class is a noise giving class. It takes the gradient and calculates new synthezied series data
        you can choose two types of mechanism. Original laplace mechanism or Bounded Laplace Mechanism
        mechanism_type : 1) laplace, 2) bouned_laplace
        '''
        self.epsilon = epsilon
        self.delta = delta 
        self.mechanism_type = mechanism_type
        self.sensitivity = sensitivity
        self.mechanism = self._dp_mechanism()
        self.seed = seed
    
    def _dp_mechanism(self):
        if self.mechanism_type == 'laplace':
            return laplace_mechanism
        else :
            return boundedlaplacemechanism
    
    def calculate_dp_value(self, val, D = None, seed=0):
        '''
        requires value(val) and sensitivity(sens)
        '''
        if self.mechanism_type == 'laplace':
            return self.mechanism(value=val, sensitivity=self.sensitivity, epsilon=self.epsilon, seed=seed)
        else :
            self.sensitivity = 9999 # change to 9999
            return self.mechanism(value=val, D = D, b=self.sensitivity, epsilon=self.epsilon, delta = self.delta, seed=self.seed)


class Vector_creator:
    
    def __init__(self, vector: np.array, timedp: object):
        self.vector = vector
        self.vector_length = len(vector)
        self.timedp = timedp
        self.mechanism_type =timedp.mechanism_type
        self.extended_vector = self.make_extended_vector()
        self.coordinates = self.make_coordinates()
        self.gradient_list = self.prepare_for_gradient()
        self.new_gradients = self.make_new_gradient()
        self.new_function_forms = self.calculate_function_form()
        self.new_vector = self.make_new_vector()
        
    def make_extended_vector(self):
        '''
        makes extended vector
        '''
        return make_extended_vector(vector=self.vector)
    
    def make_coordinates(self):
        '''
        makes x and y coordinate list 
        '''
        extend_vector_length = self.vector_length * 2
        xs = [x for x in range(0, extend_vector_length)]
        return make_coordinate_list(xs, self.extended_vector, 2)
    
    
    def prepare_for_gradient(self):
        return give_calculated_gradient_list(self.extended_vector, step=2)
    
    def create_boundary(self, gradient):
        if gradient < 0 :
            return -9999, 0
        elif gradient > 0 :
            return 0, 9999
        else :
            return -1, 1
            
    def create_boundary_list(self):
        
        # print('creating boundary list')
        
        return list(map(self.create_boundary, self.gradient_list))
    
    def make_new_gradient(self):
        
        # print('created boundary list and making new gradients..')
        
        if self.mechanism_type == 'laplace':
            
            seeds = [i+self.timedp.seed for i in range(0, len(self.gradient_list))]
            return list(map(lambda x, y: self.timedp.calculate_dp_value(val = x, seed=y), self.gradient_list, seeds))
        else :
            boundary_list = self.create_boundary_list()
            return list(map(lambda x, y : self.timedp.calculate_dp_value(val=x, D=y, seed=self.timedp.seed), self.gradient_list, boundary_list))
    
    def calculate_function_form(self):
        '''
        list of (gradient and b)
        '''
        return list(map(lambda x, y : calculate_linear_function_form(x,y), self.coordinates, self.new_gradients))
    
    def make_new_value_based_on_new_gradient(self, gradient, b, x):
        y = x*gradient + b
        return y
    
    def make_new_vector(self):
        extend_vector_length = self.vector_length * 2
        xs = [x for x in range(0, extend_vector_length)][1::2]
        return [self.make_new_value_based_on_new_gradient(g,b,x) for (g, b), x, in zip(self.new_function_forms, xs)]
        
        
        
