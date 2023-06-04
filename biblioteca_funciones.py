import json
import re

def imprimir_opciones():
    """
    Imprime las opciones del menu por consola
    """

    print("1-Mostrar la lista de todos los jugadores del Dream Team. \n"
        "2-Seleccionar un jugador por su índice y mostrar sus estadísticas completas \n"
        "3-Guardar en un archivo CSV las estadisticas de la opcion 2\n"
        "4-Buscar un jugador por su nombre e mostrar sus logros\n"
        "5-Mostrar el promedio de punto por partido de todo el Dream Team ordenando el nombre de forma ascendente\n"
        "6-Buscar por nombre de jugador y comprobar si es parte del salon de la fama\n"
        "7-Mostrar el jugador con la mayor cantidad de rebotes totales\n"
        "8-Mostrar el jugador con el mayor porcentaje de tiros de campo\n"
        "9-Mostrar el jugador con la mayor cantidad de asistencias totales\n"
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
        "23-Guardar un archivo CSV en forma de ranking de Puntos, Rebotes, Asistencias, Robos\n"
        "0-Salir",end="\n\n")


def elegir_opcion():
    """
    Al llamar esta funcion va solicitar al usuario que ingrese la opcion que va seleccionar

    retornara como INT la opcion que selecciona
    """
    opcion = int(input("Ingrese la opcion que quiera elegir: "))
    
    return opcion


jugador_opcion_tres = None
def ejecutar_opcion(opcion:int,lista):
    """
    Recibira como parametro la opcion que selecciona el usuario y la lista de donde tomara los datos que ejucutara posteriormente

    devuelve segun que opcion elija
    """
    global jugador_opcion_tres
    if opcion == 1:

        print("Los jugadores son: ",end="\n")
        mostrar_jugadores_y_parametro(lista,"posicion")

    elif opcion == 2:

        indice = int(input("Indique el indice del jugador: "))
        jugador_opcion_tres = indice
        mostrar_jugador_por_indice(lista,indice)

    elif opcion == 3:

        if jugador_opcion_tres is not None:
            if guardar_estadisticas_jugador(lista,jugador_opcion_tres):
                print("El archivo se creo con exito")
            else:
                print("Ocurrio un error al crear al archivo")
        else:
            print("Debe elegir un jugador primero, selecciona la opcion 2")

    elif opcion == 4:

        nombre = input("Que jugador esta buscando: ")
        mostrar_logros(buscar_jugador_por_nombre(lista,nombre))

    elif opcion == 5:

        lista_ordenada_puntos = ordenar_por_parametro(lista,"promedio_puntos_por_partido")
        lista_ordenada_nombres_puntos = ordenar_por_nombre(lista_ordenada_puntos)
        mostrar_jugadores_y_parametro(lista_ordenada_nombres_puntos,"promedio_puntos_por_partido",True)

    elif opcion == 6:

        nombre = input("Indique el jugador que busca: ")
        verificar_jugador_salon_de_la_fama(lista,nombre)

    elif opcion == 7:

        mostar_mayor_estadistica(lista,"rebotes_totales")

    elif opcion == 8:

        mostar_mayor_estadistica(lista,"porcentaje_tiros_de_campo")

    elif opcion == 9:

        mostar_mayor_estadistica(lista,"asistencias_totales")

    elif opcion == 10:
        valor = int(input("Ingrese el valor a superar: "))
        lista_superan = buscar_superior_segun_valor(lista,"promedio_puntos_por_partido",valor)
        print("Los jugadores que superan el valor ingresado son: ")
        for jugador in lista_superan:
            print(f'-{jugador}')

    elif opcion == 11:

        valor = int(input("Ingrese el valor a superar: "))
        lista_superan = buscar_superior_segun_valor(lista,"promedio_rebotes_por_partido",valor)
        print("Los jugadores que superan el valor ingresado son: ")
        for jugador in lista_superan:
            print(f'-{jugador}')

    elif opcion == 12:

        valor = int(input("Ingrese el valor a superar: "))
        lista_superan =  buscar_superior_segun_valor(lista,"promedio_asistencias_por_partido",valor)
        print("Los jugadores que superan el valor ingresado son: ")
        for jugador in lista_superan:
            print(f'-{jugador}')

    elif opcion == 13:

        mostar_mayor_estadistica(lista,"robos_totales")

    elif opcion == 14:

        mostar_mayor_estadistica(lista,"bloqueos_totales")

    elif opcion == 15:

        valor = int(input("Ingrese el valor a superar: "))
        lista_superan = buscar_superior_segun_valor(lista,"porcentaje_tiros_libres",valor)
        print("Los jugadores que superan el valor ingresado son: ")
        for jugador in lista_superan:
            print(f'-{jugador}')

    elif opcion == 16:

        promedio = promedio_menos_menor(lista,"promedio_puntos_por_partido")
        print(f'El promedio excepetuando el ultimo es {promedio:.2f}')

    elif opcion == 17:

        contador_mayor(lista,"logros")

    elif opcion == 18:

        valor = int(input("Ingrese el valor a superar: "))
        lista_superan = buscar_superior_segun_valor(lista,"porcentaje_tiros_triples",valor)
        print("Los jugadores que superan el valor ingresado son: ")
        for jugador in lista_superan:
            print(f'-{jugador}')

    elif opcion == 19:

        mostar_mayor_estadistica(lista,"temporadas")
    elif opcion == 20:

        valor = int(input("Ingrese el valor a superar: "))
        ordenar_por_posicion(buscar_superior_segun_valor(lista,"porcentaje_tiros_de_campo",valor),lista)

    elif opcion == 23:

        stats = ["puntos_totales","rebotes_totales","asistencias_totales","robos_totales"]
        archivo_csv = guardar_csv_ranking_jugadores(stats,ranking(lista,stats))
        if archivo_csv:
            print("El archivo csv se ha guardado correctamente")
        else:
            print("El archivo no pudo crearse.")
    
    print("\n")
    

