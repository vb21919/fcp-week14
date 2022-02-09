print("hello world")

import numpy as np
import matplotlib.pyplot as plt


h = int( input('input height: '))
w = int( input('input width: '))
x = np.linspace(0,h,100)
y = 0* x + w

x1 = 0*x +h
y1 = np.linspace(0,w,100)

x2 = 0*x 
y2 = 0*x

plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y1)
plt.plot(x,y2)

plt.title('title name')
plt.xlabel('xAxis name')
plt.ylabel('yAxis name')
plt.show()

