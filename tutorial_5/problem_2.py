from functools import reduce

n = 5


def g(x, y):
    return x * y


f = reduce(g, range(1, n + 1))
print(f)
