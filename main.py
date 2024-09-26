import math

def trapezoid_area(a, b, c, d):
    p = (a + b + c + d) / 2
    
    area = math.sqrt((p - a) * (p - b) * (p - c) * (p - d))
    return area

a = float(input("Введите длину основания a: "))
b = float(input("Введите длину основания b: "))
c = float(input("Введите длину боковой стороны c: "))
d = float(input("Введите длину боковой стороны d: "))

area = trapezoid_area(a, b, c, d)
print(f"Площадь трапеции: {area}")