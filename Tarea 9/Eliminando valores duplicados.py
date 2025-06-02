lista = []
input_usuario = input("Digite los valores separados por un espacio: ")
for valor in input_usuario.split():
    if valor not in lista:
        lista.append(valor)
print("Lista sin duplicados:", lista)