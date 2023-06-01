def imprimir_opciones():
    print("1-Mostrar la lista de todos los jugadores del Dream Team. \n"
        "2-seleccionar un jugador por su índice y mostrar sus estadísticas completas \n"
        "3-Guardar en un archivo CSV las estadisticas de la opcion 2\n"
        "4-Buscar un jugador por su nombre e mostrar sus logros\n"
        "5-Mostrar el promedio de punto por partido de todo el Dream Team ordenando el nombre de forma ascendente\n"
        "6-Buscar por nombre de jugador y comprobar si es parte del salon de la fama\n"
        "7-Mostrar el jugador con la mayor cantidad de rebotes totales\n"
        "8-Mostrar el jugador con el mayor porcentaje de tiros de campo\n"
        "9-Mostrar el jugador con la mayor cantidad de asistencais totales\n"
        "10-Mostar los jugadores que promedian mayor a puntos por partido que el valor a ingresar\n"
        "11-Mostar los jugadores que promedian mayor a rebotes por partido que el valor a ingresar\n"
        "12-Mostar los jugadores que promedian mayor a asistencias por partido que el valor a ingresar\n"
        "13-Mostrar el jugador con la mayor cantidad de robos totales\n"
        "14-Mostrar el jugador con mayor cantidad de bloqueos totales\n"
        "15-Mostrar los jugadores que tengan mayor porcentaje de tiros libres que el valor a ingresar\n"
        "16-Mostrar el promedio de puntos por partido del equipo exceptuando el jugador con la menor cantidad de puntos por partido\n"
        "17-Mostrar el jugador con mayor cantidad de logros obtenidos\n"
        "18-Mostrar los jugadores que hayan tenido un porcentaje de tiros triples mayo que el valor a ingresar\n"
        "19-Mostrar el jugador con la mayor cantidad de temporadas jugadas\n"
        "20-Mostrar los jugadores ordenados por posicion que tengan un porcentaje de tiros de campo superior al valor a ingresar\n"
        "23-Guardar un archivo CSV en forma de ranking de Puntos, Rebotes, Asistencias, Robos\n")

import json
import re

with open("pp_lab1_dagostino_leonel_eloy/recursos/data.json","r") as data:
    datos = json.load(data)
    lista_datos = datos["jugadores"]
    
def mostrar_jugadores(lista:list):
    for jugador in lista:
        print(f'{jugador["nombre"]} - {jugador["posicion"]}')

def mostrar_jugador_por_indice(lista:list, indice:int, imprimir:bool = True) -> list:
    estadisticas_jugador = lista[indice - 1]['estadisticas']
    if imprimir:
        print(f'El jugador es: {lista[indice - 1]["nombre"]}')
        for estadistica,valor in estadisticas_jugador.items():
            print(f'{estadistica}: {valor}')
    
    return estadisticas_jugador

def buscar_nombre_por_indice(lista,indice):
    nombre = lista[indice - 1]['nombre']
    return nombre


def guardar_estadisticas_jugador(lista:list, indice):
    jugador_nombre = buscar_nombre_por_indice(lista,indice).replace(" ","_").lower()
    jugador = mostrar_jugador_por_indice(lista,indice,False)
    archivo_creado = False
    with open(f'Estadistica_{jugador_nombre}.csv','w') as archivo:
        contenido_archivo = ''
        for estadistica, valor in jugador.items():
            contenido_archivo += f'{estadistica} : {valor}\n'
        archivo.write(contenido_archivo)
        archivo_creado = True
    return archivo_creado
    
def buscar_jugador_por_nombre(lista:list ,nombre_buscar:str) -> list:
    for jugador in lista:
        if (re.search(nombre_buscar,jugador['nombre'].lower()) != None):
            print(jugador['nombre'])
            return jugador


def mostrar_logros(jugador):
    for logros in jugador['logros']:
        print(logros)

