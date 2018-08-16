num = 1
print(num, type(num))

big_num = 1_000_000
print(big_num, type(big_num))

num_float = 3.1415
print(num_float, type(num_float))

big_num_float = 1_000_000.000_001
print(big_num_float, type(big_num_float))

exp_float_num = 1.5e2
print(exp_float_num, type(exp_float_num))

float_to_int = int(num_float)
print(float_to_int, type(float_to_int))

int_to_float = float(num)
print(int_to_float, type(int_to_float))

complex_num = 14 + 1j
print(complex_num, type(complex_num), complex_num.real, complex_num.imag)

str = "Some string"
print(str, type(str))


sum1 = 1 + 2
print(sum1, type(sum1))

sum2 = 1 + 2.0
print(sum2, type(sum2))

sub1 = 10 - 1
print(sub1, type(sub1))

sub2 = 10 - 1.0
print(sub2, type(sub2))

div1 = 10 / 2
print(div1, type(div1))

#div2 = 10 / 0  #ZeroDivisionError

mul1 = 4 * 5.25
print(mul1, type(mul1))

mul2 = 4 * 5
print(mul2, type(mul2))

num_sqrt = 4 ** 2
print(num_sqrt, type(num_sqrt))

num_sqrt2 = 4 ** (1 / 2)
print(num_sqrt2, type(num_sqrt2))

num_sqrt3 = 4 ** -2
print(num_sqrt3, type(num_sqrt3))

div_ceil = 10 // 3
print(div_ceil, type(div_ceil))

div_rem = 10 % 3
print(div_rem, type(div_rem))

print(10 * 3 + 3)
print(10 * (3 + 3))


x = 4
y = 3

print("Побитовое или:", x | y)
print("Побитовое исключающее или:", x ^ y)
print("Побитовое и:", x & y)
print("Побитовый сдвиг влево:", x << 3)
print("Побитовое сдвиг вправо:", x >> 1)
print("Инверсия битов:", ~x)

#нахождение гипотенузы
#распаковка значений
x1, y1 = 0, 0
x2 = 3
y2 = 4

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Решение:", distance, type(distance))

#меняем местами 2 значения
a = 100
b = 200
print("Before", a, b)

a, b = b, a
print("After", a, b)


#immutable example
x = y = 0
x += 1
print(x, y)

#mutable example
x = y = []
x.append(1)
x.append(2)

print(x, y)