empty_list = []
empty_list = list()

none_list = [None] * 10

collections = ['list', 'tuple', 'dict', 'set']

user_data = [
    ['Elena', 4.4],
    ['Andrey', 4.2]
]

list_len = len(collections)

print(list_len)
print(collections)

print(collections[0])
print(collections[-1])

collections[3] = 'frozenset'
print(collections)

#collections[10]  #IndexError

print('tuple' in collections)

range_list = list(range(10))
print(range_list)

print(range_list[1:3])
print(range_list[3:])
print(range_list[:5])

print(range_list)
print(range_list[::2])
print(range_list[::-1])
print(range_list[5:1:-1])

print(range_list[:] is range_list)

for collection in collections:
    print("Learning {}...".format(collection))

for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))

collections.append('OrderedDict')

print(collections)

collections.extend(['ponyset', 'unicorndict'])
print(collections)

collections += [None]
print(collections)

del collections[7]
print(collections)

numbers = [4, 17, 19, 9, 2, 6, 10, 13]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

tag_list = ['python', 'cource', 'courcera']
print(', '.join(tag_list))

import random

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 20))

print(numbers)
print(sorted(numbers))
print(numbers)

numbers.sort()
print(numbers)

print(sorted(numbers, reverse=True))
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(reversed(numbers))

print(list(reversed(numbers)))