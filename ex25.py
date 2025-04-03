def calcular_valor_H():
    valor_H = 0
    numerador = 1
    denominador = 1

    while denominador <= 50:
        termo = numerador / denominador
        valor_H += termo
        numerador += 2
        denominador += 1

    return valor_H

# Chamando a função para calcular o valor de H
valor_H = calcular_valor_H()
print(f"O valor de H é: {valor_H}")