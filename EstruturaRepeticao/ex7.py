contador = 1
numeronovo = 10 ** 23
while contador < 6:
    numero2 = int(input("Digite um numero: "))
    if numeronovo > numero2:
        numeronovo = numero2
    contador+=1

print(numeronovo)
    
