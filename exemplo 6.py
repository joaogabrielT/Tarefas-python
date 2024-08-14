import math
import cmath

a= float(input("a:"))
b= float(input("b:"))
c= float(input("c:"))
if a ==0:
    print("Não é uma equação de segundo grau")
else:
    delta = b**2 - 4*a*c
if delta <0:
    x1= (-b + cmath.srqt(delta))/(2*a)
    x2= (-b - cmath.srqt(delta))/(2*a)
    print("Raizes complexas:",x1,"e",x2)
elif delta==0:
    x=-b / (2*a)
    print("Uma raiz real:",x)
else:
    x1=(-b + math.sqrt(delta))/(2*a)
    x2=(-b - math.sqrt(delta))/(2*a)
    print("Duas raizes reais:",x1,"e",x2)
