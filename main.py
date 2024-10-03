import math
a = float(input("Введите длину основания a: "))
b = float(input("Введите длину основания b: "))
c = float(input("Введите длину боковой стороны c: "))
d = float(input("Введите длину боковой стороны d: "))

 p = (a + b + c + d) / 2
    area = ((a+b)/math.fabs(a-b))*math.sqrt((p-a)*(p-b)*(p-a-c)*(p-a-d))
print("Площадь трапеции: ", area)
