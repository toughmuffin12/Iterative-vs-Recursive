#Import time module
import time

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

iterativePower(Pi, 13)

#Record end time
end = time.time()

print(start * 10**9)
print(end * 10**9)

#Print differince between start and end time in nano secs.
print("The time of execution of above program is: ",
     (end-start) * 10**100, "ns")