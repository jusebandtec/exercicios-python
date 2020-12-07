lista = []
print("Digite 5 numeros: ")
soma = 0
multi = 1
for numero in range(5):
    x = int(input())
    lista.append(x)
    soma += x
    multi *= x

for x in lista:
    print(x)

print("Soma:",soma)
print("Multiplicação:",multi)