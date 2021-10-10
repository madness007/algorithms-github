# Ex1
def naturalSum(min, max):
    __min = min
    __max = max
    __value = 0

    for x in range(__min, __max + 1):
        if  x%7 == 0 or x%9 == 0:
            __value += x
    return __value



print("natural sum to 20: " + str(naturalSum(0,20)))
print("natural sum to 10000: " + str(naturalSum(0,10000)))

