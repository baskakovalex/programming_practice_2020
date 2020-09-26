import numpy as np
import math
import matplotlib.pyplot as plt
x=1
y=np.log((x**2+1)*np.exp(-1*np.abs(x)/10))/np.log(1+np.tan(1/(1+np.sin(x)*np.sin(x))))
print (y)
x = np.arange(-100,+100)
plt.plot(x,(np.log((x**2+1)*np.exp(-1*np.abs(x)/10))/np.log(1+np.tan(1/(1+np.sin(x)*np.sin(x))))))
plt.show()