import numpy as np

my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)
zeros = np.zeros(5)
print(zeros)
ones = np.ones(5)
print(ones)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2
resultado = arr1 * arr2

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],])

promedio_por_hogar = np.mean(consumo, axis=1)
promedio_por_dia = np.mean(consumo, axis=0)
total_consumo = np.sum(consumo)

maximos= np.max(consumo, axis=1)
minimos = np.min(consumo, axis=0)
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

consumo_total_hogar = np.sum(consumo, axis=1)
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total por hogar semanal: {consumo_total_hogar}")
altos = consumo_total_hogar > 100
consumo_mayor_100 = np.where(altos)[0] 
print(f"Hogares con consumo total mayor a 100: {consumo_mayor_100}")

consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

#1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)? Respuesta: 17.4
#2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo. Respuesta: [12. 16.7 9.3]
#3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6). Respuesta: 13.801428571428573
#4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto. 
# Respuesta: Día con mayor desviación estándar: Sábado. Esto indica que el sábado hay mayor variabilidad entre el consumo de diferentes hogares.
#5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores. Respuesta: Índices: [9 3 1] Valores: [62.6 66.1 76.1]
#6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal? Respuesta: 121.22