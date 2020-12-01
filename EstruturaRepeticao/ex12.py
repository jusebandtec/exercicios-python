numero = int(input("Digite um número da tabuada:"))
f = numero
for x in range(10):
    x +=1
    print("{} X {} = {}".format(f, x, f*x))

contador = 1
while contador < 11:
    print("{} X {} = {}".format(f, contador, numero*contador))
    contador+=1
