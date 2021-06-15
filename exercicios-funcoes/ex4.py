def positivo_negativo(numero):
    if numero <= 0:
        return 'N'
    else:
        return 'P'

print(positivo_negativo(int(input("Digite um número: "))))