def leer_archivo(ruta:str,datos_buscar:str) -> list:
    """
    Funcion que lee el archivo csv y devuelve una lista con los datos buscados.
    parametro:ruta -> recibe la ruta donde se encuentra el set de datos
    parametro:datos_buscar -> recibe los datos que se buscan en el set de datos

    retornara una lista de los datos
    """
    with open(ruta,"r") as data:
        datos = json.load(data)
        lista_datos = datos[datos_buscar]
    
    return lista_datos
    

def mostrar_jugadores_y_parametro(lista:list,parametro:str,estadistica = False):
    """
    Funcion que muestra los jugadores y su respectivo parametro.
    parametro:lista -> recibe la lista donde se encuentra los datos
    parametro:parametro -> recibe el dato que se quiere mostrar
    parametro:estadistica -> si cambia a true buscara el parametro dentro de su apartado de estadisticas
    
    imprime por pantalla los datos deseados
    """
    if estadistica != True: 
        for jugador in lista:
            print(f'{jugador["nombre"]} - {jugador[parametro]}')
    else:
        for jugador in lista:
            print(f'{jugador["nombre"]} - {jugador["estadisticas"][parametro]}')

def mostrar_jugador_por_indice(lista:list, indice:int, imprimir= True) -> list:
    """
    Funcion que muestra el jugador por indice.
    parametro:lista -> recibe la lista donde se encuentra los datos
    parametro:indice -> recibe el indice que se buscara

    parametro:imprimir -> si cambia a false no los imprimira por consola

    retornara una lista con las estadisticas del jugador
    """
    estadisticas_jugador = lista[indice - 1]['estadisticas']
    if imprimir:
        print(f'El jugador es: {lista[indice - 1]["nombre"]}')
        for estadistica,valor in estadisticas_jugador.items():
            print(f'{estadistica.replace("_"," ")}: {valor}')
    
    return estadisticas_jugador


def buscar_nombre_por_indice(lista,indice):
    """
    Funcion que busca el nombre del jugador por indice
    parametro:lista -> recibe la lista donde se encuentra los datos de los jugadores
    parametro:indice -> recibe el indice que se buscara

    retornara el nombre segun el indice
    """
    nombre = lista[indice - 1]['nombre']
    return nombre


def guardar_estadisticas_jugador(lista:list, indice):
    """
    Funcion que guarda las estadisticas del jugador por indice
    parametro:lista -> recibira la lista donde se encuentra los datos de los jugadores
    parametro:indice -> recibe el indice que se buscara 

    retornara en valor booleano si fue creado el archivo o no
    """
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
    """
    Funcion que busca el jugador por nombre
    parametro:lista -> recibe la lista donde se encuentra los datos de los jugadores
    parametro:nombre_buscar -> recibe el nombre del jugador a buscar

    al final imprimira el jugador en caso de ser encontrado
    """
    for jugador in lista:
        if (re.search(nombre_buscar,jugador['nombre'].lower()) != None):
            print(jugador['nombre'])
            return jugador
        else:
            print("El jugador no fue encontrado")


def mostrar_logros(jugador):
    """
    Funcion que muestra los logros del jugador por consola
    parametro:jugador -> recibe el jugador 

    imprimira los logros del jugador por consola
    """
    for logros in jugador['logros']:
        print(logros)


