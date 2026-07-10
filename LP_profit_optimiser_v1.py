from scipy.optimize import linprog
import numpy as np


def collection_func():
    '''
    Function which collects user inputs for:
    - number of products
    - Manufacturing cost
    - Sale price
    - Raw material requirement for each product
    - Raw material units available
    - Time to create each product
    - Time available
    '''
    print('')
    print('-------------------------------------------')
    print('               USER INPUT:                 ')
    print('-------------------------------------------')
    print('')
    while True:
        try:
            number = int(input("Give the number of products: ")) # asks for the number of products
            if number > 0:
                break
            else:
                print('Invalid input, require > 0')
        except ValueError:
            print('Invalid input, require NUMERICAL')
    print('')
    cost = []
    for i in range(number): #collects the manufacturing cost of each product
        while True:
            try:
                unit_cost = float(input(f"How much does product {i} cost to produce in £? "))
                cost.append(unit_cost)
                break
            except ValueError:
                print('Invalid input, require NUMERICAL')
    print('')
    sale = []
    for i in range(number): #collects the sale price of each product
        while True:
            try:
                unit_sale = float(input(f"How much does product {i} sell for in £? "))
                sale.append(unit_sale)
                break
            except ValueError:
                print('Invalid input, require NUMERICAL')
    print('')        
    mat_cost = []
    for i in range(number): #collects the raw material cost of each product
        while True:
            try:
                unit_matcost = float(input(f"What is the material cost of product {i}? "))
                if unit_matcost >= 0:
                    mat_cost.append(unit_matcost)
                    break 
                else:
                    print("Invalid input, require > 0")       
            except ValueError:
                print('Invalid input, require NUMERICAL')
    print('')       
    while True:
        try:
            maxmat = float(input("What is the maximum number of material units available? ")) # collects the maximum number of material units
            if maxmat >= 0:
                break
            else:
                print('Invalid input, require > 0')
        except ValueError:
            print('Invalid input, require NUMERICAL')
    print('')
    time_cost = []
    for i in range(number): #collects the raw material cost of each product
        while True:
            try:
                unit_timecost = float(input(f"How long does it take to produce product {i}? "))
                if unit_timecost >= 0:
                    time_cost.append(unit_timecost)
                    break
                else:
                    print('Invalid input, require > 0')
            except ValueError:
                print('Invalid input, require NUMERICAL')
    print('')
    while True:
        try:
            maxtime = float(input("What is the maximum time available for production? ")) # collects the maximum time available
            if maxtime >= 0:
                break
            else:
                print('Invalid input, require > 0')
        except ValueError:
            print('Invalid input, require NUMERICAL')
    print('')
    
    # queries additional constraints (inequalities only for now)

    



    # converts lists to numpy arrays for easier manipulation
    cost_array = np.array(cost)
    sale_array = np.array(sale)
    profit_array = sale_array - cost_array
    profit = profit_array.tolist()


    input_data_lhs = np.array([profit, mat_cost, time_cost]) # empty array in which function data will later be stored
    input_data_rhs = np.array([maxmat, maxtime])


    return input_data_lhs, input_data_rhs, number

def result_function(results, number):
    '''
    Function governing the result output
    '''

    max_profit = -1 * results.fun
    optimal_values = results.x
    print('')
    print('-------------------------------------------')
    print('               RESULTS:                    ')
    print('-------------------------------------------')
    print('')
    print(results.message)
    print(f'The maximum PROFIT attainable is £{max_profit},')
    for i in range(number):
        print(f'The NUMBER of product {i} required is {optimal_values[i]} units.')

    return None

def main():
    '''
    Main function for executing code
    '''

    input_data = collection_func()
    #input_data = [[-10, -20, -25], [ 3,   2,   4,], [  1,   1,   1]], [200,  80], [3] # test coefficients
    number = input_data[2]
    obj = -1 * input_data[0][0] # function to maximise (need to x -1 as linprog can only minimise)
    lhs = input_data[0][1:] # constraint coefficients
    rhs = input_data[1] # constraint inequalities

    optimisation = linprog(c = obj, A_ub = lhs, b_ub = rhs, method = 'highs')

    result_function(optimisation, number)

    return None

main()