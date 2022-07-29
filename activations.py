import abc
from abc import ABC, abstractmethod
import numpy as np

class activation_function(ABC):

    def calculate(self):
        pass

class linear(activation_function):

    def calculate(self,a,x):
        
        return np.dot(np.matrix.transpose(np.array(a)),np.array(x))

class logistic(activation_function):

    def calculate(self,a,x):
        
        z = np.dot(np.matrix.transpose(np.array(a)),np.array(x))
        return 1/(1+pow(np.e,-z))

class ReLU(activation_function):

    def calculate(self,a,x):
        
        return max(0,np.dot(np.matrix.transpose(np.array(a)),np.array(x)))