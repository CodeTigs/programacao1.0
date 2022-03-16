linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

if (A < (B + C)) and (B < (A + C)) and (C < (A + B)):
    p = A + B + C
    print("Perimetro =", p)
else:
    area = ((A + B) / 2) * C
    print("Area =", area)
