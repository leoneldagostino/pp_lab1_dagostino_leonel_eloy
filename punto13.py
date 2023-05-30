'''
Calcular y mostrar el jugador con la mayor cantidad de robos totales
'''

import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

for jugador in lista_datos:
    print('nombre : {} - robos totales : {}'.format(jugador['nombre'],jugador['estadisticas']['robos_totales']))

robos_totales = 0
for jugador in lista_datos:
    
    if jugador['estadisticas']['robos_totales'] > robos_totales:
        robos_totales = jugador['estadisticas']['robos_totales']
        mayor_nombre = jugador['nombre']

print(f'numero de robos: {robos_totales} - {mayor_nombre}')