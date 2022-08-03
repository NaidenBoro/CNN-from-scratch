import abc
from abc import ABC, abstractmethod
import numpy as np

class activation_function(ABC):

    def calculate(self):
        pass
    
    def derivative(self,z):
        pass
class linear(activation_function):

    def calculate(self,z):
        
        return z
    
    def derivative(self,z):

        return 1

class sigmoid(activation_function):

    def calculate(self,z):
        
        return 1/(1 + pow(np.e,-z))

    def derivative(self,z):

        return z*(1 - z)

class ReLU(activation_function):

    def calculate(self,z):
        
        return max(0,z)
    
    def derivative(self,z):

        return z > 0

class bias(activation_function):

    def calculate(self,z):
        
        return 1
    
    def derivative(self,z):

        return 0