square_list = []

for number in range(10):
    square_list.append(number ** 2)

print(square_list)

square_list2 = [number ** 2 for number in range(10)]
print(square_list2)

even_list = []

for number in range(10):
    if number % 2 == 0:
        even_list.append(number)

print(even_list)

even_list2 = [num for num in range(10) if num % 2 == 0]
print(even_list2)

square_map = {number: number **2 for number in range(5)}

print(square_map)

reminders_set = {num %10 for num in range(100)}

print(reminders_set)

print(type(num ** 2 for num in range(5)))

num_list = range(7)
squared_list = [x ** 2 for x in num_list]

r1 = list(zip(num_list, squared_list))

print(r1)

r2 = list(zip(
  filter(bool, range(3)),
  [x for x in range(3) if x]
))

print(r2)