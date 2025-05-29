import random 
numero = random.randint(1, 100)

while True:
    try:
        adivina = int(input("Adivina el número entre 1 y 100: "))
        if adivina < 1 or adivina > 100:
            print("Por favor, introduce un número entre 1 y 100.")
            continue
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero entre 1 y 100.")
        continue

    if adivina < numero:
        print("El numero secreto es menor")
    elif adivina > numero:
        print("El numero secreto es mayor")
    else:
        print("¡Felicidades!, Has adivinado el número secreto.")
        break