from node import Node
from activations import bias
import numpy as np
class output():
    nodes = []
    def __init__(self, a_type , nodes_count):
        self.a_type  = a_type 
        self.nodes_count = nodes_count
        self.nodes = []
        for i in range(self.nodes_count):
            self.nodes.append(Node(a_type))
    

    def print(self):
        for i in range(len(self.nodes)):
            print(self.nodes[i].type)
    
    def calculate (self,inputs,weights):
        outputs = []
        for i in range(self.nodes_count):
            outputs.append(self.nodes[i].calculate(inputs,weights[i]))
        return outputs