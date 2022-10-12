from math import sqrt
import numpy

d = 8
c = d/2
t = c/2
h = sqrt(c*c - t*t)

def findZ1(i):
    return c- ((8-i)/8)*t

def findZ2(i):
    return i/4*h - i/8*h

def findBx(i,j):
    z1 = findZ1(i)
    return (j/4*z1) + ((8-i)/8*t)

def findBy(i,j):
    z2 = findZ2(i)
    return (j/4*z2) + (i/8*h)

def main():
    dim1 = 5
    dim2 = 5
    dim3 = 2

    tab = [[[0 for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

    for i in range(dim1):
        for j in range(dim2):
            tab[i][j][0] = findBx(i, j)
            tab[i][j][1] = findBy(i, j)
    
    print("c = " + str(c) + ", h = " + str(h))
    for i in range(dim1):
        for j in range(dim2):
            print(tab[i][j])
    
    

if __name__ == '__main__':
    main()
    exit()