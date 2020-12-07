caracteres = []
print("Digite 10 caracteres")
for x in range(10):
    caractere = str(input())
    caracteres.append(caractere)

for letra in caracteres:
    if letra == 'a':
        caracteres.remove('a')
    elif letra == 'e':
        caracteres.remove('e')
    elif letra == 'i':
        caracteres.remove('i')
    elif letra == 'o':
        caracteres.remove('o')
    elif letra == 'u':
        caracteres.remove('u')

print(caracteres)
print(len(caracteres))