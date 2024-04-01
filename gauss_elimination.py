"""
Python code related to the numerical linear algebra lesson project -> a system of linear equations with Gauss elimination method

writer : Matin Mohammadi 

Professor's name: Dr. Tabrizi Doz
"""

import numpy as np

# ----------- solve Ax = b without pivoting -----------------

# #Define Coefficients Matrix
# a_matrix = np.array([[1.012 , -2.132 , 3.104],[-2.132,4.096 , -7.013] , [3.104, -7.013, 0.014]] , float)

# #Define Answer Vector
# b_vector = np.array([1.984 , -5.049 , -3.895] , float)

# #Define the size of linear system
# system_size = len(b_vector)

# #Define Solution vector 
# solution_vector = np.zeros(system_size,float) # [0. 0. 0.]

# # nested loop for elimination process
# for f in range(system_size -1) : #to index fix row and eliminate columns
#     for i in range(f+1,system_size) : #to index subtract rows
#         if a_matrix[i,f] == 0 :
#             continue
#         ratio = a_matrix[f,f] / a_matrix[i,f]
#         for j in range(f,system_size):# to index columns for sustraction
#             a_matrix[i,j] = a_matrix[f,j] - a_matrix[i,j]*ratio
#         b_vector[i] = b_vector[f] - b_vector[i]*ratio
# print("**********************************************************")
# print("Upper triangular matrix after elimination : " )
# print(a_matrix)
# print("**********************************************************")
# print("Answer vector after elimination :")
# print(b_vector)

# # Now , we have a loop for solving backward linear system from above result
# solution_vector[system_size-1] = b_vector[system_size -1] / a_matrix[system_size-1,system_size-1] # start from last row(? : backwards)

# for i in range(system_size-2 , -1,-1) :
#     sum_of_ax = 0
#     for j in range(i+1 , system_size):# to sum
#         sum_of_ax += a_matrix[i,j] * solution_vector[j]
#     solution_vector[i] += (b_vector[i] - sum_of_ax) / a_matrix[i,i]
# print("**********************************************************")
# print("*****************************")
# print("*************")
# print("Here your answers :")
# print(solution_vector)


# lets write it in OOP form 

class LinearSystemSolver:
    def __init__(self, a_matrix, b_vector):
        self.a_matrix = np.array(a_matrix, float)
        self.b_vector = np.array(b_vector, float)
        self.system_size = len(b_vector)
        self.solution_vector = np.zeros(self.system_size, float)

    def solve(self):
        # Perform elimination to form upper triangular matrix
        for f in range(self.system_size - 1):
            for i in range(f + 1, self.system_size):
                if self.a_matrix[i, f] == 0:
                    continue
                ratio = self.a_matrix[f, f] / self.a_matrix[i, f]
                for j in range(f, self.system_size):
                    self.a_matrix[i, j] = self.a_matrix[f, j] - self.a_matrix[i, j] * ratio
                self.b_vector[i] = self.b_vector[f] - self.b_vector[i] * ratio

        # Back substitution to solve for solution vector
        self.solution_vector[self.system_size - 1] = self.b_vector[self.system_size - 1] / self.a_matrix[self.system_size - 1, self.system_size - 1]
        for i in range(self.system_size - 2, -1, -1):
            sum_of_ax = sum(self.a_matrix[i, j] * self.solution_vector[j] for j in range(i + 1, self.system_size))
            self.solution_vector[i] = (self.b_vector[i] - sum_of_ax) / self.a_matrix[i, i]

        return self.solution_vector

# usage:
a_matrix = [[1.012, -2.132, 3.104], [-2.132, 4.096, -7.013], [3.104, -7.013, 0.014]]
b_vector = [1.984, -5.049, -3.895]
solver = LinearSystemSolver(a_matrix, b_vector)
solution = solver.solve()
print("Here are your answers:")
print(solution)