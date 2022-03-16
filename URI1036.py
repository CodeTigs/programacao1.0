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
