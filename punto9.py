'''
Calcular y mostrar el jugador con la mayor cantidad de asistencias totales
'''

import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

for jugador in lista_datos:
    print('nombre : {} - asistencias totales : {}'.format(jugador['nombre'],jugador['estadisticas']['asistencias_totales']))

asistencias_totales = 0
for jugador in lista_datos:
    
    if jugador['estadisticas']['asistencias_totales'] > asistencias_totales:
        asistencias_totales = jugador['estadisticas']['asistencias_totales']
        mayor_nombre = jugador['nombre']

print(f'numero de porcentajes: {asistencias_totales} - {mayor_nombre}')