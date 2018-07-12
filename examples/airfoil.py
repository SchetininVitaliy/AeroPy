from aeropy.AeroPy import find_3D_coefficients

res = find_3D_coefficients(airfoil='dae11.dat',alpha=12.,NACA=False)
print res

