linha = input().split()

a = int(linha[0])
b = int(linha[1])

if (a % b == 0) or (b % a == 0):
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")