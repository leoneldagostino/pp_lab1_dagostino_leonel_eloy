'''
Permitir al usuario buscar un jugador por su nombre y mostrar sus logros,
 como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
'''
import json
import re

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]

nombre_buscar = input("Indique el nombre del jugador que busca: ")

for jugador in lista_datos:
    if(re.search(nombre_buscar,jugador["nombre"])!= None):
        print(jugador["nombre"])
        for logros in jugador["logros"]:
            print(logros)
