import numpy as np
"""
Python code related to the numerical linear algebra lesson project -> a system of linear equations with Gauss elimination method

writer : Matin Mohammadi 

Professor's name: Dr. Tabrizi Doz
""" 

# ----------- solve Ax = b with pivoting -----------------

#Define Coefficients Matrix
a_matrix = np.array([[2, -4, 1],[1,1 ,4] , [3, 1, -3]] , float)

#Define Answer Vector
b_vector = np.array([0 , 5 , -1] , float)

#Define the size of linear system
system_size = len(b_vector)

#Define Solution vector 
solution_vector = np.zeros(system_size,float) # [0. 0. 0.]

# nested loop for elimination process
for f in range(system_size -1) : #to index fix row and eliminate columns
    if np.fabs((a_matrix[f,f])) < 1.0e-12: #pivoting 
        for k in range(f+1 , system_size):
            if np.fabs(a_matrix[k,f]) > np.fabs(a_matrix[f,f]):
                a_matrix[[f,k]] = a_matrix[[k,f]]
                b_vector[[f,k]] = b_vector[[k,f]]
                break

    for i in range(f+1,system_size) : #to index subtract rows
        if a_matrix[i,f] == 0 :
            continue
        ratio = a_matrix[f,f] / a_matrix[i,f]
        for j in range(f,system_size):# to index columns for sustraction
            a_matrix[i,j] = a_matrix[f,j] - a_matrix[i,j]*ratio
        b_vector[i] = b_vector[f] - b_vector[i]*ratio
print("**********************************************************")
print("Upper triangular matrix after elimination : " )
print(a_matrix)
print("**********************************************************")
print("Answer vector after elimination :")
print(b_vector)

# Now , we have a loop for solving backward linear system from above result
solution_vector[system_size-1] = b_vector[system_size -1] / a_matrix[system_size-1,system_size-1] # start from last row(? : backwards)

for i in range(system_size-2 , -1,-1) :
    sum_of_ax = 0
    for j in range(i+1 , system_size):# to sum
        sum_of_ax += a_matrix[i,j] * solution_vector[j]
    solution_vector[i] += (b_vector[i] - sum_of_ax) / a_matrix[i,i]
print("**********************************************************")
print("*****************************")
print("*************")
print("Here your answers :")
print(solution_vector)
