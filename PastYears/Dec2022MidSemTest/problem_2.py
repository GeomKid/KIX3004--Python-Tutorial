# It maks it easier to ascess and store as variables and be called whenever it is needed

# Output printed with erros in Code:
# 1

# Error 1: Comparision in r(x,y) is wrong
# Error 2: after mapping we are unable to get the initial values ,
# so we should also add the values in a set after mapping
# Error 3: The reduce returns only the value of magnitude,
# we should change it so that it compares the magnitude in the mapped set and return the initial value

from functools import reduce


def m(x):
    # abs(x) returns magnitude of complex number
    # Eg: abs(3+4j)= 5.0
    return (x, abs(x))


def f(x):
    return type(x) == complex


def r(x, y):
    if x[1] > y[1]:
        return x[0]
    else:
        return y[0]


l = [3 + 4j, "Hello", -1j, "World"]
print(reduce(r, map(m, filter(f, l))))