def ordenar_por_nombre(lista:list) -> list:
    lista_izq = []
    lista_der = []
    if(len(lista)<=1):
        return lista
    else:
        pivot = lista[0]
        for elemento in lista[1:]:
            if elemento > pivot:
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)
        
    lista_izq = ordenar_por_nombre(lista_izq)
    lista_izq.append(pivot)
    lista_der = ordenar_por_nombre(lista_der)
    lista_izq.extend(lista_der)

    return lista_izq

def formar_lista_nombre(lista:list):
    lista_nombre = []
    for nombre in lista:
        lista_nombre.append(nombre['nombre'])
    
    return lista_nombre

def mostrar_promedio_puntos_partido(lista:list,parametro:str):
    acumulado = 0
    for jugador in lista:
        acumulado += jugador['estadisticas'][parametro]

    cantidad_lista = len(lista)
    promedio = acumulado / cantidad_lista

    return promedio

def buscar_menor(lista:list,parametro:str):

    menor = lista[0]["estadisticas"][parametro]
    for elemento in lista:
        if elemento["estadisticas"][parametro] < menor:
            menor = elemento["estadisticas"][parametro]

    return menor

def promedio_menos_menor(lista:list,parametro:str):
    menor = buscar_menor(lista,parametro)
    promedio = mostrar_promedio_puntos_partido(lista,parametro)
    promedio_sin_menor = promedio - menor
    return promedio_sin_menor



            




def verificar_jugador_salon_de_la_fama(lista,nombre):
    jugador = buscar_jugador_por_nombre(lista,nombre)
    for logro in jugador['logros']:
        miembro = False
        if logro == 'Miembro del salon de la fama del baloncesto':
            miembro == True
    
    if miembro:
        print(f'Pertenece al salon de la fama ')
    else:
        print(f'No es parte del salon de la fama')


def mostar_mayor_estadistica(lista:list,parametro:str):
    mayor = lista[0]["estadisticas"][parametro]
    for elemento in lista:
        if elemento["estadisticas"][parametro] > mayor:
            mayor = elemento["estadisticas"][parametro]
            nombre_mayor = elemento["nombre"]
    
    print(f'El mayor en {parametro.replace("_"," ")} : {nombre_mayor} - {mayor}')
    return mayor

def buscar_superior_segun_valor(lista:list,parametro:str,valor:int):
    lista_superiores = []
    for elemento in lista:
        valor_superior = elemento["estadisticas"][parametro]
        nombre_superior = elemento["nombre"]
        if valor <= valor_superior:
            lista_superiores.append(nombre_superior)
    
    for superior in lista_superiores:
        print(superior)

    return lista_superiores

def ordenar_por_posicion(lista:list, lista_2:list):
    diccionario_ordenado = {}
    for elemento in lista:
        for elemento_2 in lista_2:
            if elemento == elemento_2['nombre']:
                if elemento_2['posicion'] in diccionario_ordenado:
                    diccionario_ordenado[elemento_2['posicion']].append(elemento_2['nombre'])
                else:
                    lista = []
                    lista.append(elemento_2['nombre'])
                    diccionario_ordenado[elemento_2['posicion']] = lista


        
def contador_mayor(lista:list,parametro:str):
    cantidad_maximo = 0
    for elemento in lista:
        if len(elemento[parametro]) > cantidad_maximo:
            cantidad_maximo = len(elemento[parametro])
            mayor_nombre = elemento['nombre']



    print(f"Numero de {parametro}: {cantidad_maximo} - {mayor_nombre}")

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


def guardar_csv_ranking_jugadores(datos:list,ranking:dict):
    with open('ranking.csv', 'w') as archivo:
        encabezado = datos
        texto = ""
        texto_encabezado = 'Jugador, ' 

        for orden in encabezado:
            texto_encabezado += f'{orden.replace("_"," ")}, '
        for jugador in ranking:
            texto += '\n' + jugador + ','
            for contenido in ranking[jugador]:
                texto += f'{contenido},'
        archivo.write(texto_encabezado)
        archivo.write(texto)

