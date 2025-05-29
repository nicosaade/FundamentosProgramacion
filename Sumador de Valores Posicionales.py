numero = int(input("Ingresa un número: "))

def sumar_digitos(numero):
    print(f"Proceso de reducción para {numero}:")
    while numero >= 10:
        numero = sum(int(digito) for digito in str(numero))
        print(numero)
    return numero

if 1 <= numero <= 10**9:
    resultado = sumar_digitos(numero)
    print(f"El resultado final es: {resultado}")
else:
    print("Número invalido")