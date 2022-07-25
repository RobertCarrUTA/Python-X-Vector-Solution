"""
How the program was ran:
    Ran on CSE VM 3.1.2
    
    Used sympy, nummpy, and scipy:
        To install:
            pip3 install sympy
            pip3 install nummpy
            pip3 install scipy
    
    Compile/run: python3 solveXMatrix.py

Goal of Program:
    (a) Compute the vector x given B and [x]B below and print the
        result. 


Basis B =
 0  -4   6
-1   0   6
-1   0   3

Vector [x]B =
-2
 6
 1

"""
import sympy
import numpy as np
import scipy.linalg as linalg

# -------------------------------------------------------------------
# Our given matrix and vector:
print('Our given basis B and our [x]B vector:')
    
basis_B_Matrix = np.array([[0, -4, 6], [-1, 0, 6], [-1, 0, 3]])
x_Vector_B = np.array([[-2], [6], [1]])

"""
    solve_x_Vector is our function. We pass in both np.array's as arguments, then inside we
    print those back out to the terminal. Then we take those two arguments and solve for the
    x vector. This is like number 2 on the handwritten portion, so we take the same approach. We just
    multiply basis_B_Matrix and x_Vector_B to get the x vector. We use np.matmul to do this easily.
"""
def solve_x_Vector(basis_B_Matrix, x_Vector_B):
    
    print('\nBasis B in Matrix Form:\n', basis_B_Matrix)
    print('\n[x]B vector:\n', x_Vector_B)
    print('-------------------------------')

    print('x vector is:\n', np.matmul(basis_B_Matrix, x_Vector_B))
    
solve_x_Vector(basis_B_Matrix, x_Vector_B)
