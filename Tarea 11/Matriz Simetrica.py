def es_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

n = int(input("Ingrese la dimensión de la matriz (N): "))
matriz = []

print("Ingrese las filas de la matriz, separando los números con comas:")
for i in range(n):
    fila = list(map(int, input(f"Fila {i + 1}: ").split(',')))
    if len(fila) != n:
        print("Error: la fila debe tener exactamente", n, "elementos.")
        exit(1)
    matriz.append(fila)

if es_simetrica(matriz):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
