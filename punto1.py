#Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
#Nombre Jugador - Posición. Ejemplo:
#Michael Jordan - Escolta

import json

with open("pp_lab1_dagostino_leonel_eloy/recursos/data.json","r") as data:
    datos = json.load(data)
    lista_datos = datos["jugadores"]

#print(lista_datos)
for jugadores in lista_datos:
    print('{0} - {1} '.format(jugadores["nombre"],jugadores["posicion"]))