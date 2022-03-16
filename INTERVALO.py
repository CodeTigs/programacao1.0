print("digite um numero para consultar seu intervalo")

x = int(input())

if 0 <= x <= 25:
    print('Intervalo [0,25]')

if 25 < x <= 50:
    print('Intervalo (25,50]')

if 50 < x <= 75:
    print('Intervalo (50,75]')

if 75 < x <= 100:
    print('Intervalo (75,100]')

else:
    print('Fora de intervalo')
