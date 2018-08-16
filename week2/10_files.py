f = open('test.txt', 'w')

text_modes = ['r', 'w', 'a', 'r+']
binary_modes = ['br', 'bw', 'ba', 'br+']


f.write("The world is changed. \nI taste it in the watter.\n")

f.close()

f = open('test.txt', 'r+')

f.read()

f.tell()

f.read()

f.seek()
f.read()

f.close()

f = open('test.txt', 'r+')
f.readline()
f.close()

f = open('test.txt', 'r+')
f.readlines()
f.close()

with open('test.txt') as f:
    print(f.read())

