##############################################
# Proyecto 2 / Analisis de Algotritmos       #
# Gustavo Pérez Badilla                      #
# Mauricio Agüero Marquez                    #
# Fecha de creación: 20/10/2021      2:05 PM #
##############################################
########## IMPORTACION DE LIBRERIAS ##########
##############################################

from math import pi
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2 as cv
import funciones as func
import random as r

############ CREACION DE CLASES #############

class BaseDatos:
    """Se guarda la imagen en una variable para mantener
       cualquier modificación y tener seguimiento del algoritmo."""

    def __init__(self, nomArchivo = "", nomImagen = ""):
        self.archivo = nomArchivo
        self.imagen = nomImagen
    
    def crearImagen(self):
        self.imagen = cv.imread(self.archivo)

class ADN:
    """Corresponde a los parámetros a tomar en cuenta para el avance del algoritmo
       genético relacionado con los individuos."""

    def __init__(self, objetivo = [], individuos = 10, pob = [], mutacion = 0.2, gen = 50):
        self.final = objetivo
        self.numIndividuos = individuos
        self.poblacion = pob
        self.probMutar = mutacion
        self.generaciones = gen
        self.genActual = 0
   

############ CREACION DE FUNCIONES ###########

def pasarGen(genLabel):
    """Se encarga de pasar las generaciones de los individuos
        Entradas:
            -Label indicando la generación
        Salidas:
            -N/A
    """
    if adn.genActual == 0:
        adn.genActual += 1
        genLabel.config(text = "Generación: " + str(adn.genActual))
        adn.poblacion = func.crearPoblacion(baseDatos.archivo, baseDatos.imagen, adn.numIndividuos)
        adn.poblacion = func.fitness(adn.poblacion, baseDatos.imagen, baseDatos.archivo)
        zoom = cv.resize(baseDatos.imagen, None, fx = 7, fy = 7, interpolation = cv.INTER_LINEAR)
        cv.imshow("Laberinto", zoom)
        print(adn.poblacion)
    else:
        adn.genActual += 1
        genLabel.config(text = "Generación: " + str(adn.genActual))
        print("hola")
        

def analisisImagen():
    """Abre un controlador para pasar a las siguientes generaciones del algoritmo."""
    global adn
    
    adn = ADN()
    pantalla = tk.Frame(ventana, width = 1000, height = 600, bg = "gray10")
    pantalla.place(x = 0, y = 0)

    generacionLabel = tk.Label(pantalla, text = "Generación: 0", font = ("Arial", 20), bg = "gray10", fg = "snow")
    generacionLabel.place(x = 425, y = 0)

    siguiente = tk.Button(pantalla, text = "Siguiente", font = ("Arial", 15), command = lambda: pasarGen(generacionLabel))
    siguiente.place(x = 850, y = 540)

def validarEntrada():
    """Valida que la imagen seleccionada sea correcta"""
    if (baseDatos.archivo == ""):
        messagebox.showerror("ERROR AL CARGAR ARCHIVO", "El archivo no ha sido cargado. Por favor, ingrese un archivo '.png'.")
        return
    elif (baseDatos.archivo[-4:] != ".png"):
        messagebox.showerror("ERROR", "El tipo del archivo no es un '.png'. Por favor ingrese uno válido.")
        return
    else:
        baseDatos.crearImagen()
        analisisImagen()
        return

def buscarImagen(labelArchivo):
    """Permite buscar la imagen dentro de la computadora y la guarda como variable"""
    baseDatos.archivo = filedialog.askopenfilename(initialdir = "/", title = "Seleccione la imagen",
                                          filetypes = (("Imagenes PNG", "*.png*"), ("Todos los archivos", "*.*")))
    nomCorto = baseDatos.archivo.split("/")
    labelArchivo.config(text = nomCorto[-1])

def ventanaPrincipal():
    """Interfaz gráfica del programa principal"""
    global ventana
    global baseDatos

    baseDatos = BaseDatos()
    ventana = tk.Tk()
    ventana.title("Solucionador de laberintos")
    ventana.geometry("1000x600")
    ventana.config(bg = "gray10", )
    ventana.resizable(False, False)

    titulo = tk.Label(ventana, text = "Solucionador de laberintos", font = ("Arial", 25), fg = "snow", bg = "gray10")
    titulo.pack()

    mensaje1 = tk.Label(ventana, text = "Seleccione el laberinto por solucionar:", font = ("Arial", 15), fg = "snow", bg = "gray10")
    mensaje1.place(x = 25, y = 150)

    nombreArchivo = tk.Label(ventana, text = "", font = ("Arial", 15), fg = "snow", bg = "gray10")
    nombreArchivo.place(x = 255, y = 250)

    archivoLabel = tk.Label(ventana, text = "Nombre del archivo:", font = ("Arial", 15), fg = "snow", bg = "gray10")
    archivoLabel.place(x = 25, y = 250)

    seleccionarArchivo = tk.Button(ventana, text = "Seleccionar", font = ("Arial", 15), bg = "gray80", command = lambda: buscarImagen(nombreArchivo))
    seleccionarArchivo.place(x = 365, y = 145)

    iniciar = tk.Button(ventana, text = "Iniciar", font = ("Arial", 15), bg = "gray80", width = 15, command = lambda: validarEntrada())
    iniciar.place(x = 815, y = 550)

    ventana.mainloop()



############## CODIGO PRINCIPAL ##############

ventanaPrincipal()


