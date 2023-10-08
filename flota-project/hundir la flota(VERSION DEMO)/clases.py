#EN ESTE PY SE DEFINEN LAS CLASES QUE COMPONEN EL JUEGO.

import numpy as np
import random
from funciones import *
#----------------------------------------CLASE BARCOS----------------------------------------------------
class Barco:
    """Tendra una variable fija donde almacenaremos las coordenadas.
    ¿Porque vidas y orientacion dentro? Porque se crearan un monton de variables de tipo Barco.
    De esta forma, podemos crear un monton de variables y rapidamente darles todo lo que necesitan."""
    coordenadas = []
    def __init__(self, vidas, orientacion):
        #vidas sera el numero de golpes que necesita para ser hundido.
        self.vidas = vidas
        #orientacion sera un numero del 1 al 4
        self.orientacion = orientacion
    """Este sera el metodo de la clase que creara las coordenadas donde estara situado el barco.
    Las coordenadas seran entre 0 y 9 y segun su orientacion, sera colocado de una forma u otra en el tablero.
    Primero creamos la coordenada que sera el "pico" del barco, luego a partir de la horientacion, se saca el resto."""
    def crear_coordenadas(self):
        #Coordenadas y filas son numeros aleatorios.
        columna = random.randint(0,9)
        fila = random.randint(0,9)
        #por si acaso queda algun residuo, o, se repite el proceso por posicion ya tomada.
        #Declaramos coordenadas como una lista vacia.
        self.coordenadas=[]
        self.coordenadas.append((fila,columna))
        #Self vidas es importante, mejor no cambiar su valor, ya que, se usara mas tarde.
        contador = self.vidas
        while contador > 1:
            """Como ejemplo. si tenemos la coordenada base que es el pico del barco [9,2]
            Si orientacion es 1, deberia ir del centro [9,2] hacia arriba.
            Tiene 4 vidas, la lista final de coordenadas sera [(9,2),(12,2),(11,2),(10,2)]
            Como se sale de la lista, entra dentro del primer if, se genera nueva posicion y lo intenta de neuvo.
            Asi hasta que pille un sitio libre.
            Por eso, es importante tener el pico, y el numero de vidas.
            Porque de esa forma, se hace instantaneamente el calculo de la posicion del barco.
            Siendo (9,2) el inicio, y (9+4,2) el final :)"""
            match self.orientacion:
                case 1:
                    #orientacion de centro a arriba
                    if fila + contador >= 10:
                        #Solo entra si se sale de su fila.
                        columna = random.randint(0,9)
                        fila = random.randint(0,9)
                        self.coordenadas=[]
                        self.coordenadas.append((fila,columna))
                    else:
                        #Si esta en un sitio libre, mete las coordenadas en la lista.
                        contador -=1
                        self.coordenadas.append((fila+contador, columna))
                #LO MISMO PARA EL RESTO DE CASES, PERO CAMBIA LA HORIENTACION.
                case 2:
                    #orientacion de centro a abajo
                    if fila - contador <= -1:
                        columna = random.randint(0,9)
                        fila = random.randint(0,9)
                        self.coordenadas=[]
                        self.coordenadas.append((fila,columna))
                    else:
                        contador -=1
                        self.coordenadas.append((fila-contador, columna))
                #Recuerda, sumar a la columna es mover a la derecha, si restas, a la izquierda.
                case 3:
                    #orientacion de centro a derecha
                    if columna + contador >= 10:
                        columna = random.randint(0,9)
                        fila = random.randint(0,9)
                        self.coordenadas=[]
                        self.coordenadas.append((fila,columna))
                    else:
                        contador -=1
                        self.coordenadas.append((fila, columna+contador))
                case 4:
                    #orientacion de centro a izquierda
                    if columna - contador <= -1:
                        columna = random.randint(0,9)
                        fila = random.randint(0,9)
                        self.coordenadas=[]
                        self.coordenadas.append((fila,columna))
                    else:
                        contador -=1

                        self.coordenadas.append((fila, columna-contador))
                        
        #devuelvo las coordenadas
        return self.coordenadas
    



