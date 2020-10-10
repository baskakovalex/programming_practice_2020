import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
p, v = np.polyfit(x,y,deg=1,cov=True)
a= np.arange(1, 5.01, 0.01)
sp = plt.subplot(121)
plt.errorbar(x, y, xerr=max(abs(v[0, 0]), abs(v[1, 0]), abs(v[2, 0])), yerr=max(abs(v[0, 1]), abs(v[1, 1]), abs(v[2, 1])))
m=np.poly1d(p)
plt.plot(a, m(a))
plt.plot(p,v)
plt.grid()
plt.show()