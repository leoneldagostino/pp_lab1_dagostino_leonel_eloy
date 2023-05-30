'''
Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
'''

import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

for jugador in lista_datos:
    print('nombre : {} - logros: {}'.format(jugador['nombre'],jugador['logros']))
    print(len(jugador['logros']))


cantidad_logros_maximo = 0
for jugador in lista_datos:

    if len(jugador['logros']) > cantidad_logros_maximo:
        cantidad_logros_maximo = len(jugador['logros'])
        mayor_nombre = jugador['nombre']

print(f'numero de logros: {cantidad_logros_maximo} - {mayor_nombre}')