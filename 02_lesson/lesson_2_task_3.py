import math

def square(t):
    return math.ceil(t*t)


t=float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата:{square(t)}")


