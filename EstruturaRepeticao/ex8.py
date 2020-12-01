contador = 0
numeronovo = 0
while contador < 5:
    numero2 = int(input("Digite um numero: "))
    numeronovo += numero2
    contador+=1

print('Soma: {}'.format(numeronovo))
media = numeronovo / contador
print('Média: {}'.format(media))
    
