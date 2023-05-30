'''
Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales
'''

import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

for jugador in lista_datos:
    print('nombre : {} - bloqueos totales : {}'.format(jugador['nombre'],jugador['estadisticas']['bloqueos_totales']))

bloqueos_totales = 0
for jugador in lista_datos:
    
    if jugador['estadisticas']['bloqueos_totales'] > bloqueos_totales:
        bloqueos_totales = jugador['estadisticas']['bloqueos_totales']
        mayor_nombre = jugador['nombre']

print(f'numero de bloqueos: {bloqueos_totales} - {mayor_nombre}')