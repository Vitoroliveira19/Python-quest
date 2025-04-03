def maior_empresa_por_categoria():
    grandes = {"codigo": 0, "funcionarios": 0}
    medias = {"codigo": 0, "funcionarios": 0}
    pequenas = {"codigo": 0, "funcionarios": 0}
    micros = {"codigo": 0, "funcionarios": 0}

    while True:
        codigo = int(input("Digite o código da empresa (ou 0 para sair): "))
        if codigo == 0:
            break
        funcionarios = int(input("Digite o número de funcionários da empresa: "))
        porte = input("Digite o porte da empresa (G = Grande, M = Média, P = Pequena, Mi = Microempresa): ")

        if porte == "G" and funcionarios > grandes["funcionarios"]:
            grandes["codigo"] = codigo
            grandes["funcionarios"] = funcionarios
        elif porte == "M" and funcionarios > medias["funcionarios"]:
            medias["codigo"] = codigo
            medias["funcionarios"] = funcionarios
        elif porte == "P" and funcionarios > pequenas["funcionarios"]:
            pequenas["codigo"] = codigo
            pequenas["funcionarios"] = funcionarios
        elif porte == "Mi" and funcionarios > micros["funcionarios"]:
            micros["codigo"] = codigo
            micros["funcionarios"] = funcionarios

    print("Maiores empresas por categoria:")
    print(f"Grande empresa: Código {grandes['codigo']}, Funcionários {grandes['funcionarios']}")
    print(f"Média empresa: Código {medias['codigo']}, Funcionários {medias['funcionarios']}")
    print(f"Pequena empresa: Código {pequenas['codigo']}, Funcionários {pequenas['funcionarios']}")
    print(f"Microempresa: Código {micros['codigo']}, Funcionários {micros['funcionarios']}")

# Chamando a função para determinar as maiores empresas por categoria
maior_empresa_por_categoria()
