import numpy as np

class Node():
    def __init__(self, type):
        self.type = type

    def calculate(self, a,x):
        z = np.dot(np.array(a),np.array(x))
        print("z=",z)
        return self.type.calculate(z)