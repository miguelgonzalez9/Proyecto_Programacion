# -*- coding: utf-8 -*-
"""
Eventos y juego
"""
from tkinter import ttk
from PIL import ImageTk, Image
import Tablero_class as tb

class Buscaminas:
    
    def __init__(self, col = 10, fil = 10):
        # Crear ventana con botones.
        self.tab = tb.Tablero(col, fil)
        self.tab.centrar_ventana()
        # Crear botones
        self.tab.agregar_botones()
        # Crear eventos
        for (b, fila, columna) in self.tab.botones:
                b.bind("<Button-1>", prueba())
                
        self.tab.mainloop()
        
        

    
def prueba():
    msj = "hola"
    print(msj)

b = Buscaminas()