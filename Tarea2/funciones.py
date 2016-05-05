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
	
    return

def obtenerTableroEnBlanco():
	tabla = [
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
    return tabla 

def obtenerNuevaPieza():
    return

def esPosicionValida(tablero, pieza, adjX=0, adjY=0):
    return

def agregarTablero(tablero, pieza):
	return