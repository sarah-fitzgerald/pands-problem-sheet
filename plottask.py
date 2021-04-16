#Progam that displays a plot of functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
#Author: Sarah Fitzgerald

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 4.0) #This is the x-axis values, the range is from 0.0 to 4.0: https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm

x = x #This is f(x)
y = x ** 2 #This is g(x)
z = x ** 3 #This is h(x)

#This sections is plots the points on the graph: https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html
plt.plot (x, linestyle = 'dashed', label = 'f(x)', color ='r') #X is a dashed line, with the label 'f(x)', and in the colour red
plt.plot (y, linestyle = 'dashed', label = 'g(x)', color = 'b') #Y is a dashed line, with the label 'g(x)', and in the colour blue
plt.plot (z, linestyle = 'dashed', label = 'h(x)', color = 'g') # Z is a dashed line, with the label 'h(x)', and in the colour green

plt.xlim(0.0, 3.5) #Sets the limit for the x-axis: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
plt.ylim(0.0, 30.0) #Sets the limit for the y-axis

plt.xlabel ('X-Axis') #Labels the x-axis
plt.ylabel ('Y-Axis') #Labels the y-axis

plt.title('f(x)=x, g(x)=x2 and h(x)=x3') #Title of the graph

plt.legend() #Shows the labels in plots 
plt.show() #Despicts a graphic representation of this plot
