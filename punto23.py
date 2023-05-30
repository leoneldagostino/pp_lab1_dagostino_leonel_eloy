'''
Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking
Puntos 
Rebotes 
Asistencias 
Robos
'''

import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]


def ordenar_por_parametro(lista:list,parametro:str,orden:bool = True):

    rango_a = len(lista) 
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a -=1
        if orden:
                for indice_A in range(rango_a):
                    if  lista[indice_A]["estadisticas"][parametro] >  lista[indice_A+1]["estadisticas"][parametro]:
                        lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                        flag_swap = True
        else:
            for indice_A in range(rango_a):
                if  lista[indice_A]["estadisticas"][parametro]  <  lista[indice_A+1]["estadisticas"][parametro] :
                    lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                    flag_swap = True 
    return lista

# def ordenar_lista(lista:list,parametro:str,ordenado:bool = True) -> list:
#     lista_izq = []
#     lista_der = []
#     if ordenado == True:
#         if(len(lista)<=1):
#             return lista
#         else:
#             pivot = lista[0]
#             for elemento in lista[1:]:
#                 if elemento[parametro] > pivot[parametro]:
#                     lista_der.append(elemento)
#                 else:
#                     lista_izq.append(elemento)
            
#         lista_izq = ordenar_lista(lista_izq,parametro)
#         lista_izq.append(pivot)
#         lista_der = ordenar_lista(lista_der,parametro)
#         lista_izq.extend(lista_der)

#         return lista_izq
#     else:
#         return lista
    

def ranking(lista_jugadores:list,estadistica:list):
    ranking_jugadores = {}
    puesto_ranking = 0
    lista_estadistica = estadistica
    for estadistica in lista_estadistica:
        lista = ordenar_por_parametro(lista_datos,estadistica,False)
        for jugador_nombre in lista_jugadores:
            puesto_ranking = 0
            for jugador in lista:
                puesto_ranking += 1
                if jugador['nombre'] == jugador_nombre['nombre']:
                    texto = f"Ranking n˚ {puesto_ranking}"
                    if jugador['nombre'] in ranking_jugadores:
                        ranking_jugadores[jugador['nombre']].append(texto)
                    else:
                        lista_aux = []
                        lista_aux.append(texto)
                        ranking_jugadores[jugador['nombre']] = lista_aux
                    break

    return ranking_jugadores


stats = ['puntos_totales','asistencias_totales','rebotes_totales','robos_totales']
jugadores_ranking = ranking(lista_datos,stats)

with open('ranking.csv','w') as archivo:
    encabezado = stats
    texto = ""
    texto_encabezado = 'Jugador,'
    
    for orden in encabezado:
        texto_encabezado += f'{orden.replace("_"," ")}, '
    for jugador in jugadores_ranking:
        texto += '\n' + jugador + ','
        for contenido in jugadores_ranking[jugador]:
            texto += f'{contenido},'
    archivo.write(texto_encabezado)
    archivo.write(texto)