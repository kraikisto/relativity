# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:02:20 2021

@author: kalle
"""
import sympy 


def getMatrix():
    """ 
    Asks the user to input necessary values to create a matrix.
    
    returns: matrix as the sympy object
    """
    matrix = []
    try:
        rows = int(input("How many rows? "))
        columns = int(input("How many columns? "))
        for i in range(0, columns): #loops ask values and add them to the matrix
            column = []
            for i in range(0, rows):
                inp = input("Give number in matrix (use a, b, c and d as variables): ")
                func = sympy.sympify(inp)
                column.append(func)
            matrix.append(column)
    except ValueError:
        print("Invalid input")
    
    return sympy.Matrix(matrix) #creates an object that we can use different functions on

def printChristoffel(metric, size):
    """
    Calculates all the Christoffel symbols for a metric. Uses the basic formula for them.
    
    Arguments:
    metric: the metric that we are calculating Christoffel symbols for
    size: size of the matrix (if 2x2 input 2 and so on)
    """
    invMetric = metric.inv()
    print("Iverse matrix:")
    print(invMetric)
    if size == 4: 
        listOfNumbers = [[0,0,0],[0,0,1],[0,1,1],[0,1,2],[0,2,2],[0,2,3],[0,3,3],[0,1,3],[0,0,3],[0,0,2],[1,0,0],[1,0,1],[1,1,1],[1,1,2],[1,2,2],[1,2,3],[1,3,3],[1,1,3],[1,0,3],[1,0,2],[2,0,0],[2,0,1],[2,1,1],[2,1,2],[2,2,2],[2,2,3],[2,3,3],[2,1,3],[2,0,3],[2,0,2],[3,0,0],[3,0,1],[3,1,1],[3,1,2],[3,2,2],[3,2,3],[3,3,3],[3,1,3],[3,0,3],[3,0,2]] 
    if size == 3: 
        listOfNumbers = [[0,0,0],[0,0,1],[0,1,1],[0,1,2],[0,2,2],[0,0,2],[1,0,0],[1,0,1],[1,1,1],[1,1,2],[1,2,2],[1,0,2],[2,0,0],[2,0,1],[2,1,1],[2,1,2],[2,2,2],[2,0,2]] 
    #if size == 2: remember to fix (not that 2x2 is really needed anyway)
        #listOfNumbers = [[0,0,0],[0,0,1],[0,1,1][1,0,0],[1,0,1],[1,1,1]] 
        
    print("Christoffel symbols:")    
    for numbers in listOfNumbers:
        terms = []
        for i in range(0, size):
            terms.append(0.5 * invMetric[numbers[0],i]*(metric[i,numbers[2]].diff(indexing(numbers[1])) + metric[i,numbers[1]].diff(indexing(numbers[2])) + metric[numbers[1],numbers[2]].diff(indexing(i))))
            christoffel = sum(terms)
            print(numbers)
            print(christoffel)
        






#main program
prog = 1
while prog != 0:
    prog = int(input("""
For Taylor series press 1
For numeric derivative press 2
For numeric derivative function press 3
For Christoffel symbols press 4
To stop press 0
What do you want to do?
"""))
    if prog == 1:
        getTaylor()
    elif prog == 2:
        getNumDerivative()
    elif prog == 3:
        getNumDerivativeFunc()
    elif prog == 4:
        
        metric = getMatrix()
        print(metric)
        size = len(metric.row(0))
        printChristoffel(metric, size)
    elif prog == 0:
        break 
    else:
        print("Please press one of the options above!")