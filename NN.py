import activations
import numpy as np
from layers import layer
from output import output
from node import Node
class NeuralNetwork():
    inputs_c = 0
    layers = []
    output_l = output(activations.sigmoid,0)
    weights = []
    def __init__(self, inputs_c, layers,output_l):
        self.inputs_c = inputs_c
        self.layers = layers
        self.output_l = output_l

        self.weights.append(np.random.randn(len(layers[0].nodes)-1,inputs_c)/10)
        for i in range(len(layers)-1):
            self.weights.append(np.random.randn(len(layers[i+1].nodes)-1,len(layers[i].nodes))/10)
        self.weights.append(np.random.randn(len(output_l.nodes),len(layers[len(layers)-1].nodes))/10)

    def calculate(self,inputs):
        last_output = inputs
        for i in range(len(self.layers)):
            last_output = self.layers[i].calculate(last_output,self.weights[i])
        return self.output_l.calculate(last_output,self.weights[-1])