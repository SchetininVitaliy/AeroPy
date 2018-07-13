#!/usr/bin/env python

from aeropy.AeroPy import find_3D_coefficients
from aeropy.generators.nurbs import NURBS
import numpy as np
import dakota.interfacing as di

print(1)
def rm_old_files(pattern):
	import os, re, os.path
	mypath = "."
	for root, dirs, files in os.walk(mypath):
	    for file in filter(lambda x: re.match(pattern, x), files):
	        os.remove(os.path.join(root, file))

rm_old_files("Polar_*")
rm_old_files("Alfa_*")
rm_old_files("airfoil.dat")

params, results = di.read_parameters_file()

'''Runs an example'''
k ={}
k['ta_u'] = params['ta_u']
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

res = find_3D_coefficients(airfoil='airfoil.dat',alpha=12.,NACA=False)
print(res)

results['Cd'].function = res['C_D']
results['Cl'].function = res['C_L']

results.write()