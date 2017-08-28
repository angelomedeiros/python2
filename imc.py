massa = float(input("Qual o valor da sua massa corporal em Kilogramas? "))
altura = float(input("Qual a sua altura em metros? "))

imc = massa/altura**2

if imc < 20:
    print("Seu estado é de desnutição!")
elif imc >= 20 and imc <= 25:
    print("Seu estado é Normal!")
elif imc > 25 and imc <= 30:
    print("Você está acima do peso!")
elif imc > 30 and imc <= 40:
    print("Seu estado é de obesidade leve!")
elif imc > 40:
    print("Seu estado é de obesidade grave!")

