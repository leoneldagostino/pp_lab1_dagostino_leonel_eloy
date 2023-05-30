'''
Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
'''
import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]



for jugador in lista_datos:
    print('nombre : {} - rebotes : {}'.format(jugador['nombre'],jugador['estadisticas']['rebotes_totales']))

mayor_rebote = 0
for jugador in lista_datos:
    
    if jugador['estadisticas']['rebotes_totales'] > mayor_rebote:
        mayor_rebote = jugador['estadisticas']['rebotes_totales']
        mayor_nombre = jugador['nombre']

print(f'numero de rebotes: {mayor_rebote} - {mayor_nombre}')
    
