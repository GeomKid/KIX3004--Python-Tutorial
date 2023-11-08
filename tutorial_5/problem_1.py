from functools import reduce

a = [10, 30, 20]


def f(x, y):
    return x if x > y else y


m = reduce(f, a)
print(m)
