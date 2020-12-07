lista = []
print("Digite os 10 números: ")
for item in range(10):
    numero = float(input())
    lista.append(numero)

lista.reverse()
print("-----------")
for item in lista:
    print(item)
