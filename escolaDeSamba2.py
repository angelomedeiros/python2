# coding: utf-8
# Questão: p

nota = []
x = 0

# Recebendo as notas do usuário

while True:
    A = float(input("Digite sua %d nota(digite -1 para sair): " %(x+1)))
    if A == -1:
        break
    nota.append(A)
    x+=1

# Exibe a lista das notas sem ordenação

print(nota)

# Ordenando as notas

for j in range(1,len(nota)):
    chave = nota[j]
    i = j - 1
    while i >= 0 and nota[i] > chave:
        nota[i+1] = nota[i]
        i -= 1
    nota[i+1] = chave

# Exibe as notas ordenadas

print(nota)

#Exibe a soma das notas não desprezadas

i = 1
soma = 0

for B in range(1,len(nota)-1):
    soma += nota[i]
    i += 1

print(soma)
