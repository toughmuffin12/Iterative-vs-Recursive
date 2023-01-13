#Import modules
import time
import pandas as pd

base = 3.14159265359

#Iterative Power Implementation
def iterativePower(base, exponent) :
    retVal = 1.0
    if exponent < 0 :
        return 1.0 / iterativePower(base, -exponent)
    else :
        for x in range(0, exponent) :
            retVal *= base
            x + 1 
    return retVal

#Recusive Power Implemetation
def recursivePower(base, exponent) :
    if exponent < 0 :
        return 1.0 / recursivePower(base, -exponent)
    elif exponent == 0 :
        return 1.0
    else :
        return base * recursivePower(base, exponent - 1)

#Declration of lists
n = []
iterativeresultslist = []
recursiveresultslist = []

for x in range(-1, 997):
    #Get current processor time for iteration function
    it0 = time.time()

    iterativePower(base, x)

    #Get current processor time for iteration function
    it1 = time.time()

    iterativeresultslist.append("{:.2f}".format((it1-it0) * 10**9))

    #Get current processor time for recursive function
    rt0 = time.time()

    recursivePower(base, x)

    #Get current processor time for recursive function
    rt1 = time.time()

    recursiveresultslist.append("{:.2f}".format((rt1-rt0) * 10**9))

    n.append(x)
    x + 1

#Naming the columns 
col1 = "n"
col2 = "iterative-time (ns)"
col3 = "recursive-time (ns)"



#Creating the data frames and 
data = pd.DataFrame({col1:n, col2:iterativeresultslist, col3:recursiveresultslist})
data.to_excel('Iterative_vs_Recursive_results.xlsx', sheet_name='sheet1', index=False)

