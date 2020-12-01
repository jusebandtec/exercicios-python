contador = 1
while contador < 21:
    print(contador)
    contador+=1

for x in range(20):
    print(x+1,end='')
    print("," if x < 19 else ".",end='')