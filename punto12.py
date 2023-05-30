'''
Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.
'''
import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]


valor = int(input("Ingrese un valor: "))
lista_nombre = []

for jugador in lista_datos:
    promedio_asistencia_partido_jugador = jugador['estadisticas']['promedio_asistencias_por_partido']
    nombre_jugador = jugador['nombre']
    if valor <= promedio_asistencia_partido_jugador:
        lista_nombre.append(nombre_jugador)

for nombre_jugador_lista in lista_nombre:
    print(nombre_jugador_lista)
