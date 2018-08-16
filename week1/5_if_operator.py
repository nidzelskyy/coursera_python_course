company = "my.com"
if "my" in company:
    print("Условие выполнено!")

company = "example.net"
if "my" in company or company.endswith(".net"):
    print("Условие выполнено!")

company = "google.com"
if "my" in company:
    print("Условие выполнено!")
else:
    print("Условие не выполнено!")

company = "google.com"
if "my" in company:
    print("Подстрока my найдена")
elif "google" in company:
    print("Подстрока google найдена")
else:
    print("Подстрока не найдена")

#ternary operator
score_1 = 5
score_2 = 0
winner = "Argentina" if score_1 > score_2 else "Jamaica"
print(winner)

#while loop
i = 0
while i < 100:
    i += 1

print("while loop")
print(i)


#for loop, range object
name = "Igor"
print("String for iteration")
for letter in name:
    print(letter)

print("range for iteraion")
for i in range(3):
    print(i)

result = 0
for i in range(101):
    result += i

print("Summ of range numbers")
print(result)

print("Range diapason")
for i in range(5, 8):
    print(i)

print("Range diapason with step")
for i in range(1, 10, 2):
    print(i)

print("Revert range")
for i in range(10, 1, -1):
    print(i)


#pass operator
print("pass opertor")
for i in range(100):
    pass

#break operator
print("break operator")

result = 0

while True:
    result += 1
    if result >= 100:
        break

print(result)

print("break in for")
for i in range(10):
    if i == 5:
        break
    print(i)

#continue operator

result = 0

print("sum even numbers")
for i in range(10):
    if i % 2 != 0:
        continue
    result += i

print(result)