class Tablero_jugador_1:
    #creamos el tablero del jugador 1, todo lleno de ?
    id = "JUGADOR 1"
    campo = np.full((10,10), "?")
    #Esta variable es la suma de todas las vidas de los barcos.
    vidas_totales = 0
    #Ya nos aseguramos en la clase Barco que no saliesen coordenadas fuera de rango.
    #Aqui solo las metemos con un bucle for.
    def insertar_barco(self, coord, vidas):
        for i,j in coord:
            #Recuerda que coord es una lista de tuplas, podemos acceder a cada valor de la tupla
            #con un bucle for de 2 variables, siendo i la fila y j la columna.
            #Este if, comprueba que las coordenadas esten libres, si detecta que una esta ocupada.
            #Retornara el 1, que continuara el bucle dentro de la funcion,
            if self.campo[i,j] == "O":
                return 1
            else:
                #Entra al else si no hay ninguna repetida.
                continue
        #Este bucle for mete las coordenadas dentro de nuestro tablero.
        for i,j in coord:
            self.campo[i,j] = "O"
        #aqui sumamos las vidas del barco.
        self.vidas_totales = self.vidas_totales + vidas
        return 0
    
class Tablero_jugador_2:
    #Lo mismo que antes, por comodidad en el manejo, tenemos otra clase de jugador 2.
    id = "JUGADOR 2"
    campo = np.full((10,10), "?")
    vidas_totales = 0
    def insertar_barco(self, coord, vidas):
        for i,j in coord:
            if self.campo[i,j] == "O":
                return 1
            else:
                continue
        for i,j in coord:
            self.campo[i,j] = "O"
        self.vidas_totales = self.vidas_totales + vidas
        return 0

class Niebla_de_guerra:

    niebla1 = np.full((10,10), "?")
    niebla2 = np.full((10,10), "?")

