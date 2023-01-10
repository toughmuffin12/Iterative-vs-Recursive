import time

Pi = 3.14159

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

iterativestart = time.clock()
iterativePower(Pi, 100)
iterativeend = time.clock()
print("The iterative function took: ", (iterativeend-iterativestart) * 10**-9, "ns")

recursivestart = time.clock()
recursivePower(Pi, 100)
recursiveend = time.clock()
print("The recursive function took: ", (recursiveend-recursivestart) * 10**-9, "ns")

