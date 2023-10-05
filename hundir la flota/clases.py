import numpy as np
import random


class Barco:

    coordenadas = []
    def __init__(self, vidas, orientacion):

        self.vidas = vidas
        self.orientacion = orientacion

    def crear_coordenadas(self):

        columna = random.randint(0,9)
        fila = random.randint(0,9)
        self.coordenadas=[]
        self.coordenadas.append((fila,columna))
        contador = self.vidas
        while contador > 1:
            
            match self.orientacion:
                case 1:
                    #orientacion de centro a arriba
                    if fila + contador >= 10:
                        columna = random.randint(0,9)
                        fila = random.randint(0,9)
                        self.coordenadas=[]
                        self.coordenadas.append((fila,columna))
                    else:
                        contador -=1
                        self.coordenadas.append((fila+contador, columna))
                
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
                        

        return self.coordenadas
    
class Juego:

    orden = 0

    def __init__(self, modo):

        self.modo = modo

class Tablero_jugador_1:

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
    
class Tablero_jugador_2:

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