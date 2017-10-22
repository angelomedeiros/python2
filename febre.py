T = float(input("Qual a temperatura do seu corpo em graus Celsius? "))

if T < 36.5:
    print("Seu estado é de hipotermia!")
elif T >= 36.5 and T <= 37:
    print("Seu estado é normal!")
elif T > 37 and T <= 38:
    print("Seu estado é febril!")
else:
    print("Seu estado é febril!")
