# Função para converter Fahrenheit para  celsius 
def fahrenheit_para_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

# Inicializando variáveis
fahrenheit_inicial = 50
fahrenheit_final = 150
passo = 1

# Imprimindo cabeçalho da tabela
print("Fahrenheit   Celsius")

# Loop para calcular e imprimir a tabela
for fahrenheit in range (fahrenheit_inicial, fahrenheit_final + 1, passo):
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit}         {celsius}")