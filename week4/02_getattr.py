class Researcher:
    def __getattr__(self, name):
        return 'Nothing found :('

    def __getattribute__(self, name):
        return 'nope'

class Researcher2:
    def __getattr__(self, name):
        return 'Nothing found :('

    def __getattribute__(self, name):
        print('Looking for {}'.format(name))
        return object.__getattribute__(self, name)

class Ignorant:
    def __setattr__(self, key, value):
        print('Not gonna set {}!'.format(key))

class Polite:
    def __delattr__(self, item):
        value = getattr(self, item)
        print(f"Goodbye {item}, you were {value}!")

        object.__delattr__(self, item)

class Logger:
    def __init__(self, filename):
        self.filename = filename

    # def __call__(self, func):
    #     with open(self.filename, 'w') as f:
    #         f.write('Oh Danny boy...')
    #     return func

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            with open(self.filename, 'a') as f:
                f.write('Oh Danny boy...')

            return func(*args, *kwargs)

        return wrapped

obj = Researcher()

print(obj.attr)
print(obj.method)
print(obj.DFG2H3J00KLL)


obj2 = Researcher2()

print(obj2.attr)
print(obj2.method)
print(obj2.DFG2H3J00KLL)

obj3 = Ignorant()
obj3.math = True
#print(obj3.math)   #AttributeError

obj4 = Polite()

obj4.attr = 10
del obj4.attr


logger = Logger('log.txt')

@logger
def completely_useless_function():
    pass

completely_useless_function()

with open('log.txt', 'r') as f:
    print(f.read())