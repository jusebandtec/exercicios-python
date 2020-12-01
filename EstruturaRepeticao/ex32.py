fatorial = int(input("Fatorial de: "))
f = fatorial
numero = 1
print('{}! = '.format(fatorial),end='')
while f > 0:
    print('{}'.format(f), end='')
    print('.' if f > 1 else ' =',end='')
    numero *= f
    f -=1
print(" {}".format(numero),end='')

 
     
# lista.sort(reverse=True)
# print(lista)
# print('{}! = {}'.format(fatorial, multiplyList(lista)))

    
