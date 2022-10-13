
import numpy as np
from scipy import interpolate

def make_extended_vector(vector : np.array):
    '''
    This function takes a given function and outputs a extended version of the vector
    The extended values are the linear interpolated values
    '''
    length_of_timestep = len(vector)
    xs = [2*x+1 for x in range(0,length_of_timestep)]
    new_xs = [x for x in range(0,2*length_of_timestep)]
    
    f = interpolate.interp1d(xs, vector, fill_value='extrapolate')
    
    return f(new_xs)


def make_coordinate_list(x_vector : list, y_vector : list, step: int):
    coordinate_list = [(x,y) for x, y in zip(x_vector, y_vector)][::step]
    return coordinate_list


def calculate_gradient(two_points:tuple, dx=1):
    '''
    This function calculates the gradient of a two point.
    The precondition is that the dx of a given two points is 1. But this can be changed.
    two_points : (x_0, x_1) 
    '''
    if dx <= 0 : 
        raise ValueError('dx should be larger than 0')
    
    x0, x1 = two_points
    grad = (x1 - x0)/dx
    return grad


def give_calculated_gradient_list(extended_vector:list, step=2):
    '''
    This function takes the extended vector as its input and calculates the gradient.
    It outputs the gradient for every point.
    step : step size to calculate the gradient. default : 2
    '''
    number_of_chunks = int(len(extended_vector) / 2)
    chunks = [(extended_vector[num*2],extended_vector[num*2+1]) for num in range(0,number_of_chunks)]
    return list(map(calculate_gradient,chunks))


def calculate_linear_function_form(coordinate: tuple, gradient: float):
    '''
    This function calculates the linear function parameters.
    coordinate : (x,y)
    y = ax + b
    '''
    x, y = coordinate
    b = y - (x*gradient)
    return gradient, b
