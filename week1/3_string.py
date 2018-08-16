example_string = "Курс про Python на Coursera"
print(example_string)
print(type(example_string))

example_string = 'Курс про "Python" на "Coursera"'
print(example_string)

example_string = "Курс про \"Python\" на \"Coursera\""
print(example_string)

#сырые строки r-string
example_string = "Файл на диске c:\\\\"
print(example_string)

example_string = r"Файл на диске c:\\"
print(example_string)

#long string
example_string = "Python cource " \
                "on Coursera " \
                "Hello world"
print(example_string)\

example_string = """
Есть всего два типа языков программирования: те, на которые
люди всё время ругаются, и те, которые никто не использует.

Bjarne Stroustrup
"""
print(example_string)

first_string = "First "
second_string = "string"
concat_string = first_string + second_string
print(first_string)
print(second_string)
print(concat_string)

print(first_string * 3)

#immutable string
example_string = "Hello"
print(id(example_string), example_string)
example_string += " world!"
print(id(example_string), example_string)

#string slice [start:stop:step]
example_string = "Курс про Python на Coursera"
print(example_string[:9])
print(example_string[9:])
print(example_string[2:9])
print(example_string[2:9:2])
print(example_string[2::2])
print(example_string[-8:])

example_string = "0123456789"
print(example_string[::2])

example_string = "Kyiv"
print(example_string[::-1])

example_string = """
Болтовня ничего не стоит. Покажи мне код.

Linus Torvalds
"""
print(example_string.count("о"))

print("kyiv".capitalize())

print("2018".isdigit())

#operator in
print("3.14" in "Number Pi = 3.1415926")
print("Алексей" in "Александр Пушкин")

#operator for .. in
example_string = "Hello"
for letter in example_string:
    print("Letter", letter)

num_string = str(901.25)
print(num_string, type(num_string))

print(bool("not empty string"))
print(bool(""))

#String formating
#first exapmle
template = "%s - главное достоинство программиста. (%s)"
print(template % ("Лень", "Larry Wall"))

#second example
print("{} не лгут, но {} пользуются формулами. ({})".format("Цифры", "лжецы", "Robert A. Heinlein"))

#third example
print("{num} Кб должно хватить для любых задач. ({author})".format(num = 640, author = "Bill Gates"))

#f-string
subject = "оптимизация"
author = "Donald Knuth"

print(f"Преждевременная {subject} - корень всех зол. ({author})")

num = 8
print(f"{num} in binary: {num:#b}")

num  = 2 / 3
print(num)

print(f"{num:.3f}")

#name = input("Enter your name: ")
#print(f"Hello, {name}")

#bytes string (b-string)
example_string = b"hello"
print(example_string, type(example_string))

for element in example_string:
    print(element)

#error using unicode
#example_bytes = b"привет"

example_string = "привет"
print(example_string)
print(type(example_string))

encoded_string = example_string.encode(encoding='utf-8')
print(encoded_string)
print(type(encoded_string))

decoded_string = encoded_string.decode(encoding='utf-8')
print(decoded_string)
print(type(decoded_string))


