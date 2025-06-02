numero = int(input("Introduce un numero: "))

if numero % 7 == 0 and numero % 5 != 0:
    print("Magico")
else:
    print("Normal")