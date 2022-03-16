while True:
    try:
        cont = 0
        cont2 = 0
        calculo = 0
        N = int(input())
        Votos = (input().split())
        for i in range(N):
            if (int(Votos[cont])) == 1:
                cont2 += 1
            cont += 1
        calculo = (N / 3) * 2
        if cont2 >= calculo:
            print("impeachment")
        else:
            print("acusacao arquivada")

    except EOFError:
        break
