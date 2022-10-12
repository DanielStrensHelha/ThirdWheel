#Test of matrixes
from math import *
import numpy as np

d = 8
c = d/2
t = c/2
h = sqrt(c*c - t*t)

matrix_A = np.matrix([
    [1,0,c], 
    [0,1,h], 
    [0,0,1]
])
print('Matrix A:\n', matrix_A)


a2 = -sqrt(3)/2
b1 = sqrt(3)/2

matrix_B = np.matrix([
    [0.5, a2, 0],
    [b1, 0.5, 0],
    [0,0,1]
])
print('\nMatrix B:\n', matrix_B)

matrix_C = np.matrix([
    [1,0,-c],
    [0,1,-h],
    [0,0, 1]
])

print ("La multiplication des deux matrixs utilisant la méthode matmul()")
resultat = np.matmul(matrix_A, matrix_B)
print (resultat)

print("ajout de la derniere matrix : ")
matrix_finale = np.matmul(resultat, matrix_C)
print(matrix_finale)

print("matrix de transformation pour le point (3, 0)")
point = np.matrix([
    [4],
    [2.598076211353316],
    [1]
])
print(point)

resultat = point
for i in range(6):
    print("resultat ", i)
    resultat = np.matmul(matrix_finale, resultat)
    print(resultat)