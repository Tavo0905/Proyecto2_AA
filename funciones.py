##############################################
# Funciones auxiliares para el programa      #
# Proyecto 2 - Analisis de Algoritmos        #
##############################################

###################### Importar Modulos ##########################

import cv2 as cv
import random as r

###################### Clases #############################

###################### Funciones ###########################

#pasa un número de decimal (int) a binario (string)
def decABin(num):
    binario = 0
    exp = 0
    while num > 0:
        binario += (num % 2) * (10 ** exp)
        num //= 2
        exp += 1
    binario = ("0" * (6 - len(str(binario)))) + str(binario)
    return binario

#pasa un número de binario (int) a decimal (int)
def binADec(num):
    dec = 0
    mul = 1
    while num > 0:
        div = num % 10
        dec += div * mul
        num //= 10
        mul *= 2
    return dec


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
        print(len(inicio))
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

        #buscamos la cantidad de pixeles negros en un radio de 2 pixeles
        for x in range(centro[1] - 2, centro[1] + 3):
            for y in range(centro[0] - 2, centro[0] + 3):
                if imagen[x, y][0] == 0 and imagen[x, y][2] == 0 and imagen[x, y][2] == 0:
                    pixelesNegros += 1

        #entre más pixeles negros, menos apto es el individuo
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

        #pintamos el individuo en la imagen
        imagen[centro[1], centro[0]][0] = 255
        imagen[centro[1], centro[0]][1] = imagen[centro[1], centro[0]][2] = aclarante
    cv.imwrite(nombre, imagen)
    return sorted(poblacion, key = lambda x: x[1], reverse = True)

def reproducir(poblacion, imagen, nombre):
    padres = poblacion[:-4]
    hijos = []
    final = False
    
    #reproducimos los padres hasta tener 10 hijos
    while len(hijos) < 10:
        padre1 = padres[r.randint(0, 5)]
        padre2 = padres[r.randint(0, 5)]
        while padre2 == padre1:
            padre2 = padres[r.randint(0, 5)]

        #hacemos el cruce de los dos padres
        x1 = decABin(padre1[0][0])
        x2 = decABin(padre2[0][0])
        divisor = r.randint(2, 4)
        Xhijo1 = binADec(int(x1[:divisor] + x2[divisor:]))
        Xhijo2 = binADec(int(x2[:divisor] + x1[divisor:]))
        y1 = decABin(padre1[0][1])
        y2 = decABin(padre2[0][1])
        Yhijo1 = binADec(int(y1[:divisor] + y2[divisor:]))
        Yhijo2 = binADec(int(y2[:divisor] + y1[divisor:]))

        #hay una probabilidad del 10% de una mutación
        if r.uniform(0.0, 1.0) > 0.9:
            Xhijo1 += r.randint(-4, 4)
            Yhijo1 += r.randint(-4, 4)
        if r.uniform(0.0, 1.0) > 0.9:
            Xhijo2 += r.randint(-4, 4)
            Yhijo2 += r.randint(-4, 4)

        #si algún hijo quedó fuera de la imagen entonces no se toman en cuenta
        if Xhijo1 >= 50 or Xhijo2 >= 50:
            continue
        if Yhijo1 >= 50 or Yhijo2 >= 50:
            continue

        #si el hijo 1 está en un pixel blanco o rojo está bien
        if (imagen[Yhijo1, Xhijo1][0] == 255 and imagen[Yhijo1, Xhijo1][1] == 255 and imagen[Yhijo1, Xhijo1][2] == 255) or\
           (imagen[Yhijo1, Xhijo1][0] == 0 and imagen[Yhijo1, Xhijo1][1] == 0 and imagen[Yhijo1, Xhijo1][2] == 255):
            hijos.append([[Xhijo1, Yhijo1], 100])
        #si el hijo 2 está en un pixel blanco o rojo está bien
        if (imagen[Yhijo2, Xhijo2][0] == 255 and imagen[Yhijo2, Xhijo2][1] == 255 and imagen[Yhijo2, Xhijo2][2] == 255) or\
           (imagen[Yhijo2, Xhijo2][0] == 0 and imagen[Yhijo2, Xhijo2][1] == 0 and imagen[Yhijo2, Xhijo2][2] == 255):
            hijos.append([[Xhijo2, Yhijo2], 100])
        #si el hijo 1 está en un pixel verde es que se llegó al final
        if (imagen[Yhijo1, Xhijo1][0] == 0 and imagen[Yhijo1, Xhijo1][1] == 255 and imagen[Yhijo1, Xhijo1][2] == 0):
                final = True
                hijos.append([[Xhijo1, Yhijo1], 100])
        #si el hijo 2 está en un pixel verde es que se llegó al final
        if (imagen[Yhijo2, Xhijo2][0] == 0 and imagen[Yhijo2, Xhijo2][1] == 255 and imagen[Yhijo2, Xhijo2][2] == 0):
                final = True
                hijos.append([[Xhijo2, Yhijo2], 100])
    
    #al tener los hijos, se les aplica la función de fitness
    hijos = fitness(hijos, imagen, nombre)
    return hijos, final