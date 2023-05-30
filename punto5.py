'''
Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team,
ordenado por nombre de manera ascendente. 

'''
import json

with open('pp_lab1_dagostino_leonel_eloy/recursos/data.json','r') as data:
    
    datos = json.load(data)
    lista_datos = datos["jugadores"]


#armamos la lista de nombre
lista_nombres = []
for nombre in lista_datos:
    lista_nombres.append(nombre['nombre'])

#armamos la funcion para ordenar los nombres
def ordenar_lista(lista:list) -> list:
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
        
    lista_izq = ordenar_lista(lista_izq)
    lista_izq.append(pivot)
    lista_der = ordenar_lista(lista_der)
    lista_izq.extend(lista_der)

    return lista_izq

lista_ordenada = ordenar_lista(lista_nombres)
#print(lista_nombres)
#print(lista_ordenada)

#sumamos 


acumulador = 0
for jugador in lista_datos:
    acumulador += jugador['estadisticas']['promedio_puntos_por_partido']

print(acumulador)

#calculamos el promedio

cantidad = len(lista_datos)
promedio = acumulador / cantidad

print(promedio)
print(f'El promedio de puntos por partido es de {promedio}')