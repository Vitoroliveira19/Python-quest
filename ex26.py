def calcular_valor_S():
    valor_S = 0

    for i in range(1, 11):
        termo = (-1) ** (i + 1) * i / (i ** 2)
        valor_S += termo

    return valor_S

# Chamando a função para calcular o valor de S
valor_S = calcular_valor_S()
print(f"O valor de S é: {valor_S}")