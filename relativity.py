import sympy 
import math

x = sympy.var('x')  #define the variable we are using so that we can recognise functions
a = sympy.Symbol('a')
b = sympy.Symbol('b')
c = sympy.Symbol('c')
d = sympy.Symbol('d')

def indexing(num): 
    if num == 0:
        return a
    elif num == 1:
        return b
    elif num == 2:
        return c
    elif num == 3:
        return d

def taylor(func, a, n):
    """
    This function calculates the taylors series for a function. 
    
    Arguments:
    Func: the function you are using
    a: the spot you want to calculate the derivative in
    n: the number of terms of the taylors series you want to calculate
        
    
    returns: taylors series
    """
    symp = sympy.sympify(func) #makes the function from a string into something we can use
    terms = [] #creating a list that has all the terms for us separately
    terms.append(symp)
    for i in range(1,n+1): #here is just simple math, using the basic formula for taylor's series
        func = func.diff(x) 
        f_a = symp.subs(x, a) #value of the function in the spot a
        fact = math.factorial(i)
        taylor = f_a / fact * (x - a)
        terms.append(taylor)
        
    taylorSeries = 0
    for term in terms: #we have all the terms separately, now we add them together
        taylorSeries = taylorSeries + term
    print(taylorSeries)
        
def getTaylor():
    """
    This function calculates the taylor series, but instead of having the needed values as arguments, 
    asks for them making it simpler to use and simpler coding.
    """
    try:
        func = input("give the function you want to use this for: ")
        a = float(input("give the x value: "))
        n = int(input("give the amount of terms you want: "))
        taylor(func, a, n)
    except ValueError:
        print("The x value and/or amount of terms need a number value!")

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
For Christoffel symbols press 2
To stop press 0
What do you want to do?
"""))
    if prog == 1:
        getTaylor()
    elif prog == 2:
        
        metric = getMatrix()
        print(metric)
        size = len(metric.row(0))
        printChristoffel(metric, size)
    elif prog == 0:
        break 
    else:
        print("Please press one of the options above!")