def ordenar_por_nombre(lista:list) -> list:
    """
    Funcion que ordena la lista por nombre
    parametro:lista -> recibe la lista donde se encuentra los datos

    retornara la lista ordenada
    """
    lista_izq = []
    lista_der = []
    if(len(lista)<=1):
        return lista
    else:
        pivot = lista[0]
        for elemento in lista[1:]:
            if elemento["nombre"] > pivot["nombre"]:
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)
        
    lista_izq = ordenar_por_nombre(lista_izq)
    lista_izq.append(pivot)
    lista_der = ordenar_por_nombre(lista_der)
    lista_izq.extend(lista_der)

    return lista_izq


def mostrar_promedio(lista:list,parametro:str):
    """
    Funcion que muestra el promedio de un parametro
    parametro:lista -> recibe la lista donde se encuentra los datos
    parametro:parametro -> dato que se busca

    retornara el promedio
    """
    acumulado = 0
    for jugador in lista:
        acumulado += jugador['estadisticas'][parametro]

    cantidad_lista = len(lista)
    promedio = acumulado / cantidad_lista

    return promedio


def buscar_menor(lista:list,parametro:str):
    """
    Funcion que busca el jugador con el menor valor de un parametro
    parametro:lista -> recibe la lista donde sencuentra los datos 
    parametro:parametro -> dato que se busca

    retornara el jugador con el menor valor en el parametro dado
    """
    menor = lista[0]["estadisticas"][parametro]
    for elemento in lista:
        if elemento["estadisticas"][parametro] < menor:
            menor = elemento["estadisticas"][parametro]

    return menor


def promedio_menos_menor(lista:list,parametro:str):
    """
    Funcion que calcula el promedio de un parametro menos el menor valor
    parametro:lista -> recibe la lista donde se encuentra los datos 
    parametro:parametro -> recibe el dato que se quiere calcular el promedio

    retornara el promedio final
    """
    menor = buscar_menor(lista,parametro)
    promedio = mostrar_promedio(lista,parametro)
    promedio_sin_menor = promedio - menor
    return promedio_sin_menor


def verificar_jugador_salon_de_la_fama(lista,nombre):
    """
    Funcion que verifica si un jugador esta en salon de la fama
    parametro:lista -> recibe la lista donde se encuentra los datos de los jugadores
    parametro:nombre -> es el nombre el cual se busca dentro de la lista

    al final imprimira si es o no parte del salon de la fama
    """
    jugador = buscar_jugador_por_nombre(lista,nombre)
    miembro = False
    for logro in jugador['logros']:
        if logro == 'Miembro del Salon de la Fama del Baloncesto':
            miembro = True
    
    if miembro:
        print(f'Pertenece al salon de la fama ')
    else:
        print(f'No es parte del salon de la fama')


def mostar_mayor_estadistica(lista:list,parametro:str):
    """
    funcion que muestra el jugador con mayor estadistica segun el parametro especificado
    parametro:lista -> recibe la lista donde se encuentra los datos del jugador 
    parametro:parametro -> dato que se desea buscar

    retornara el jugador mayor en el dato buscado y lo imprimira 
    """
    mayor = lista[0]["estadisticas"][parametro]
    for elemento in lista:
        if elemento["estadisticas"][parametro] > mayor:
            mayor = elemento["estadisticas"][parametro]
            nombre_mayor = elemento["nombre"]
    
    print(f'El jugador con mayor {parametro.replace("_"," ")} : {nombre_mayor} - {mayor}')
    return mayor


def buscar_superior_segun_valor(lista:list,parametro:str,valor:int):
    """
    funcion que busca el jugador con un valor superior al valor especificado
    parametro:lista -> recibe la lista donde se encuentra los datos de los jugadores
    parametro:parametro -> dato que se desea buscar
    parametro:valor -> valor que se busca superar

    retornara una lista de aquellos que superan el valor segun el parametro
    """
    lista_superiores = []
    for elemento in lista:
        valor_superior = elemento["estadisticas"][parametro]
        nombre_superior = elemento["nombre"]
        if valor <= valor_superior:
            lista_superiores.append(nombre_superior)
    
    
    return lista_superiores


def ordenar_por_posicion(lista:list, lista_2:list):
    """
    funcion que ordena la lista segun la posicion de los jugadores
    parametro:lista -> recibe la lista donde se encuentra los datos de los jugadores
    parametro:lista_2 -> recibe la lista que hara comparacion con el primer parametro lista

    al final imprimira los jugadores segun su posicion
    """
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
    
    for posicion in diccionario_ordenado:
        print(f'Los jugadores en la posicion {posicion} son: ')
        for jugador in diccionario_ordenado[posicion]:
            print(f'*{jugador}')


