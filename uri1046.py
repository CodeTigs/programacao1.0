horas = input().split()
i = int(horas[0])
f = int(horas[1])

if i > f:
    a = 24-i
    h = a+f
    print("O JOGO DUROU", h, "HORA(S)")
elif i == f:
    h = 24
    print("O JOGO DUROU", h, "HORA(S)")
elif i < f:
    h = f - i
    print("O JOGO DUROU", h, "HORA(S)")
