# Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20
# números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

lista = []
i = 0
numero = int(input("digite a quantidade de entradas: "))

while (i < numero):
    numero1 = str(input("Valor: "))
    i += 1
    lista.append(numero1)

lista.reverse()

print(lista)
