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

x = iterativePower(Pi, 5)
y = recursivePower(Pi, 5)

print(x, y)

#Record start time
start = time.time()

iterativePower(Pi, 13)

#Record end time
end = time.time()

print("The time it took for the iterative function was:", (end-start) * 10**9, "ns")

#Record start time
start = time.time()

recursivePower(Pi, 13)

#Record end time
end = time.time()

print("The time it took for the recursive function was:", (end-start) * 10**9, "ns")

