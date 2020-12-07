mediaNotas = []
notas = []
print("Digite as notas: ")
for x in range(10):
    media = 0
    print("Aluno",x+1)
    for i in range(4):
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        media += nota
    media = media/4
    mediaNotas.append(media)

for notas in mediaNotas:
    if notas >= 7:
        print(len(notas))
