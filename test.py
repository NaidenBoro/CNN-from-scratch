import activations
import matplotlib.pyplot as plt
import numpy as np
from layers import layer
from output import output
from NN import NeuralNetwork
nn = NeuralNetwork(3,[layer(activations.ReLU,4),layer(activations.linear,6)],output(activations.sigmoid,4))
print(nn.calculate([3,3,3]))