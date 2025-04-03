def calcular_estatisticas_altura_sexos(dados):
    # Inicializando variáveis para as estatísticas
    maior_altura = float('-inf')
    menor_altura = float('inf')
    soma_altura_mulheres = 0
    total_mulheres = 0
    total_homens = 0

    # Percorrendo os dados para calcular as estatísticas
    for altura, sexo in dados:
        # Calculando a maior e a menor altura
        if altura > maior_altura:
            maior_altura = altura
        if altura < menor_altura:
            menor_altura = altura
        
        # Calculando a soma das alturas das mulheres e contando o número de homens e mulheres
        if sexo == 'F':
            soma_altura_mulheres += altura
            total_mulheres += 1
        else:
            total_homens += 1

    # Calculando a média de altura das mulheres
    media_altura_mulheres = soma_altura_mulheres / total_mulheres if total_mulheres > 0 else 0

    # Calculando a diferença percentual entre homens e mulheres
    diferenca_percentual = abs(total_homens - total_mulheres) / max(total_homens, total_mulheres) * 100

    # Escrevendo as estatísticas
    print("Estatísticas:")
    print(f"Maior altura: {maior_altura}")
    print(f"Menor altura: {menor_altura}")
    print(f"Média de altura das mulheres: {media_altura_mulheres:.2f}")
    print(f"Número de homens: {total_homens}")
    print(f"Diferença percentual entre homens e mulheres: {diferenca_percentual:.2f}%")

# Coletando os dados das 50 pessoas
dados_pessoas = []
for i in range(50):
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))
    sexo = input(f"Digite o sexo da pessoa {i+1} ('M' para masculino, 'F' para feminino): ").upper()
    dados_pessoas.append((altura, sexo))

# Chamando a função para calcular e escrever as estatísticas
calcular_estatisticas_altura_sexos(dados_pessoas)