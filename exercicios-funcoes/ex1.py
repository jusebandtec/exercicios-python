x = int(input("Digite um número: "))

def imprimir(numero):
    contador = 1
    while contador <= numero:
        print(f"{contador}" * contador)
        contador+=1

imprimir(x)