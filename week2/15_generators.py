def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2

print(list(even_range(0,10)))

def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b

print(list(fibonacci(20)))

def accumulator():
    total = 0
    while True:
        value = yield total
        print("Got: {}".format(value))

        if not value: break
        total += value

generator = accumulator()

next(generator)

print("Accumulated:{}".format(generator.send(1)))
print("Accumulated:{}".format(generator.send(1)))
print("Accumulated:{}".format(generator.send(2)))
next(generator)