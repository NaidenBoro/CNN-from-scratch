import abc
from abc import ABC, abstractmethod

class activation_function(ABC):

    def calculate(self):
        pass

class linear(activation_function):
    
    def calculate(a,b,x):
        return a*x+b