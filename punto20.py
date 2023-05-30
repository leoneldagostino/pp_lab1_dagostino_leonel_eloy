'''
Permitir al usuario ingresar un valor y mostrar los jugadores , 
ordenados por posición en la cancha, 
que hayan tenido un porcentaje de tiros de campo superior a ese valor.
'''
import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]


valor = int(input("Ingrese un valor: "))
lista_nombre = []
for jugador in lista_datos:
    porcentaje_tiros_de_campo_jugador = jugador['estadisticas']['porcentaje_tiros_de_campo']
    nombre_jugador = jugador['nombre']
    if valor <= porcentaje_tiros_de_campo_jugador:
        lista_nombre.append(nombre_jugador)



diccionario_jugadores = {}


for nombre in lista_nombre:
    for nombre_jugador in lista_datos:
        if nombre == nombre_jugador['nombre']:
            if nombre_jugador['posicion'] in diccionario_jugadores:
                diccionario_jugadores[nombre_jugador['posicion']].append(nombre_jugador['nombre'])
            else:
                lista = []
                lista.append(nombre_jugador['nombre'])
                diccionario_jugadores[nombre_jugador['posicion']] = lista


for posicion in diccionario_jugadores:
    print(f'Los jugadores que superan de la {posicion} son: ')
    for jugador in diccionario_jugadores[posicion]:
        print(f'*{jugador}')
