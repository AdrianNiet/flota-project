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
import time

#Creamos los 2 jugadores, jugador 1 es siempre persona, jugador 2 sera IA o persona.
#Para seguir flujo de codigo, ve a clases.py a las clases de jugador
campo_jugador1 = Tablero_jugador_1()
campo_jugador2 = Tablero_jugador_2()
#Creamos los barcos para cada jugador, para seguir el flujo, ve a la funcion crear_barcos
crear_barcos_jugador1(campo_jugador1)
crear_barcos_jugador2(campo_jugador2)
#creamos la niebla de guerra
niebla = Niebla_de_guerra
modo_juego = 0
while modo_juego != 1 and modo_juego != 2:
    try:
        modo_juego = int(input("Selecciona 1 para jugar contra la IA, 2 para jugar 1vs1:   "))
    except:
        print("SOLO NUMEROS POR FAVOR.")
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

juego = Juego(modo_juego)
juego.jugando(campo_jugador1,campo_jugador2,niebla)
#para debugging, descomentar para ver tu propio tablero.
#Se vera igualmente si juegas contra la IA, pero no si juegas contra otra persona.
#print(campo_jugador1.vidas_totales)
#print(campo_jugador1.campo)
#print(campo_jugador2.vidas_totales)
#print(campo_jugador2.campo)


