import activations
import matplotlib.pyplot as plt
import numpy as np
from node import Node
a = activations.sigmoid()
n = Node(a)

print(n.calculate(1,0))