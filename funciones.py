##############################################
# Funciones auxiliares para el programa      #
# Proyecto 2 - Analisis de Algoritmos        #
##############################################

###################### Importar Modulos ##########################

import cv2 as cv
import random as r

###################### Clases #############################

###################### Funciones ###########################

def mostrarImagen(imagen):
    """Despliega la informacion principal de la imagen.
            Entradas:
                -Imagen por trabajar
            Salidas:
                -Impresion de pixeles verdes y rojos
    """
    imagenZoom = cv.resize(imagen, None, fx = 7, fy = 7, interpolation = cv.INTER_LINEAR)
    for x in range(50):
        for y in range(50):
            if imagen[x, y][0] == 0 and imagen[x, y][1] == 255 and imagen[x, y][2] == 0:
                print("verde")
                print(imagen[x, y])
                print("-" * 100)
            elif imagen[x, y][0] == 0 and imagen[x, y][1] == 0 and imagen[x, y][2] == 255:
                print("rojo")
                print(imagen[x, y])
                print("-" * 100)
    cv.imshow("zoomed", imagenZoom)
    return

def determinarInicio(imagen):
    """Determina el origen del laberinto.
        Entradas:
            -Imagen por trabajar
        Salidas:
            -Inicio del laberinto
    """
    inicio = []
    for x in range(50):
        for y in range(50):
            if imagen[x, y][0] == 0 and imagen[x, y][1] == 0 and imagen[x, y][2] == 255:
                inicio.append([y, x])
    return inicio

def determinarFinal(imagen, poblacion):
    """Determina el final del algoritmo.
        Entradas:
            -Población
        Salidas:
            -Bool
    """
    return

def crearPoblacion(nombre, imagen, numIndividuos):
    """Crea la población inicial.
        Entradas:
            -Imagen
            -Nombre de la imagen
            -Cantidad de individuos por crear
        Salidas:
            -Población inicial
    """
    inicio = determinarInicio(imagen)
    poblacion = []
    for i in range(numIndividuos):
        pixelAleatorio = r.choice(inicio)
        if pixelAleatorio in poblacion:
            continue
        else:
            poblacion.append([pixelAleatorio, 100])
            imagen[pixelAleatorio[1], pixelAleatorio[0]][0] = 255
            imagen[pixelAleatorio[1], pixelAleatorio[0]][1] = 0
            imagen[pixelAleatorio[1], pixelAleatorio[0]][2] = 0
    cv.imwrite(nombre, imagen)
    return poblacion

def fitness(poblacion, imagen, nombre):
    """Establece qué tan apto es un individuo para su reproducción.
        Entradas:
            -Población
            -Imagen
            -Nombre de la imagen
        Salidas:
            -Población con su aptitud
    """
    for individuo in poblacion:
        pixelesNegros = 0
        centro = individuo[0]
        aclarante = 0
        for x in range(centro[1] - 2, centro[1] + 3):
            for y in range(centro[0] - 2, centro[0] + 3):
                if imagen[x, y][0] == 0 and imagen[x, y][2] == 0 and imagen[x, y][2] == 0:
                    pixelesNegros += 1
        if pixelesNegros == 0:
            pass
        elif 0 < pixelesNegros <= 2:
            individuo[1] = 95
            aclarante = 20
        elif 2 < pixelesNegros <= 6:
            individuo[1] = 80
            aclarante = 50
        elif 6 < pixelesNegros <= 12:
            individuo[1] = 65
            aclarante = 75
        elif 12 < pixelesNegros <= 18:
            individuo[1] = 40
            aclarante = 130
        elif 18 < pixelesNegros <= 23:
            individuo[1] = 20
            aclarante = 150
        else:
            individuo[1] = 5
            aclarante = 175
        imagen[centro[1], centro[0]][1] = imagen[centro[1], centro[0]][2] = aclarante
    cv.imwrite(nombre, imagen)
    return sorted(poblacion, key = lambda x: x[1], reverse = True)
        

