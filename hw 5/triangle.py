print("Стороны:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a + b > c and a + c > b and b + c > a:
        P = a + b + c
        print(P)
        print(bool(P))
    if  a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        S = pow(p * (p - a) * (p - b) * (p - c), 1 / 2)
        print(S)
        print (bool(S))


else:
    print("Треугольник не существует")