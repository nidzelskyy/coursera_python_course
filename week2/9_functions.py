from datetime import datetime

def get_seconds():
    """Return current seconds"""
    return datetime.now().second

def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())

    return tag_list

def add(x: int, y: int) -> int:
    return x + y

def extender(source_list, extend_list):
    source_list.extend(extend_list)

def replacer(source_tuple, replace_with):
    source_tuple = replace_with

def say(greeting, name):
    print("{} {}!".format(greeting, name))

result = 0

def increment():
    result += 1
    return result

def greeting(name="tt's me..."):
    print("Hello, {}".format(name))

def printer(*args):
    print(type(args))

    for argument in args:
        print(argument)

def printer2(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))




print(get_seconds())
print(get_seconds.__doc__)
print(get_seconds.__name__)


tags = split_tags("python, courcera, mooc")

print(tags)

print(add(1, 3))
print(add("still ", "works"))

values = [1, 2, 3]
extender(values, [4, 5, 6])

print(values)

user_info = ("Guido", '31/01')
replacer(user_info, ('Larry', '27/09'))

print(user_info)

say("hello", 'Kitty')
say(name='Kitty', greeting="hello")

#print(increment()) #UnboundLocalError

greeting('IGORek')
greeting()

printer(1, 2, 3, 4, 5)

names = ['John', 'Bill', 'Amy']
printer(*names)


printer2(a=10, b=11)

payload = {
    'user_id': 117,
    'feedback': {
        'subject': "Registration fields",
        'message': 'There is no country for old men'
    }
}

printer2(**payload)