def contador_mayor(lista:list,parametro:str):
    """
    Funcion que buscara el mayor del parametro dado
    parametro:lista -> recibe la lista donde se encuentra los datos de los jugadores
    parametro:parametro -> el dato que realizara la busqueda

    al final mostrara el nombre con su cantidad y que dato se busco
    """
    cantidad_maximo = 0
    for elemento in lista:
        if len(elemento[parametro]) > cantidad_maximo:
            cantidad_maximo = len(elemento[parametro])
            mayor_nombre = elemento['nombre']



    print(f"Numero de {parametro}: {cantidad_maximo} - {mayor_nombre}")


def ordenar_por_parametro(lista:list,parametro:str,orden:bool = True):
    """
    Funcion que ordenara la lista segun el parametro dado
    parametro:lista -> recibe la lista de donde se encuentra los datos
    parametro:parametro -> dato del cual tendra en cuenta para ordenar
    parametro:orden -> en caso de ser false ordenara de forma ascendente o descendente

    retornara la lista ordenada
    """

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
    """
    Funcion que ordenara la lista en ranking segun el parametro dado
    parametro:lista_jugadores -> recibe la lista de jugadores y sus datos para armar el ranking
    parametro:estadisticas -> recibe una lista de las estadisticas a tener en cuenta segun su ranking

    retornara en una lista el ranking de los jugadores
    """

    ranking_jugadores = {}
    puesto_ranking = 0
    lista_estadistica = estadistica
    for estadistica in lista_estadistica:
        lista = ordenar_por_parametro(lista_jugadores,estadistica,False)
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
    """
    Funcion que tomara los datos y el ranking guardandolo en un archivo csv
    parametro:datos -> recibe una lista de los datos para armar el archivo
    parametro:ranking -> tomara un diccionario del cual los usara los datos para guardar el archivo

    retornara true o false segun si se realizo el archivo o no
    """
    
    archivo_creado = False
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
        archivo_creado = True

    return archivo_creado


#punto extra 1

def contador_jugador_posicion_basquet(lista:list):
    """
    Funcion que tomara una lista de jugadores y los contara por posicion de basquet
    parametro:lista -> recibe una lista de los jugadores

    imprimira el numero de jugadores en cada posicion
    """

    lista_contador_posiciones = {
        "base":0,
        "escolta":0,
        "alero":0,
        "ala-pivot":0,
        "pivot":0
    }
    for jugador in lista:
        if jugador['posicion'].lower() == "base":
            lista_contador_posiciones["base"] += 1
        elif jugador['posicion'].lower() == "escolta":
            lista_contador_posiciones["escolta"] += 1
        elif jugador['posicion'].lower() == "alero":
            lista_contador_posiciones["alero"] += 1
        elif jugador['posicion'].lower() == "ala-pivot":
            lista_contador_posiciones["ala-pivot"] += 1
        elif jugador['posicion'].lower() == "pivot":
            lista_contador_posiciones["pivot"] += 1
    
    for posicion, valor in lista_contador_posiciones.items():
        print(f'{posicion}: {valor}')
        
# punto extra 2
def ordenar_jugadores_por_all_star(lista:dict):
    """
    Funcion que ordenara los jugadores por el numero de all star
    parametro:lista -> recibe una lista de los jugadores

    retornara la lista de los jugadores ordenados
    """

    nueva_lista = list(lista.items())
    rango_a = len(nueva_lista) 
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a -=1
        
        for indice_A in range(rango_a):
            if  nueva_lista[indice_A][1] > nueva_lista[indice_A+1][1]:
                nueva_lista[indice_A], nueva_lista[indice_A+1] = nueva_lista[indice_A+1], nueva_lista[indice_A]
                flag_swap = True
                
    lista_definitiva_jugadores = {}
    for jugador in nueva_lista:
        lista_definitiva_jugadores[jugador[0]] = jugador[1]
    return lista_definitiva_jugadores


def jugador_veces_all_star(lista:list):
    """
    Funcion que retornara el numero de veces que un jugador ha sido all star
    parametro:lista -> recibe una lista de los jugadores

    retornara un diccionario con los jugadores y sus numero de veces de all-star
    """
    jugador_all_star = {}
    for jugador in lista:
        for logro in jugador["logros"]:
            coincidencia = re.search(r'(\d+) veces All-Star',logro)  
            if coincidencia != None:
                jugador_all_star[jugador['nombre']] = coincidencia.string
    ordenar_jugadores_por_all_star(jugador_all_star)

    return jugador_all_star


def mostrar_jugador_orden_all_star(jugadores:dict):
    """
    Funcion que mostrará los jugadores ordenados por el numero de all star
    parametro:jugadores -> recibe un diccionario de los jugadores

    imprimira los jugadores y su cantidad de veces all-star
    """

    for nombre, cantidad_all_star in jugadores.items():
        print(f'{nombre} ({cantidad_all_star} veces All-star)')



