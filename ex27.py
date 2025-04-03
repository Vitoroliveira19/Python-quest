def calcular_soma_serie():
    soma = 0
    numerador = 2
    denominador = 500
    sinal = 1

    for _ in range(10):
        termo = sinal * numerador / denominador
        soma += termo
        sinal *= -1
        if sinal == 1:
            numerador = 2
        else:
            numerador = 5
        denominador -= 50

    return soma

# Chamando a função para calcular a soma da série
soma_serie = calcular_soma_serie()
print(f"A soma dos dez primeiros termos da série é: {soma_serie}")
