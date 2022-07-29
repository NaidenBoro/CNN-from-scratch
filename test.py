import activations
import matplotlib.pyplot as plt
import numpy as np
a = activations.logistic() 
x=np.empty([100])
y1=np.empty([100])
y2=np.empty([100])
for i in range(100):
    y1[i] = a.calculate([1,2],[0,i/25-2])
    y2[i] = a.calculate([1,20],[0,i/25-2])
    x[i]=i/25-2

plt.plot(x, y1)
plt.plot(x, y2)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()