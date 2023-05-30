'''
Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido
'''
import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

promedio_menor = lista_datos[0]['estadisticas']['promedio_puntos_por_partido']
jugador_nombre_menor_promedio = ""

for jugador in lista_datos:
    if jugador['estadisticas']['promedio_puntos_por_partido'] < promedio_menor:
        promedio_menor = jugador['estadisticas']['promedio_puntos_por_partido']
        jugador_nombre_menor_promedio = jugador['nombre']

print(f'El jugador con menor promedio por partido es {jugador_nombre_menor_promedio} con {promedio_menor}')

cantidad_jugadores = len(lista_datos) - 1
total_promedios_puntos_partido = 0

for jugador in lista_datos:
    total_promedios_puntos_partido += jugador['estadisticas']['promedio_puntos_por_partido']

print(total_promedios_puntos_partido)
total_promedios_puntos_partido -= promedio_menor
promedio_puntos_partido = total_promedios_puntos_partido / cantidad_jugadores

print(f'El promedio de puntos sin contar el ultimo {promedio_puntos_partido}')


    