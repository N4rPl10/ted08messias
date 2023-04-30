# Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
# números repetidos no vetor VET e em que posições se encontram.

lista = []
i = 0
numero = int(input("digite a quantidade de entradas: "))

while i < numero:
    numero1 = int(input("Valor: "))
    i += 1
    lista.append(numero1)
duplicados = set([x for x in lista if lista.count(x) > 1])
duplicadop = []
positionsdup = []
for duplicate in duplicados:
    positions = [i for i, x in enumerate(lista) if x == duplicate]
    duplicadop.append(duplicate)
    positionsdup.append(positions)

print(f"os numeros duplicados são {duplicadop} e as posições são {positionsdup}")