class Juego:

    orden = 0

    def __init__(self, modo):

        self.modo = modo

    def jugando(self,jugador1,jugador2,niebla):
        #Modo = 1 es para jugador contra IA
        if self.modo == 1:
            while True:
                #Aqui nos aseguramos de que se ponen coordenadas coherentes.
                #los print nos especifican formato, y con IFs nos aseguramos de que los valores introducidos
                #no causen problemas a la hora de probar las coordenadas luego.
                posicion = 0
                print(jugador1.vidas_totales)
                print(jugador1.campo)
                print(jugador2.vidas_totales)
                print(jugador2.campo)
                time.sleep(1)
                print("INSTRUCCIONES DE COORDENADAS: iNTRODUCE EN FORMATO X,X.\n",
                      "Escribe tutorial o comandos, para obtener info.")
                coordenada = []
                #en lugar de fila y columna, es primero y segundo, no quiero repetir nombres de varaiables.
                primera = 0
                segunda = 0
                #Con la variable check, nos aseguramos de detener este bucle cuando queramos.
                #Estara dentro del bucle hasta que el disparo haya sido exitoso.
                #Se repetira si se introduce mal la coordenada o ya esta marcada como agua o tocado (X).
                check = 1
                while check == 1:
                    #Pedimos input al usuario, podemos hacerlo entre 1 y 10 por facilidad para ver el tablero.
                    posicion = input("Introduce coordenada: ")
                    match posicion:
                        case "tutorial":
                            print("Dispara a una coordenada, si aciertas te toca de nuevo.\n",
                                  "Los barcos se han posicionado de forma aleatoria.\n",
                                  "Usa tu ingenio para hundirlos todos antes que la IA.")
                        case "tablero":
                            print("imprimiendo tableros...")
                            time.sleep(1)
                            print("Tablero jugador1")
                            print(niebla.niebla1)
                            time.sleep(1)
                            print("Tablero jugador2")
                            print(niebla.niebla2)
                            time.sleep(1)
                        case "comandos":
                            print("los comandos son: \n tablero \n tutorial \n salir")
                        case "salir":
                            print("Partida terminada...")
                            time.sleep(1)
                            return 0
                        case other:
                            print("Comprobando disparo...")
                            time.sleep(1)
                            #usamos split para comvertirlo en lista con 2 valores.
                            coordenada = posicion.split(",")
                            #si tenemos dos valores comprobamos que esten entre 1 y 10.
                            if len(coordenada) == 2:
                                try:
                                    if (int(coordenada[0]) <= 10 and int(coordenada[0]) > 0) and (int(coordenada[1]) <= 10 and int(coordenada[1]) > 0):
                                        primera = int(coordenada[0])-1
                                        segunda = int(coordenada[1])-1
                                        #aqui llamamos a la funcion de disparo.
                                        #devuelve 1 si la zona ya esta marcada, 0 si es valido, ademas actualiza el tablero.
                                        check = disparo(jugador2,1,primera,segunda,niebla.niebla1)
                                    else:
                                        print("POR FAVOR, INTRODUCE NUMEROS ENTRE 1 y 10")
                                except:
                                    print("POR FAVOR, INTRODUCE NUMEROS ENTRE 1 y 10")
                            else:
                                print("POR FAVOR, INTRODUCE NUMEROS EN FORMATO X,X")
                        #esta parte es solo para terminar el juego segun quien ha ganado.
                if jugador2.vidas_totales == 0:
                    print(jugador1.vidas_totales)
                    print(jugador1.campo)
                    print(jugador2.vidas_totales)
                    print(jugador2.campo)
                    print("JUGADOR1 HA GANADO!!!")
                    break
                print("Le toca a la IA...")
                time.sleep(1)
                check = 1
                while check == 1:
                    primera = random.randint(0,9)
                    segunda = random.randint(0,9)
                    check = disparo(jugador1,2,primera,segunda,niebla.niebla2)
                print("Turno de IA finalizado, imprimiendo tablero.",
                      "Al ser la demo, te imprimo los tableros sin niebla y las vidas de ambos.")
                #------------------------------------------------------
                if jugador1.vidas_totales == 0:
                    print("JUGADOR 2 HA GANADO!!!!")
                    break



        #Modo = 2 es jugador contra jugador.
        if self.modo == 2:
            #Repetimos esta parte para jugador 1.
            while True:
                posicion = 0
                print("INSTRUCCIONES DE COORDENADAS: iNTRODUCE EN FORMATO X,X.")
                coordenada = []
                primera = 0
                segunda = 0
                check = 1
                while check == 1:
                    posicion = input("Introduce coordenada: ")
                    print("Comprobando disparo...")
                    time.sleep(1)
                    coordenada = posicion.split(",")
                    if len(coordenada) == 2:
                        try:
                            if int(coordenada[0]) <= 10 or int(coordenada[1]) >= 0 and int(coordenada[1]) <= 10 or int(coordenada[0]) >= 0:
                                primera = int(coordenada[0])-1
                                segunda = int(coordenada[1])-1
                                check = disparo(jugador2,1,primera,segunda,niebla.niebla1)
                            else:
                                print("POR FAVOR, INTRODUCE NUMEROS ENTRE 1 y 10")
                        except:
                            print("POR FAVOR, INTRODUCE NUMEROS ENTRE 1 y 10")
                    else:
                        print("POR FAVOR, INTRODUCE NUMEROS EN FORMATO X,X")
                if jugador2.vidas_totales == 0:
                    print(jugador1.vidas_totales)
                    print(jugador1.campo)
                    print(jugador2.vidas_totales)
                    print(jugador2.campo)
                    print("JUGADOR1 HA GANADO!!!")
                    break
                #Ahora, cambiamos lo necesario para jugador 2.
                print("Turno de jugador 2...")
                time.sleep(1)
                posicion = 0
                coordenada = []
                primera = 0
                segunda = 0
                check = 1
                while check == 1:
                    posicion = input("Introduce coordenada: ")
                    print("Comprobando disparo...")
                    time.sleep(1)
                    coordenada = posicion.split(",")
                    if len(coordenada) == 2:
                        try:
                            if int(coordenada[0]) <= 10 or int(coordenada[1]) >= 0 and int(coordenada[1]) <= 10 or int(coordenada[0]) >= 0:
                                primera = int(coordenada[0])-1
                                segunda = int(coordenada[1])-1
                                #cambiamos jugador2 por jugador 1
                                check = disparo(jugador1,1,primera,segunda,niebla.niebla2)
                            else:
                                print("POR FAVOR, INTRODUCE NUMEROS ENTRE 1 y 10")
                        except:
                            print("POR FAVOR, INTRODUCE NUMEROS ENTRE 1 y 10")
                    else:
                        print("POR FAVOR, INTRODUCE NUMEROS EN FORMATO X,X")
                if jugador1.vidas_totales == 0:
                    print(jugador1.vidas_totales)
                    print(jugador1.campo)
                    print(jugador2.vidas_totales)
                    print(jugador2.campo)
                    print("JUGADOR1 HA GANADO!!!")
                    break
                print("Imprimiendo nieblas de guerra...")
                time.sleep(1)
                print(jugador1.vidas_totales)
                print(niebla.niebla1)
                print(jugador2.vidas_totales)
                print(niebla.niebla2)