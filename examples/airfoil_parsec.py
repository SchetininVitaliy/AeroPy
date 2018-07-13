from aeropy.AeroPy import find_3D_coefficients
from aeropy.generators.parsec import PARSEC
import matplotlib.pyplot as plt 
import numpy as np

def rm_old_files(pattern):
	import os, re, os.path
	mypath = "."
	for root, dirs, files in os.walk(mypath):
	    for file in filter(lambda x: re.match(pattern, x), files):
	        os.remove(os.path.join(root, file))

rm_old_files("Polar_*")
rm_old_files("Alfa_*")
rm_old_files("airfoil.dat")

'''Runs an example.'''
k = {}
# Sample coefficients
k['rle'] = .01
k['x_pre'] = .45
k['y_pre'] = -0.006
k['d2ydx2_pre'] = -.2
k['th_pre'] = 2
k['x_suc'] = .35
k['y_suc'] = .055
k['d2ydx2_suc'] = -.35
k['th_suc'] = -10

# Trailing edge x and y position
k['xte'] = 1.
k['yte'] = 0.

# Evaluate pressure (lower) surface coefficients
test_airfoil = PARSEC(k)

pts = test_airfoil.get_coords()

print pts

x = np.concatenate((pts[0],np.flip(pts[2],0)))
y = np.concatenate((pts[1],np.flip(pts[3],0)))

np.savetxt('airfoil.dat',np.c_[x,y])

def show(x,y):
	plt.xlim(0,1)
	plt.ylim(-.2,.2)
	plt.plot(x,y)
	plt.show()

#show(x,y)

res = find_3D_coefficients(airfoil='airfoil.dat',alpha=12.,NACA=False)
print("\nC_D = %f"%res['C_D'])
print("C_L = %f"%res['C_L'])

