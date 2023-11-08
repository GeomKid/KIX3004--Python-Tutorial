from functools import reduce

a = [1, -2, 5, 6, 8]
filtered = filter(lambda x: x > 0, a)
t = reduce(lambda x, y: x + y, filtered)
print(t)
