'''
Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.
'''
import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]


valor = int(input("Ingrese un valor: "))
lista_nombre = []

for jugador in lista_datos:
    porcentaje_tiros_triples_jugador = jugador['estadisticas']['porcentaje_tiros_triples']
    nombre_jugador = jugador['nombre']
    if valor <= porcentaje_tiros_triples_jugador:
        lista_nombre.append(nombre_jugador)

for nombre_jugador_lista in lista_nombre:
    print(nombre_jugador_lista)