def inserir_ordenado(lista, elemento):
    index = 0
    for i in range(len(lista)):
        if elemento > lista[i]:
            index = i + 1
        else:
            break
    lista.insert(index, elemento)

# Exemplo de uso:
lista_ordenada = ['a', 'c', 'e', 'g', 'i']
novo_elemento = 'f'
inserir_ordenado(lista_ordenada, novo_elemento)
print(lista_ordenada)  # Saída esperada: ['a', 'c', 'e', 'f', 'g', 'i']