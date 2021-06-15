x = int(input("Digite um número: "))

def imprimir(numero):
    contador = 1
    while contador <= numero:
        for x in range(contador):
            print(f"{x+1}", end=" ")

        print()
        contador+=1

imprimir(x)