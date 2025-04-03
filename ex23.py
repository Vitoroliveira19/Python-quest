def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos_entre_n1_e_n2(n1, n2):
    primos = []
    for num in range(n1, n2 + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

# Solicitando os números naturais ao usuário
n1 = int(input("Digite o primeiro número natural: "))
n2 = int(input("Digite o segundo número natural: "))

# Imprimindo os números primos no intervalo fornecido
print(f"Números primos entre {n1} e {n2}:")
print(numeros_primos_entre_n1_e_n2(n1, n2))