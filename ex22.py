def possibilidades_soma_7():
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            if dado1 + dado2 == 7:
                print(f"Dado 1: {dado1}, Dado 2: {dado2}")

# Chamando a função para imprimir as possibilidades
print("Possibilidades de soma igual a 7:")
possibilidades_soma_7()