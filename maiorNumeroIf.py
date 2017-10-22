a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if (a>b and a>c):
    print("O primeiro número é maior!")
else:
    if (b>a and b>c):
        print("O segundo número é maior!")
    else:
        print("O terceiro número é maior!")
