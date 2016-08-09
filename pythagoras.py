import math

a = int(input("Tell A"))
b = int(input("Tell B"))

if (a > 0 and b > 0):
    def pythagoras(a, b):
        value = math.sqrt(a * a + b * b)
        return value
    result = pythagoras(a, b)
    print(result)
else:
    print('-1')