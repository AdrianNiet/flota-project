#       ----------------------------------------------------------------------------
#           HUNDIR LA FLOTA. TRABAJO REALIZADO POR ADRIAN NIETO.
#           EN ESTE ARCHIVO MAIN PY TENGO LAS LLAMADAS A LAS FUNCIONES Y EL BUCLE
#           QUE MANTIENE FUNCIONANDO EL JUEGO.
#           BAJA ABAJO PARA VER LO RELACIANDO EN LOS RESPECTIVOS COMENTARIOS.

#Importamos todas las funciones que necesitamos.
import numpy as np
import random
#Solo funcionan si se importan otros py de la siguiente manera.
from clases import *
from funciones import *
from variables import *
import time

#Creamos los barcos para cada jugador, para seguir el flujo, ve a la funcion crear_barcos.
crear_barcos_jugador(campo_jugador1,barco1_1)
crear_barcos_jugador(campo_jugador1,barco1_2)
crear_barcos_jugador(campo_jugador1,barco1_3)
crear_barcos_jugador(campo_jugador1,barco1_4)
crear_barcos_jugador(campo_jugador1,barco2_1)
crear_barcos_jugador(campo_jugador1,barco2_2)
crear_barcos_jugador(campo_jugador1,barco2_3)
crear_barcos_jugador(campo_jugador1,barco3_1)
crear_barcos_jugador(campo_jugador1,barco3_2)
crear_barcos_jugador(campo_jugador1,barco4)

#Ahora los basrcos para jugador 2.

crear_barcos_jugador(campo_jugador2,barco1_1)
crear_barcos_jugador(campo_jugador2,barco1_2)
crear_barcos_jugador(campo_jugador2,barco1_3)
crear_barcos_jugador(campo_jugador2,barco1_4)
crear_barcos_jugador(campo_jugador2,barco2_1)
crear_barcos_jugador(campo_jugador2,barco2_2)
crear_barcos_jugador(campo_jugador2,barco2_3)
crear_barcos_jugador(campo_jugador2,barco3_1)
crear_barcos_jugador(campo_jugador2,barco3_2)
crear_barcos_jugador(campo_jugador2,barco4)

#creamos la niebla de guerra.
modo_juego = 4

while not(modo_juego == 1 or modo_juego == 2 or modo_juego == 0):
    try:
        print("Para jugar contra CHATGPT pulse 1.\n",
              "Para jugar contra otra persona, pulse 2.\n"
              "Para salir sin jugar pulse 0.")
        modo_juego = int(input("----->    "))
    except:
        print("SOLO NUMEROS POR FAVOR.")

if modo_juego != 0:
    #Si en tal caso, el usuario no quiere jugar, salimos sin crear el juego.
    juego = clases.Juego(modo_juego)
    #Esto lo pongo para que parezca que se toma su tiempo, y no ponga toda la informacion tan de golpe.
    print("Matando cucarachas...")
    time.sleep(1)
    print("Ensuciando cubiertas para limpiarlas luego...")
    time.sleep(1)
    print("Despertando al leviathan...")
    time.sleep(1)
    print("Finalizando registro de sirenas...")
    time.sleep(1)
    print("finalizado creacion de barcos, comenzando juego...")
    time.sleep(1)
    juego.jugando(campo_jugador1,campo_jugador2,niebla)
#para debugging, descomentar para ver tu propio tablero.
#Se vera igualmente si juegas contra la IA, pero no si juegas contra otra persona.
#print(campo_jugador1.vidas_totales)
#print(campo_jugador1.campo)
#print(campo_jugador2.vidas_totales)
#print(campo_jugador2.campo)