'''
Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto
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
        miembro = False
        for logro in jugador["logros"]:
            if logro == "Miembro del Salon de la Fama del Baloncesto":
                miembro = True

if miembro == True:
    print(f'{nombre_buscar} Pertenece al salon de la fama')
else:
    print(f'{nombre_buscar} No es parte del salon de la fama')