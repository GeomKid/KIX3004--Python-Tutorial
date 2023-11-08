from functools import reduce

c = [3 + 4j, 5, 5j]
mapped = map(abs, c)

m = reduce(lambda x, y: x + y, mapped)
print(m)
