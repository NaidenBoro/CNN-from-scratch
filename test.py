import activations
import matplotlib.pyplot as plt
import numpy as np
from layers import layer
a = activations.sigmoid()
l = layer(activations.linear(),1)

l.print()