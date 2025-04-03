def calcular_porcentagem(votos, total_votos):
    if total_votos == 0:
        return 0
    return (votos / total_votos) * 100

def escrutinio():
    candidatos = [0, 0, 0, 0]  # Índice 0 não é usado, índices 1 a 4 representam os candidatos
    votos_nulos = 0
    votos_branco = 0
    total_votos = 0

    while True:
        voto = int(input("Digite o código do voto (0 para finalizar): "))
        if voto == 0:
            break
        elif voto >= 1 and voto <= 4:
            candidatos[voto] += 1
        elif voto == 5:
            votos_nulos += 1
        elif voto == 6:
            votos_branco += 1
        total_votos += 1

    print("Resultado da Escrutinagem:")
    print("==========================")
    for i in range(1, 5):
        porcentagem = calcular_porcentagem(candidatos[i], total_votos)
        print(f"Total de votos para o candidato {i}: {candidatos[i]}, {porcentagem:.2f}% do total.")
    porcentagem_nulos = calcular_porcentagem(votos_nulos, total_votos)
    porcentagem_branco = calcular_porcentagem(votos_branco, total_votos)
    print(f"Total de votos nulos: {votos_nulos}, {porcentagem_nulos:.2f}% do total.")
    print(f"Total de votos em branco: {votos_branco}, {porcentagem_branco:.2f}% do total.")
    print(f"Total de votos registrados: {total_votos}")

# Chamando a função principal
escrutinio()
