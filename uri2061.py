n, m = map(int, input().split())
i = 1
acoes = []
while i <= m:
    acao = input()
    acoes.append(acao)
    i += 1

soma = n

for acao in acoes:
    if acao == 'fechou':
        soma += 1
    elif acao == 'clicou':
        soma -= 1

print(soma)