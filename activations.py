import abc
from abc import ABC, abstractmethod
from traceback import print_tb
import numpy as np

class activation_function(ABC):

    def calculate():
        pass
    
    def derivative(z):
        pass
class linear(activation_function):

    def calculate(z):
        return z
    
    def derivative(z):

        return 1

class sigmoid(activation_function):

    def calculate(z):
        
        return 1/(1 + pow(np.e,-z))

    def derivative(z):

        return z*(1 - z)

class ReLU(activation_function):

    def calculate(z):
        
        return max(0,z)
    
    def derivative(z):

        return z > 0

class bias(activation_function):

    def calculate(z):
        
        return 1
    
    def derivative(z):

        return 0