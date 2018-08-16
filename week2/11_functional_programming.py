def caller(func, params):
    return func(*params)

def printer(name, origin):
    print("I'm {} of {}!".format(name, origin))

caller(printer, ['Moana', 'Motunui'])

def get_multiplier():
    def inner(a, b):
        return a * b
    return inner

multiplier = get_multiplier()
print(multiplier(10, 11))
print(multiplier.__name__)


def get_multiplier2(number):
    def inner(a):
        return a * number
    return inner

multiplier_by_2 = get_multiplier2(2)
print(multiplier_by_2(10))

def squarify(a):
    return a ** 2

r1 = list(map(squarify, range(5)))

print(r1)

squarify_list = []

for number in range(5):
    squarify_list.append(squarify(number))

print(squarify_list)

def is_positive(a):
    return a > 0

r2 = list(filter(is_positive, range(-2, 3)))

print(r2)

positive_list = []

for number in range(-2, 3):
    if is_positive(number):
        positive_list.append(number)

print(positive_list)