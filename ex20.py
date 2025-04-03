def calcular_graos(tabuleiro=8):
    graos = 1
    total_graos = 0
    for _ in range(tabuleiro):
        total_graos += graos
        graos *= 2
    return total_graos

# Exemplo de uso
tabuleiro = 64  # Número de casas no tabuleiro de xadrez
total = calcular_graos(tabuleiro)
print(f"O número total de grãos esperado pelo monge é: {total}")