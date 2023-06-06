from biblioteca_funciones import *
print("Iniciando programa...",end="\n\n")


while True:
    imprimir_opciones()
    opcion = elegir_opcion()
    if opcion != -1:
        if opcion == 0:
            imprimir_mas_opciones()
            opcion = elegir_opcion()    
            ejecutar_opciones_extra(opcion,leer_archivo("recursos/data.json","jugadores"))
        else:
            ejecutar_opcion(opcion,leer_archivo("recursos/data.json","jugadores"))
        
    else:
        break

print("Fin del programa")
