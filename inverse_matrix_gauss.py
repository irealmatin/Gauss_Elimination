"""
Python code related to the numerical linear algebra lesson project -> Inverse matrix using Gauss

writer : Matin Mohammadi 

Professor's name: Dr. Tabrizi Doz
""" 
import numpy as np

# n = int(input("len : "))

# a_matrix = np.zeros((n, 2*n))

# for i in range(n):
#     for j in range(n):
#         a_matrix[i][j] = float(input(f"a[{str(i+1)},{str(j+1)}] : "))

# # attached the I matrix 
# for i in range(n):
#     for j in range(n):
#         if i == j :
#             a_matrix[i][j+n] = 1

# #print(a_matrix)
# """
# [[ 1. -1.  1.  1.  0.  0.]
#  [ 2.  1.  2.  0.  1.  0.]
#  [ 3.  2. -1.  0.  0.  1.]]
# """
# # ---------------------------------------------
# # Elimination process
# for i in range(n):
#     if a_matrix[i][j] == 0.0:
#         raise Exception("Divide by zero Error , please check the values or pivoting")
#     for j in range(n):
#         if i != j :
#             factor = a_matrix[j][i] / a_matrix[i][i]
#             for f in range(2*n):
#                 a_matrix[j][f] -=  factor*a_matrix[i][f]

# for i in range(n):
#     divs = a_matrix[i][i]
#     for j in range(2*n):
#         a_matrix[i][j] /= divs

# # show matrix
# print(a_matrix)

"""
len : 3
a[1,1] : 2
a[1,2] : -2
a[1,3] : 3
a[2,1] : 1
a[2,2] : 1
a[2,3] : 1
a[3,1] : 1
a[3,2] : 3
a[3,3] : -1
[[ 1.          0.          0.          0.66666667 -1.16666667  0.83333333]
 [ 0.          1.          0.         -0.33333333  0.83333333 -0.16666667]
 [-0.         -0.          1.         -0.33333333  1.33333333 -0.66666667]]
"""

# lets write in OOP form :
class MatrixInverter:
    def __init__(self, size):
        self.size = size
        self.a_matrix = np.zeros((self.size, 2*self.size))

    def input_matrix(self):
        for i in range(self.size):
            for j in range(self.size):
                self.a_matrix[i][j] = float(input(f"a[{i+1},{j+1}]: "))

    def attach_identity(self):
        """
        to attach the main matrix with I matrix for make augmented matrix:
        [[a11 a12  a13   1   0.   0.]
        [ a21  a22  a23  0.  1.  0.]
        [ a31 a32 a33    0.  0.  1.]]
        """
        for i in range(self.size):
            self.a_matrix[i][i+self.size] = 1

    def eliminate(self):
        for i in range(self.size):
            if self.a_matrix[i][i] == 0.0:
                raise Exception("Divide by zero detected, please check the values or consider pivoting")
            for j in range(self.size):
                if i != j:
                    factor = self.a_matrix[j][i] / self.a_matrix[i][i]
                    for f in range(2*self.size):
                        self.a_matrix[j][f] -= factor * self.a_matrix[i][f]

    def normalize(self):
        """
        responsible for transforming the rows of the augmented matrix (which contains both the original matrix and the identity matrix) 
        into a form where the leading coefficient of each row (the diagonal elements of the original matrix part) is 1.
        This is achieved by dividing each element in a row by the value of the leading coefficient (the diagonal element) of that row.
        """
        for i in range(self.size):
            divisor = self.a_matrix[i][i]
            for j in range(2*self.size):
                self.a_matrix[i][j] /= divisor

    def invert(self):
        self.input_matrix()
        self.attach_identity()
        self.eliminate()
        self.normalize()
        return self.a_matrix[:, self.size:]

# usage:
n = int(input("Enter the size of the matrix: "))
inverter = MatrixInverter(n)
inverse_matrix = inverter.invert()
print("The inverse matrix is:")
print(inverse_matrix)