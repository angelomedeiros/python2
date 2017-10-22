# coding: utf-8
# Questão: p

nota = [0,0,0,0]
x = 0

# Recebendo as notas do usuário

while x<4:
    nota[x]=float(input("Digite sua %d nota: " %(x+1)))
    x+=1

print(nota)

# Ordenando as notas

for j in range(1,len(nota)):
    chave = nota[j]
    i = j - 1
    while i > -1 and nota[i] > chave:
        nota[i+1] = nota[i]
        i -= 1
    nota[i+1] = chave

print(nota[1]+nota[2])


