def fibo_generator():
    current_term = 0
    next_term = 1
    while True:
        yield current_term
        current_term, next_term = next_term, current_term + next_term


fibo_generator_object = fibo_generator()

print(next(fibo_generator_object))
print(next(fibo_generator_object))

for idx in range(48):
    print(next(fibo_generator_object), end=",")
