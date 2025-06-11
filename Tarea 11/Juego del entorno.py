def contar_vecinos(matriz, fila, col):
    filas = len(matriz)
    columnas = len(matriz[0])
    conteo = 0
    for i in range(fila - 1, fila + 2):
        for j in range(col - 1, col + 2):
            if (0 <= i < filas) and (0 <= j < columnas) and (i != fila or j != col):
                if matriz[i][j] == 1:
                    conteo += 1
    return conteo

n = int(input("Ingrese el número de filas (N): "))
m = int(input("Ingrese el número de columnas (M): "))
matriz = []

print("Ingrese las filas de la matriz binaria (solo 0 y 1), separados por comas:")
for i in range(n):
    fila = list(map(int, input(f"Fila {i + 1}: ").split(',')))
    if len(fila) != m:
        print(f"Error: La fila debe tener exactamente {m} elementos.")
        exit(1)
    matriz.append(fila)

resultado = []
for i in range(n):
    fila_resultado = []
    for j in range(m):
        vecinos = contar_vecinos(matriz, i, j)
        fila_resultado.append(vecinos)
    resultado.append(fila_resultado)

print("Resultado:")
for fila in resultado:
    print(fila)
