"""
nome, conta, saldo = input().split()
conta = int(conta)
saldo = float(saldo)

print("o cliente %s, com o numero da conta %d tem %.2f reais de saldo"%(nome, conta, saldo))


notaA = 5.0
notaB = 6.0
notaC = 7.0

media = ((notaA * 2) + (notaB * 3) + (notaC * 5)) / 10

print("MEDIA = %.1f" %(media))



import math
line = str(input(""))

split = line.split(" ")

A = float(split[0])
B = float(split[1])
C = float(split[2])

try:
    x1 = ((-B) + math.sqrt(math.pow(B, 2) - (4*A*C))) / (2*A)
    x2 = ((-B) - math.sqrt(math.pow(B, 2) - (4*A*C))) / (2*A)

    print("R1 = {0:.5f}".format(x1))
    print("R2 = {0:.5f}".format(x2))

except ValueError:
    print("Impossivel calcular")
except ZeroDivisionError:
    print("Impossivel calcular")


A, B, C = input().split()
A, B, C = float(A), float(B), float(C)
DELTA = (B ** 2) - (4 * A * B)

if DELTA < 0 or A == 0 :
    print("impossivel calcular")
else:
    R1 = (-B + DELTA ** (1 / 2)) / (2 * A)
    R2 = (-B - DELTA ** (1 / 2)) / (2 * A)
    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)
"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print('DIFERENCA =', (A*B) + (C*D))





