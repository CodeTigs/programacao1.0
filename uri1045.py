linha = input().split()

a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

numeros = [a, b, c]
ordenados = sorted(numeros)

c = (ordenados[0])
b = (ordenados[1])
a = (ordenados[2])

if a >= b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a ** 2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")
    if a ** 2 > b ** 2 + c ** 2:
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b ** 2 + c ** 2:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b:
        print("TRIANGULO ISOSCELES")
    elif a == c:
        print("TRIANGULO ISOSCELES")
    elif b == c:
        print("TRIANGULO ISOSCELES")
