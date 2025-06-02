unidades_consumidas = int(input("Ingrese el número de unidades consumidas: "))

if unidades_consumidas <= 100:
        print("No se cobra impuesto")
elif unidades_consumidas > 100 and unidades_consumidas <= 200:
        unidades_consumidas = unidades_consumidas * 0.5
        print("impuesto total $", unidades_consumidas)
elif unidades_consumidas > 200:
        unidades_consumidas = unidades_consumidas * 0.7
        print("impuesto total $", unidades_consumidas)
