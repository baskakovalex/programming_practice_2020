import numpy as np
import matplotlib.pyplot as plt
a=input()
with plt.xkcd():
    plt.figure(figsize=(10,10))
    plt.plot([eval(a)for x in range(-100, 100)],lw=1)
    plt.show()
