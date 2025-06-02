A = int(input("Ubicacion elevador A: "))
B = int(input("Ubicacion elevador B: "))
p = int(input("piso de usuario: "))

distanciaA = abs(A - p)
distanciaB = abs(B - p)

if distanciaA < distanciaB:
    print("Elevador A")
elif distanciaB < distanciaA:
    print("Elevador B")
elif distanciaA == distanciaB:
    print("Elevador A")
else:
    print("Error")