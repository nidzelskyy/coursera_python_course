import functools

def decorator(func):
    return func

@decorator
def decorated():
    print("Hello!")

#decorated = decorator(decorated)


def decorator2(func):
    def new_func():
        pass
    return new_func

@decorator2
def decorated2():
    print("Hello!")

decorated2()

print(decorated2.__name__)


def stringify(func):
  return str(func)


@stringify
def multiply(a, b):
  return a * b


print(multiply)

def logger(func):
    @functools.wraps(func)
    def wrapped(*argsm, **kwargs):
        result = func(*argsm, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)

r1 = summator([1,2,3,4,5])
print(summator.__name__)

print(r1)

with open('log.txt', 'r') as f:
    print('log.txt: {}'.format(f.read()))


def logger(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))

            return result
        return wrapper
    return decorator

@logger('new_log.txt')
def summator(num_list):
    return sum(num_list)

r2 = summator([1,2,3,4,5,6])
print(r2)
print(summator.__name__)

with open('new_log.txt', 'r') as f:
    print('new_log.txt: {}'.format(f.read()))

def first_decorator(func):
    def wrapped():
        print("Inside first_decorator product")
        return func()
    return wrapped

def seccond_decorator(func):
    def wrapped():
        print("Inside second_decorator product")
        return func()
    return wrapped

@first_decorator
@seccond_decorator
def decorated():
    print('Finally called...')

# decorated = first_decorator(seccond_decorator(decorated))

decorated()

def bold(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped

def italic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@bold
@italic
def hello():
    return "Hello world"

#hello = bold(italic(hello))

print(hello())