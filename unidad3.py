from numpy import array
from numpy.linalg import inv

#autovalores (eigenvalues) y autovectores (eigenvectors) en Python

"""
# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72

A = array([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

B = array([
    44,
    56,
    72
])

# Inversa de A por A debería darnos la matrix identidad:
print(inv(A) @ A)
"""