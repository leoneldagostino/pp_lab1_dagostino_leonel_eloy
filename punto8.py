'''
Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo
'''
import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

for jugador in lista_datos:
    print('nombre : {} - % tiros de campo : {}'.format(jugador['nombre'],jugador['estadisticas']['porcentaje_tiros_de_campo']))

mayor_porcentaje_tiro = 0
for jugador in lista_datos:
    
    if jugador['estadisticas']['porcentaje_tiros_de_campo'] > mayor_porcentaje_tiro:
        mayor_porcentaje_tiro = jugador['estadisticas']['porcentaje_tiros_de_campo']
        mayor_nombre = jugador['nombre']

print(f'numero de porcentajes: {mayor_porcentaje_tiro} - {mayor_nombre}')


