import numpy as np
import random
from clases import *

def crear_barcos_jugador1(campo_jugador1):
    
    orientacion = random.randint(1,4)
    barco1= Barco(1,orientacion)
    orientacion = random.randint(1,4)
    barco1_2= Barco(1,orientacion)
    orientacion = random.randint(1,4)
    barco1_3= Barco(1,orientacion)
    orientacion = random.randint(1,4)
    barco1_4= Barco(1,orientacion)
    orientacion = random.randint(1,4)
    barco2_1 = Barco(2,orientacion)
    orientacion = random.randint(1,4)
    barco2_2 = Barco(2,orientacion)
    orientacion = random.randint(1,4)
    barco2_3 = Barco(2,orientacion)
    orientacion = random.randint(1,4)
    barco3 = Barco(3,orientacion)
    orientacion = random.randint(1,4)
    barco3_2 = Barco(3,orientacion)
    orientacion = random.randint(1,4)
    barco4 = Barco(4,orientacion)

    bucle =1
    while bucle==1:

        barco1.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco1.coordenadas, barco1.vidas)

    bucle =1
    while bucle==1:
        barco1_2.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco1_2.coordenadas, barco1_2.vidas)
    bucle =1
    while bucle==1:
        barco1_3.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco1_3.coordenadas, barco1_3.vidas)
    bucle =1
    while bucle==1:
        barco1_4.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco1_4.coordenadas, barco1_4.vidas)
    bucle =1
    while bucle==1:
        barco2_1.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco2_1.coordenadas,barco2_1.vidas)
    bucle =1
    while bucle==1:
        barco2_2.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco2_2.coordenadas,barco2_2.vidas)
    bucle =1
    while bucle==1:
        barco2_3.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco2_3.coordenadas,barco2_3.vidas)
    bucle =1
    while bucle==1:
        barco3.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco3.coordenadas,barco3.vidas)
    bucle =1
    while bucle==1:
        barco3_2.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco3_2.coordenadas,barco3_2.vidas)
    bucle =1
    while bucle==1:
        barco4.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco4.coordenadas,barco4.vidas)

    return "Jugador 1 Creado con exito."


def crear_barcos_jugador2(campo_jugador2):
    orientacion = random.randint(1,4)
    jugador_2_barco1 = Barco(1,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco1_2= Barco(1,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco1_3= Barco(1,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco1_4= Barco(1,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco2_1 = Barco(2,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco2_2 = Barco(2,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco2_3 = Barco(2,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco3 = Barco(3,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco3_2 = Barco(3,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco4 = Barco(4,orientacion)

    bucle =1
    while bucle==1:

        jugador_2_barco1.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco1.coordenadas, jugador_2_barco1.vidas)

    bucle =1
    while bucle==1:
        jugador_2_barco1_2.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco1_2.coordenadas, jugador_2_barco1_2.vidas)
    bucle =1
    while bucle==1:
        jugador_2_barco1_3.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco1_3.coordenadas, jugador_2_barco1_3.vidas)
    bucle =1
    while bucle==1:
        jugador_2_barco1_4.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco1_4.coordenadas, jugador_2_barco1_4.vidas)
    bucle =1
    while bucle==1:
        jugador_2_barco2_1.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco2_1.coordenadas,jugador_2_barco2_1.vidas)
    bucle =1
    while bucle==1:
        jugador_2_barco2_2.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco2_2.coordenadas,jugador_2_barco2_2.vidas)
    bucle =1
    while bucle==1:
        jugador_2_barco2_3.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco2_3.coordenadas,jugador_2_barco2_3.vidas)
    bucle =1
    while bucle==1:
        jugador_2_barco3.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco3.coordenadas,jugador_2_barco3.vidas)
    bucle =1
    while bucle==1:
        jugador_2_barco3_2.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco3_2.coordenadas,jugador_2_barco3_2.vidas)
    bucle =1
    while bucle==1:
        jugador_2_barco4.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco4.coordenadas,jugador_2_barco4.vidas)

    return "Jugador 2 creado con exito."