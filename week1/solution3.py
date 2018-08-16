import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
elif d == 0:
    x1 = x2 = -b / (2 * a)
else:
    x1 = x2 = None

if not x1 is None:
    print(int(x1))
    print(int(x2))
else:
    print("Корней уравнения нет")