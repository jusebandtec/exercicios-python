notas = []
soma = 0
print("Digite as 4 notas: ")
for y in range(4):
    x = float(input())
    notas.append(x)

for nota in notas:
    soma += nota

print("Média:",soma / len(notas))