# -*- encoding: utf-8 -*-
# -*- encoding: utf-8 -*-

from constantes import *
from main import *
import random

def estaEnTablero(x, y):
	if x >= 0 and x < ANCHOTABLERO:
		if y < LARGOTABLERO and y >= 0:
			return True
		else:
			return False

	else:
		return False
		
		

def estadoLineaCompleta(tablero, y):
	for index_fila in range(len(tablero)):
		if tablero[index_fila][y] == BLANK: # Si encuentra 1 solo espacio en blanco en una fila es suficiente para decir que no es completa.(Logicamente)
			return False
	return True #Si no encuentra ningun espacio vacio, entonces es linea completa

def removerLineaCompleta(tablero):
	#No encontre un modo de eliminar la linea en si, asi que mejor copie cada fila sobre la linea completa una fila mas abajo y luego elimine facilmente la primera fila.
	filas = 0
	y = len(tablero*2) -1 #Para comenzar desde la parte de abajo del tablero, donde caen las piezas.

	while y >= 0:

		if estadoLineaCompleta(tablero, y) == True:
			for reversa in range(y,0,-1):
				for index in range(len(tablero)):
					tablero[index][reversa] = tablero[index][reversa-1] #Copia la fila superior en el lugar donde estaba la linea completa, es decir baja a todas las lineas superiores en 1 fila.

			for cada_espacio in range(len(tablero)):
					tablero[cada_espacio][0] = BLANK #La linea superior que queda duplicada la convierte en vacia.

			filas = filas + 1
		else:
			y = y - 1 #en caso de no ser una linea completa continuamos con el ciclo para ver si encontramos una.

	return filas


def obtenerTableroEnBlanco():
	 tablero = list() 
	 tab = list() #Lista vacia como base.(¿Redundante?) .
	 i = 0
	 p = 0
	 for x in range(ANCHOTABLERO):
		 tablero.append(list(tab))

	 while i < LARGOTABLERO:         
		while p < ANCHOTABLERO:
			 tablero[p].append(BLANK)
			 p = p +1

		p = 0
		i = i +1
		
	 return tablero

def obtenerNuevaPieza():
	#Valores Random para Diccionario
	llave_azar = random.choice (list(PIEZAS.keys())) #Elige azar entre una lista con las llaves del Diccionario.
	rotacion_azar = random.randint (0, len(PIEZAS[llave_azar])-1) 
	#Elige un entero al azar entre [0] y la longitud de la lista que contiene los templates de una llave especifica, de manera que se escoge un indice al azar, y asi tambien una rotacion al azar.
	color_azar = random.randint (0, len(COLORES)-1)
	#Al igual que arriba, la longitud-1 es por que los indices comienzan desde 0.
	

	nueva_pieza = dict()
	nueva_pieza ['forma'] = llave_azar
	nueva_pieza ['rotacion'] = rotacion_azar
	nueva_pieza ['x'] = int(ANCHOTABLERO / 2) - int(ANCHOTEMPLATE / 2) #De acuerdo a lo indicado en el documento de ayudantia de tarea 2, deja la pieza en medio del tablero al iniciar.
	nueva_pieza ['y'] = 0 #Comienza en el limite superior del tablero.
	nueva_pieza ['color'] = color_azar
	
	return nueva_pieza
	

def esPosicionValida(tablero, pieza, adjX=0, adjY=0):
	for coord_x in range(ANCHOTEMPLATE):
		for coord_y in range(LARGOTEMPLATE):
			suma_y = adjY+coord_y+pieza['y'] #La suma de las coordenadas y, va a ser nuestra nueva coordenada y para verfificar ciertos casos. (Este valor siempre es positivo)
			suma_x = adjX+coord_x+pieza['x'] #Igual que arriba, solo que este valor si puede ser negativo.

			if PIEZAS[pieza['forma']][pieza['rotacion']][coord_y][coord_x] == BLANK:
				#Revisa el template de la pieza para ver si el punto en cuestion es un punto vacio o es la pieza y asi ver cuando puede salirse del tablero o cuando va a chocar con una pieza o con el tablero.
				#Si el punto resulta ser parte de la pieza, no continua y pasa al siguiente for.
				continue

			elif estaEnTablero(suma_x, suma_y) == False: #Chequea que las nuevas coordenadas(suma de estas) esten dentro del tablero.Retorna Falso si no esta en tablero.
				return False
			
			elif tablero[suma_x][suma_y] != BLANK: # Si el tablero esta ocupado retorna falso
				return False
	return True

def agregarTablero(tablero, pieza):
#Recorremos el template y cambiamos los puntos que no son BLANK a el codigo del color, para que la pieza tome un color.

	for x in range(ANCHOTEMPLATE):		
		for y in range(LARGOTEMPLATE):

			suma_y = y + pieza['y'] # Es la suma porque pieza['y'] es una bariable que nunca cambia, por lo tanto le sumamos valores del rango del largo del template para asi ir recorriendo el template en si, en el tablero.
			suma_x = x + pieza['x'] # Igual que arriba

			if PIEZAS[pieza['forma']][pieza['rotacion']][y][x] != BLANK: # Si la pieza en dichas coordenadas no esta en blanco significa que debemos asignarle el color a dicho punto que esta ocupado.
				
				tablero[suma_x][suma_y] = pieza['color'] #Añadimos el punto (o cuadro en este caso) de color al tablero.
				# El proceso se repite hasta llenar de color todos los cuadros necesarios