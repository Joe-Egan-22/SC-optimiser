from scipy.optimize import linprog
import numpy as np

FILE_NAME = 'test_file.csv'
OBJ_FUNC = [-10,-20,-25] # example coefficients of the objective function




def main():

    array_main = np.genfromtxt(FILE_NAME, dtype=float, comments= '#', delimiter=',',skip_header=True)
    obj = OBJ_FUNC
    lhs = array_main[:,:-1]
    rhs = array_main[:,-1]

    #bnd = [(0, float('inf')), (0, float('inf'))] # assume boundary conditions of zero to infinity (default bounds)

    optimisation = linprog(c = obj, A_ub = lhs, b_ub = rhs, method = 'simplex')


    return print(optimisation)

main()