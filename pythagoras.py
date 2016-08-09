import math

a = int(input("Tell A"))
b = int(input("Tell B"))

def pythagoras(a, b):
        if (a > 0 and b > 0):
            value = math.sqrt(a * a + b * b)
            return value
        else:
            return -1
result = pythagoras(a, b)
print(result)