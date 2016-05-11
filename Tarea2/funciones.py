# -*- encoding: utf-8 -*-
# -*- encoding: utf-8 -*-

from constantes import *
from main import *
import random

def estaEnTablero(x, y):
#Recibe 2 coordenadas y debe retornar True si esta dentro del tablero y False si esta fuera.
    if x >= 0 and x < ANCHOTABLERO and y < LARGOTABLERO:
    	return True

    else:
    	return False

def estadoLineaCompleta(tablero, y):
	for linea in range(ANCHOTABLERO):
		if tablero[x][y] == '.':
			return False
	return True 

def removerLineaCompleta(tablero):
	lineas_borradas = 0
	largo = LARGOTABLERO 

	while largo > 0:

		if estadoLineaCompleta(tablero, y):
			for quitar_linea in range(y, 0, -1):
				for ancho_t in range(ANCHOTABLERO):
					board[ancho_t][quitar_linea] = board[ancho_t][quitar_linea-1]

				for ancho_t in range(ANCHOTABLERO):
					board[ancho_t][0] = '.'

				lineas_borradas = lineas_borradas + 1
		else:
			y = y - 1 

		return lineas_borradas


def obtenerTableroEnBlanco():
	tablero = [
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
	]
	return tablero

def obtenerNuevaPieza():
	# return a random new piece in a random rotation and color
	forma_pieza = random.choice(list(PIEZAS.keys()))
	nueva_pieza = {'forma': forma_pieza,
                'rotacion': random.randint(0, len(PIEZAS[forma_pieza]) - 1),
                'x': int(ANCHOTABLERO / 2) - int(ANCHOPANTALLA / 2),
                'y': -4, 
                'color': random.randint(0, len(COLORES)-1)}

	return nueva_pieza
    

def esPosicionValida(tablero, pieza, adjX=0, adjY=0):
	for x in range(ANCHOPANTALLA):
	     for y in range(LARGOPANTALLA):
			entablero = y + pieza['y'] + adjY < 0
			if entablero or PIEZAS[pieza['forma_pieza']][pieza['rotacion']][y][x] == BLANK:
				continue
			if not entablero(x + pieza['x'] + adjX, y + pieza['y'] + adjY):
				return False
			if tablero[x + pieza['x'] + adjX][y + pieza['y'] + adjY] != BLANK:
				return False
	return True

def agregarTablero(tablero, pieza):
	 for x in range(ANCHOPANTALLA):
	 	for y in range(LARGOPANTALLA):
	 		if PIEZAS[pieza['forma_pieza']][pieza['rotacion']][y][x] != BLANK:
				board[x + pieza['x']][y + pieza['y']] = pieza['color']
