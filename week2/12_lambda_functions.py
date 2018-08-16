r1 = list(map(lambda x: x ** 2, range(5)))

print(r1)

print(type(lambda x: x ** 2))

r2 = list(filter(lambda x: x > 0, range(-2, 3)))

print(r2)

def stringify_list(num_list):
    return list(map(str, num_list))

r3 = list(map(lambda x: str(x), range(10)))

r4 = list(map(str, range(10)))

r5 = stringify_list(range(10))

print(r3)
print(r4)
print(r5)

from functools import reduce

def multiply(a, b):
    return a * b

r6 = reduce(multiply, range(1, 6))
print(r6)

r7 = reduce(lambda a, b: a * b, range(1, 6))
print(r7)

from functools import partial

def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)

hier = partial(greeter, greeting="Hi")
helloer = partial(greeter, greeting="Hello")

print(hier('brother'))
print(helloer('sir'))