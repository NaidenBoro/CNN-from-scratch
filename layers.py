from node import Node
from activations import bias
import numpy as np
class layer():
    nodes = []
    a_type = bias
    def __init__(self, a_type , nodes_count):
        self.a_type  = a_type 
        self.nodes_count = nodes_count
        self.nodes = []
        self.nodes.append(Node(bias))
        for i in range(self.nodes_count):
            self.nodes.append(Node(a_type))
        self.nodes_count+=1
    

    def print(self):
        for i in range(len(self.nodes)):
            print(self.nodes[i].type)

    def calculate (self,inputs,weights):
        outputs = []
        outputs.append(1)
        for i in range(self.nodes_count-1):
            outputs.append(self.nodes[i+1].calculate(inputs,weights[i]))
        return outputs

