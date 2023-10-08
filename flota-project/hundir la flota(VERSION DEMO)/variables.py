import clases
import random
#Creamos los 2 jugadores, jugador 1 es siempre persona, jugador 2 sera IA o persona.
#Para seguir flujo de codigo, ve a clases.py a las clases de jugador
campo_jugador1 = clases.Tablero_jugador_1()
campo_jugador2 = clases.Tablero_jugador_2()
niebla = clases.Niebla_de_guerra

#Creamos las variables de claes Barco.
#Orientacion es un numero aleatorio, las vidas del barco son introducidas mediante un int.
#Aqui generamos numero aleatorio.
orientacion = random.randint(1,4)
#Aqui, generamos un barco con 1 vida.
barco1= clases.Barco(1,orientacion)
#Repetimos para todos los barcos.
orientacion = random.randint(1,4)
barco1_1 = clases.Barco(1,orientacion)
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
barco3_1 = clases.Barco(3,orientacion)
orientacion = random.randint(1,4)
barco3_2 = clases.Barco(3,orientacion)
orientacion = random.randint(1,4)
barco4 = clases.Barco(4,orientacion)

#Lo mismo que la funcion de crear barcos para jugador 1
orientacion = random.randint(1,4)
jugador_2_barco1_1 = clases.Barco(1,orientacion)
