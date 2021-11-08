##############################################
# Proyecto 2 / Analisis de Algotritmos       #
# Gustavo Pérez Badilla                      #
# Mauricio Agüero Marquez                    #
# Fecha de creación: 20/10/2021      2:05 PM #
##############################################
########## IMPORTACION DE LIBRERIAS ##########
##############################################

import tkinter as tk
from tkinter import filedialog, messagebox
import cv2 as cv

############ CREACION DE CLASES #############

class BaseDatos:
    archivo = ""
    imagen = ""

    def __init__(self, nomArchivo = "", nomImagen = ""):
        self.archivo = nomArchivo
        self.imagen = nomImagen
    
    def crearImagen(self):
        self.imagen = cv.imread(self.archivo)

############ CREACION DE FUNCIONES ###########

def inicioAlgoritmo(datos):
    if (datos.archivo == ""):
        messagebox.showerror("ERROR AL CARGAR ARCHIVO", "El archivo no ha sido cargado. Por favor, ingrese un archivo '.png'.")
        return
    elif (datos.archivo[-4:] != ".png"):
        messagebox.showerror("ERROR", "El tipo del archivo no es un '.png'. Por favor ingrese uno válido.")
        return
    else:
        print("Paso la validacion")
        datos.crearImagen()
        print(datos.imagen.shape)
        print(datos.imagen[0, 0])
        return

def buscarImagen(datos, labelArchivo):
    datos.archivo = filedialog.askopenfilename(initialdir = "/", title = "Seleccione la imagen",
                                          filetypes = (("Imagenes PNG", "*.png*"), ("Todos los archivos", "*.*")))
    nomCorto = datos.archivo.split("/")

    labelArchivo.config(text = nomCorto[-1])

def ventanaPrincipal():
    global ventana

    baseDatos = BaseDatos()
    ventana = tk.Tk()
    ventana.title("Solucionador de laberintos")
    ventana.geometry("1000x600")
    ventana.config(bg = "gray10", )

    titulo = tk.Label(ventana, text = "Solucionador de laberintos", font = ("Arial", 25), fg = "snow", bg = "gray10")
    titulo.pack()

    mensaje1 = tk.Label(ventana, text = "Seleccione el laberinto por solucionar:", font = ("Arial", 15), fg = "snow", bg = "gray10")
    mensaje1.place(x = 25, y = 150)

    nombreArchivo = tk.Label(ventana, text = "", font = ("Arial", 15), fg = "snow", bg = "gray10")
    nombreArchivo.place(x = 255, y = 250)

    archivoLabel = tk.Label(ventana, text = "Nombre del archivo:", font = ("Arial", 15), fg = "snow", bg = "gray10")
    archivoLabel.place(x = 25, y = 250)

    seleccionarArchivo = tk.Button(ventana, text = "Seleccionar", font = ("Arial", 15), bg = "gray80", command = lambda: buscarImagen(baseDatos, nombreArchivo))
    seleccionarArchivo.place(x = 365, y = 145)

    iniciar = tk.Button(ventana, text = "Iniciar", font = ("Arial", 15), bg = "gray80", width = 15, command = lambda: inicioAlgoritmo(baseDatos))
    iniciar.place(x = 815, y = 550)

    ventana.mainloop()



############## CODIGO PRINCIPAL ##############

ventanaPrincipal()


