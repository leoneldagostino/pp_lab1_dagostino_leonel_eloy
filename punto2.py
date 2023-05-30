'''
Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas,
incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, 
promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales,
bloqueos totales, porcentaje de tiros de campo, 
porcentaje de tiros libres y porcentaje de tiros triples.
'''
import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

indice_buscar = int(input("Indique el indice del jugador que busca: "))
print("el jugador es: {}".format(lista_datos[indice_buscar]['nombre']))
lista_estadisticas_jugador = lista_datos[indice_buscar]['estadisticas']

for estadistica,valor in lista_estadisticas_jugador.items():
    print(f'{estadistica} - {valor} ')