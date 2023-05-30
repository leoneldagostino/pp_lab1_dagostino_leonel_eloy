'''
Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
'''

import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

for jugador in lista_datos:
    print('nombre : {} - Temporadas jugadas : {}'.format(jugador['nombre'],jugador['estadisticas']['temporadas']))

temporadas_jugadas = 0
for jugador in lista_datos:
    
    if jugador['estadisticas']['temporadas'] > temporadas_jugadas:
        temporadas_jugadas = jugador['estadisticas']['temporadas']
        mayor_nombre = jugador['nombre']

print(f'numero de temporadas jugadas: {temporadas_jugadas} - {mayor_nombre}')