empty_tuple = ()
empty_typle = tuple()

immutables = (int, str, tuple)

#immutables[0] = float  #TypeError

blink = ([], [])
blink[0].append(0)

print(blink)

print(hash(tuple()))

one_element_typle = (1,)
guess_what = (1)

print(type(one_element_typle))
print(type(guess_what))