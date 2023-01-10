#Import time module
import time
import timeit
Pi = 3.14159

#Record start time
start = time.time()

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

t0 = time.clock()
iterativePower(Pi, 100)
#print("Hello")
t1 = time.clock()
print("Time elapsed: ", t1 - t0)

#Print differince between start and end time in nano secs.
#print("The time of execution of above program is: ",
     #(end-start) * 10**100, "ns")