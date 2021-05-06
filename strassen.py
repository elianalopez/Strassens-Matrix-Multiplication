import numpy as np


print("\n\nPlease input the values of your matrix A\n\n")
print("Here is how your matrix will be formatted:\n")
print('[[a11,a12]\n[a21,a22]]\n')
a11 = int(input("a11: "))
a12 = int(input("a12: "))
a21 = int(input("a21: "))
a22 = int(input("a22: "))


a = np.matrix([[a11, a12], [a21, a22]])


print("\n\nPlease input the values of your matrix B\n\n")
print("Here is how your matrix will be formatted:\n")
print('[[b11,b12]\n[b21,b22]]\n')
b11 = int(input("b11: "))
b12 = int(input("b12: "))
b21 = int(input("b21: "))
b22 = int(input("b22: "))


b = np.matrix([[b11, b12], [b21, b22]])


def strassen(a,b):

    
    a11 = a[0,0]
    a12 = a[0,1]
    a21 = a[1,0]
    a22 = a[1,1]

    
    b11 = b[0,0]
    b12 = b[0,1]
    b21 = b[1,0]
    b22 = b[1,1]


    s1 = b12 - b22
    s2 = a11 + a12
    s3 = a21 + a22
    s4 = b21 - b11
    s5 = a11 + a22
    s6 = b11 + b22
    s7 = a12 - a22
    s8 = b21 + b22
    s9 = a11 - a21
    s10 = b11 + b12


    p1 = s1 * a11
    p2 = s2 * b22
    p3 = s3 * b11
    p4 = s4 * a22
    p5 = s5 * s6
    p6 = s7 * s8
    p7 = s9 * s10

    
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p5 + p1 - p3 - p7

    
    print("\nmatrix a:\n")
    print(a)
    print("\nmatrix b:\n")
    print(b)
    print("\nThis is the product of the matrix:\n")
    key = np.matrix([[c11, c12], [c21, c22]])
    print(key)

    
strassen(a,b)
