import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

'''
Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. 
 
El archivo CSV debe contener los siguientes campos: 
nombre, posición, 
temporadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, 
asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, 
porcentaje de tiros libres y porcentaje de tiros triples.
'''

indice_buscar = int(input("Indique el indice del jugador que busca: "))
print("el jugador es: {}".format(lista_datos[indice_buscar]['nombre']))
nombre_jugador = lista_datos[indice_buscar]['nombre'].replace(" ","_")
lista_estadisticas_jugador = lista_datos[indice_buscar]['estadisticas']


for estadistica,valor in lista_estadisticas_jugador.items():
    print(f'{estadistica} - {valor} ')

with open(f"Estadistica_{nombre_jugador}.csv",'w') as archivo:
    contenido = ''
    for estadistica_jugador,valor in lista_estadisticas_jugador.items():
        contenido += f'{estadistica_jugador} : {valor}.\n'
    archivo.write(contenido)

