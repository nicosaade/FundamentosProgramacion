entrada = input("Ingrese una lista de números separados por espacios: ")
numeros = list(map(int, entrada.split()))
lideres = []

max_derecha = float('-inf')

for num in reversed(numeros):
    if num > max_derecha:
        lideres.append(num)
        max_derecha = num

lideres.reverse()

print("Números líderes:", *lideres)
