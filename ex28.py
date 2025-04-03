def calcular_termo(n):
    return 1 / (n ** 3)

def calcular_serie_H():
    soma = 0

    for i in range(1, 20, 4):  # Incrementando de 4 em 4 para alternar entre adição e subtração
        termo = calcular_termo(i) - calcular_termo(i + 2)
        soma += termo

    return soma

# Chamando a função para calcular a soma dos dez primeiros termos da série H
soma_H = calcular_serie_H()
print(f"A soma dos dez primeiros termos da série H é: {soma_H}")
