vetorNumeros = []
impar = []
par = []
print("Digite os 20 numeros: ")
for x in range(20):
    y = int(input())
    vetorNumeros.append(y)

print(vetorNumeros)
for numero in vetorNumeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(par)
print(impar)