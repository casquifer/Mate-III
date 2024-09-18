from sympy import *

"""Ejercicio 1 - Derivar una función

x = symbols('x')
f = 3 * (x**2) + 1

dx_f = diff(f)

p1 = plot(f, xlim = [-5, 5], ylim=[-2,40], show=False)

#  Recta tangente al [3, 28]
xo = 3
x1 = 3
x2 = 3.01

yo = f.subs(x, xo)
y1 = f.subs(x, x1)
y2 = f.subs(x, x2)

m = (y2 - y1) / (x2- x1)

dx_f = m*(x-xo)+ yo 

p2 = plot(dx_f, xlim = [-5, 5], ylim=[-1,40], show=False)
p1.append(p2[0])

p1.show()

"""

"""Ejercicio 2 - Regla de la Cadena

x = symbols('x')

z = ((2 * x) + 1) ** 3

dz_dx = diff(z, x)

print("dz_dx = ", dz_dx)

"""

