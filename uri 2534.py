while True:
    try:
        lista = []
        ordenados = 0
        N, Q = map(int, input().split())
        for i in range(N):
            Notas = int(input())
            lista.append(Notas)
        ordenados = sorted(lista, reverse=True)
        for i in range(Q):
            P = int(input())
            print(ordenados[P-1])
    except EOFError:
        break
