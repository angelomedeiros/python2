print("Digite para as perguntas abaixo, s para sim e n para não!")

estudante = input("Você é estudante? ")
trabalhador = input("Você é trabalhador da indústria? ")
socio = input("Você é sócio do Clube de Viagem? ")
aposentado = input("Você é aposentado? ")

desconto = 0

if estudante == "s":
    desconto = 50

if trabalhador == "s":
    if desconto < 30:
        desconto = 30

if socio == "s":
    if desconto < 80:
        desconto = 80

if aposentado == "s":
    desconto = 0
    if estudante == "s":
        desconto += 50
    if trabalhador == "s":
        desconto += 30
    if socio == "s":
        desconto += 80
    desconto += 100

print("Seu desconto será de %4.2f" %desconto)
