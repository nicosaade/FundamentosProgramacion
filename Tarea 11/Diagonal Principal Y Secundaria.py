def obtener_diagonales(matriz):
    n = len(matriz)
    diagonal_principal = [matriz[i][i] for i in range(n)]
    diagonal_secundaria = [matriz[i][n - 1 - i] for i in range(n)]
    return diagonal_principal, diagonal_secundaria

n = int(input("Ingrese la dimensión de la matriz (N): "))
matriz = []

print("Ingrese las filas de la matriz, separando los números con comas:")
for i in range(n):
    fila = list(map(int, input(f"Fila {i + 1}: ").split(',')))
    if len(fila) != n:
        print("Error: la fila debe tener exactamente", n, "elementos.")
        exit(1)
    matriz.append(fila)

diag_principal, diag_secundaria = obtener_diagonales(matriz)

print("Diagonal principal:", diag_principal)
print("Diagonal secundaria:", diag_secundaria)
