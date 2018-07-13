from aeropy.AeroPy import find_3D_coefficients
from aeropy.generators.nurbs import NURBS
import matplotlib.pyplot as plt 
import numpy as np
'''Runs an example'''
k ={}
#sample coefficients: Coefficients for generating NACA5410
k['ta_u'] = 0.1584
k['ta_l'] = 0.1565
k['tb_u'] = 2.1241
k['tb_l'] = 1.8255
k['alpha_b'] = 11.6983
k['alpha_c'] = 3.8270

generator = NURBS(k)
pts = generator._spline()

x = np.concatenate((pts[3],np.flip(pts[1],0)))
y = np.concatenate((pts[2],np.flip(pts[0],0)))

np.savetxt('airfoil.dat',np.c_[x,y])

def show(x,y):
	plt.xlim(0,1)
	plt.ylim(-.2,.2)
	plt.plot(x,y)
	plt.show()

show(x,y)

res = find_3D_coefficients(airfoil='airfoil.dat',alpha=12.,NACA=False)
print res


