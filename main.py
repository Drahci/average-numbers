numeros = []

quantidade = int(input("Quantos números você gostaria de inserir? "))

soma = 0

for i in range(quantidade):
    numero = float(input(f"Insira o número {i+1}: "))
    numeros.append(numero)
    soma += numero

media = soma / quantidade

print("A média dos números é:", media)
