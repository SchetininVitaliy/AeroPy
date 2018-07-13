import matplotlib.pyplot as plt
import numpy as np

res = np.loadtxt('dakota_tabular.dat',skiprows=1,usecols=(2,3,4))

plt.plot(res[:,0],res[:,2])
plt.show()
