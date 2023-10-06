import numpy as np
import random
from clases import *
from funciones import *
campo_jugador1 = Tablero_jugador_1()
campo_jugador2 = Tablero_jugador_2()
crear_barcos_jugador1(campo_jugador1)
crear_barcos_jugador2(campo_jugador2)

print(campo_jugador1.vidas_totales)
print(campo_jugador1.campo)

print("ZONA JUGADOR 2")
print("hola")

print(campo_jugador2.vidas_totales)
print(campo_jugador2.campo)


while campo_jugador1.vidas_totales > 0 or campo_jugador2.vidas_totales > 0 :

    posicion = 0
    print("INSTRUCCIONES DE COORDENADAS: iNTRODUCE EN FORMATO X,X.")
    coordenada = []
    primera = 0
    segunda = 0
    check = 1
    while check == 1:
        posicion = input("Introduce coordenada: ")
        coordenada = posicion.split(",")
        print(campo_jugador2.campo)
        if len(coordenada) == 2:
            if int(coordenada[0]) <= 9 or int(coordenada[1]) >= 0 and int(coordenada[1]) <= 9 or int(coordenada[0]) >= 0:
                primera = int(coordenada[0])
                segunda = int(coordenada[1])
                check = disparo(campo_jugador2,0,primera,segunda)
            else:
                print("POR FAVOR, INTRODUCE NUMEROS ENTRE 0 y 9")

        else:
            print("POR FAVOR, INTRODUCE NUMEROS EN FORMATO X,X")
    
        