#AQUI TENEMOS LAS FUNCIONES QUE COMPONEN NUESTRO JUEGO.
#Se centraran en crear barcos y disparar.

import numpy as np
import random
import time
import clases

def crear_barcos_jugador1(campo_jugador1):
    #Creamos las variables de claes Barco.
    #Orientacion es un numero aleatorio, las vidas del barco son introducidas mediante un int.
    #Aqui generamos numero aleatorio.
    orientacion = random.randint(1,4)
    #Aqui, generamos un barco con 1 vida.
    barco1= clases.Barco(1,orientacion)
    #Repetimos para todos los barcos.
    orientacion = random.randint(1,4)
    barco1_2= clases.Barco(1,orientacion)
    orientacion = random.randint(1,4)
    barco1_3= clases.Barco(1,orientacion)
    orientacion = random.randint(1,4)
    barco1_4= clases.Barco(1,orientacion)
    orientacion = random.randint(1,4)
    barco2_1 = clases.Barco(2,orientacion)
    orientacion = random.randint(1,4)
    barco2_2 = clases.Barco(2,orientacion)
    orientacion = random.randint(1,4)
    barco2_3 = clases.Barco(2,orientacion)
    orientacion = random.randint(1,4)
    barco3 = clases.Barco(3,orientacion)
    orientacion = random.randint(1,4)
    barco3_2 = clases.Barco(3,orientacion)
    orientacion = random.randint(1,4)
    barco4 = clases.Barco(4,orientacion)
    #Hora de meter coordenadas, para asegurarnos de que no se pisen.
    #Usaremos un bucle while que solo parara cuando se haya situado el barco.
    #Es decir, cuando la funcion insertar_barco devuelva 0.
    #IMPORTANTE: para optimizar la colocacion, primero metemos los barcos mas grandes.
    bucle =1
    while bucle==1:
        barco4.crear_coordenadas()
        #Ahora las metemos las coordenadas, si se encuentra una celda ocupada retornara 1.
        bucle = campo_jugador1.insertar_barco(barco4.coordenadas,barco4.vidas)
        #Creamos coordenadas, primero asegurandonos que no se salga del tablero.
    bucle =1
    #Asi para todos los barcos.
    while bucle==1:
        barco3.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco3.coordenadas,barco3.vidas)
    bucle =1
    while bucle==1:
        barco3_2.crear_coordenadas()
        bucle = campo_jugador1.insertar_barco(barco3_2.coordenadas,barco3_2.vidas)
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
    

    return "Jugador 1 Creado con exito."


def crear_barcos_jugador2(campo_jugador2):
    #Lo mismo que la funcion de crear barcos para jugador 1
    orientacion = random.randint(1,4)
    jugador_2_barco1 = clases.Barco(1,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco1_2= clases.Barco(1,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco1_3= clases.Barco(1,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco1_4= clases.Barco(1,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco2_1 = clases.Barco(2,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco2_2 = clases.Barco(2,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco2_3 = clases.Barco(2,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco3 = clases.Barco(3,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco3_2 = clases.Barco(3,orientacion)
    orientacion = random.randint(1,4)
    jugador_2_barco4 = clases.Barco(4,orientacion)

    bucle =1

    while bucle==1:
        jugador_2_barco4.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco4.coordenadas,jugador_2_barco4.vidas)

    bucle =1
    while bucle==1:
        jugador_2_barco3.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco3.coordenadas,jugador_2_barco3.vidas)
    bucle =1
    while bucle==1:
        jugador_2_barco3_2.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco3_2.coordenadas,jugador_2_barco3_2.vidas)

    bucle=1
    while bucle==1:
        jugador_2_barco1.crear_coordenadas()
        bucle = campo_jugador2.insertar_barco(jugador_2_barco1.coordenadas, jugador_2_barco1.vidas)
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

    return "Jugador 2 creado con exito."


def disparo(jugador, direccion, coord1,coord2,niebla):
    """
    La funcion recive los parametros la clase del jugador correspondiente.
    la direccion, sera 1 si dispara un jugador y 2 si es la IA.
    Ademas, se encargara de revisar el tablero.
    Primero se asegurara de que la zona a la que apuntamos sea valida
    es decir, que no sea X o _ (agua), si es valida, ejecuta el disparo y actualiza el tablero
    si no es valido, devuelve 1 debemos probar a introducir otras coordenadas."""
    if direccion == 1:
        #Comprobamos si se ha acertado en el tablero, cambiando la O por una X y quitando una vida al jugador.
        if jugador.campo[coord1,coord2] == "O":
            print("GOLPEEEEEEE! TIRA DE NUEVO")
            time.sleep(1)
            jugador.campo[coord1,coord2] = "X"
            niebla[coord1,coord2] = "X"
            print(niebla)
            #Comprobamos ademas si ya no quedan vidas, para terminar el juego antes de dar un turno extra.
            jugador.vidas_totales -=1
            if jugador.vidas_totales == 0:
                return 0
            else:
                return 1
        #Aqui comrpobamos si la zona es golpeada o agua.
        elif jugador.campo[coord1,coord2] == "X" or jugador.campo[coord1,coord2] == "_":
            print("Zona ya intentada/golpeada")
            time.sleep(1)
            return 1
        else:
            print("Agua, HAS FALLDO HAHAHAHAHAHAAHAAHAHAHHA")
            time.sleep(1)
            jugador.campo[coord1,coord2] = "_"
            niebla[coord1,coord2] = "_"
            return 0
        

    #Esta es la parte de la IA, uso sleep para que la ejecucion no sea tan rapida.
    #Mas que nada, que se note que es mas realista.
    if direccion == 2:
        print("Chatgpt esta pensando...")
        time.sleep(1)
        if jugador.campo[coord1,coord2] == "O":
            print("TOMAAAAA CHATGPT TE HA DADO, SUFRE!!!!!!")
            time.sleep(1)
            jugador.campo[coord1,coord2] = "X"
            niebla[coord1,coord2] = "X"
            jugador.vidas_totales -=1
            if jugador.vidas_totales == 0:
                return 0
            else:
                return 1
        elif jugador.campo[coord1,coord2] == "X" or jugador.campo[coord1,coord2] == "_":
            return 1
        else:
            print("Chatgpt ha fallado...")
            time.sleep(1)
            jugador.campo[coord1,coord2] = "_"
            niebla[coord1,coord2] = "_"
            return 0