from biblioteca_funciones import *
print("Iniciando programa...",end="\n\n")


while True:
    imprimir_opciones()
    opcion = elegir_opcion()
    if opcion != 0:
        ejecutar_opcion(opcion,leer_archivo("recursos/data.json","jugadores"))
    else:
        break

print("Fin del programa")
