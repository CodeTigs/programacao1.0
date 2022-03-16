salario = float(input())

if salario >= 0 and salario <= 400.00:
    novoSalario = salario * 1.15
    reajuste = novoSalario - salario
    print("Novo salario: %0.2f" % novoSalario)
    print("Reajuste ganho: %0.2f" % reajuste)
    print("Em percentual: 15 %")

if salario >= 400.01 and salario <= 800.00:
    novoSalario = salario * 1.12
    reajuste = novoSalario - salario
    print("Novo salario: %0.2f" % novoSalario)
    print("Reajuste ganho: %0.2f" % reajuste)
    print("Em percentual: 12 %")

if salario >= 800.01 and salario <= 1200.00:
    novoSalario = salario * 1.10
    reajuste = novoSalario - salario
    print("Novo salario: %0.2f" % novoSalario)
    print("Reajuste ganho: %0.2f" % reajuste)
    print("Em percentual: 10 %")

if salario >= 1200.01 and salario <= 2000.00:
    aumento = salario * 7 / 100
    novoSalario = salario + aumento
    reajuste = novoSalario - salario
    print("Novo salario: %0.2f" % novoSalario)
    print("Reajuste ganho: %0.2f" % reajuste)
    print("Em percentual: 7 %")

if salario > 2000.00:
    aumento = salario * 4 / 100
    novoSalario = salario + aumento
    reajuste = novoSalario - salario
    print("Novo salario: %0.2f" % novoSalario)
    print("Reajuste ganho: %0.2f" % reajuste)
    print("Em percentual: 4 %")
