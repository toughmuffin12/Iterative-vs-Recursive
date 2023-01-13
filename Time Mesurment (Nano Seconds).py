#Import modules
import time

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

#Get current processor time for recursive function
rt0 = time.time()

recursivePower(base, 2)

#Get current processor time for recursive function
rt1 = time.time()

print("Recursive function with exponet 2:", "{:.2f}".format((rt1-rt0) * 10**9), "ns")

#Get current processor time for recursive function
it0 = time.time()

iterativePower(base, 3)

#Get current processor time for recursive function
it1 = time.time()

print("Iterative function with exponet 3:", "{:.2f}".format((it1-it0) * 10**9), "ns")

