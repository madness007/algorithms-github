# Ex1
def naturalSum(min, max):
    __min = min
    __max = max
    __value = 0

    for x in range(__min, __max + 1):
        if  x%7 == 0 or x%9 == 0:
            __value += x
    return __value
# Ex2
def rowLucas(max):
    __lucas = [2, 1]
    __x = 1
    __value = 0
    while __lucas[__x] < max:
        if __lucas[__x] % 2 == 1:
            __value += __lucas[__x]
        __x += 1
        __lucas.append(__lucas[__x - 1] + __lucas[__x - 2])
    return __value




# Ex1
print("natural sum to 20: " + str(naturalSum(0,20)))
print("natural sum to 10000: " + str(naturalSum(0,10000)))

# Ex2
print("Row of Lucas to 1.000.000: " + str(rowLucas(4000000)))

