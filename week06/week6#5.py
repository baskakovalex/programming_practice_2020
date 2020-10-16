import numpy as np
import matplotlib.pyplot as plt
def fun(x):
  if x<-5:
    return x^2
  if x>=-5 and x<=5:
    return 2*abs(x)-1
  if x>=5:
    return 2*x
for x in range (-10,10,):
  plt.plot(x,fun(x))
plt.show