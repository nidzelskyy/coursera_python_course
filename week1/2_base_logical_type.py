#bool
print(True, type(True))
print(False, type(False))

res = True
print(type(res))

print("Equals",13 == 13, type(13 == 13))
print("Not equals", 13 != 14, type(13 != 14))


print("More", 3 > 4, type(3 > 4))
print("Less or equals", 3 <= 4, type(3 <= 4))
print("More or equals", 3 >= 4, type(3 >= 4))
print("Less", 3 < 4, type(3 < 4))

#mass equals
x = 2
print("Mass equals", 1 < x < 3, type(1 < x < 3))

print(bool(12), type(bool(12)))
print(bool(0), type(bool(0)))

x, y = True, False

print("Logical and", x and y)
print("Logical or", x or y)
print("Logical not", not y)

#lazy loads
x = 12
y = False

print(x or y, type(x or y))

x = 12
z = "boom"

print(x and z, type(x and z))

#It is a leap year?
year = 2017
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap, type(is_leap))

import calendar
print(calendar.isleap(year))