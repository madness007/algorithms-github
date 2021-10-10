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




# Ex2
print("Row of Lucas to 1.000.000: " + str(rowLucas(4000000)))
