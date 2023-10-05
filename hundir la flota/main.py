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

print(campo_jugador2.vidas_totales)
print(campo_jugador2.campo)