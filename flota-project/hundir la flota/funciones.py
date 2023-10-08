#AQUI TENEMOS LAS FUNCIONES QUE COMPONEN NUESTRO JUEGO.
#Se centraran en crear barcos y disparar.

import numpy as np
import random
import time
import clases

def crear_barcos_jugador(campo_jugador,barco):
    
    #Hora de meter coordenadas, para asegurarnos de que no se pisen.
    #Usaremos un bucle while que solo parara cuando se haya situado el barco.
    #Es decir, cuando la funcion insertar_barco devuelva 0.
    #IMPORTANTE: para optimizar la colocacion, primero metemos los barcos mas grandes.
    bucle =1
    while bucle==1:
        barco.crear_coordenadas()
        #Ahora las metemos las coordenadas, si se encuentra una celda ocupada retornara 1.
        bucle = campo_jugador.insertar_barco(barco.coordenadas,barco.vidas)
        #Creamos coordenadas, primero asegurandonos que no se salga del tablero.

    return 1


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
            #Aqui tenemos un ejemplo, actualizamos ambos campos, pero solo se mostrara niebla.
            jugador.campo[coord1,coord2] = "_"
            niebla[coord1,coord2] = "_"
            return 0
        

    #Esta es la parte de la IA, uso sleep para que la ejecucion no sea tan rapida.
    if direccion == 2:
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