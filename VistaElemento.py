# vista_elemento.py
import tkinter as tk
from tkinter import ttk

class VistaElemento:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Elementos Químicos")
        self.root.geometry("1024x600")  # Establecer el tamaño de la ventana
        self.root.resizable(False, False)  # La ventana no es redimensionable

        # Configuración de la tabla
        self.tabla = ttk.Treeview(root, columns=("id", "element", "group", "period"), show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("element", text="Elemento")
        self.tabla.heading("group", text="Grupo")
        self.tabla.heading("period", text="Período")
        self.tabla.pack(fill="both", expand=True)

        # Ajustar el ancho de las columnas
        self.tabla.column("id", width=50)  # Ancho para ID
        self.tabla.column("element", width=300)  # Ancho para Elemento
        self.tabla.column("group", width=100)  # Ancho para Grupo
        self.tabla.column("period", width=100)  # Ancho para Período

        # Cargar datos en la tabla
        self.cargar_datos()

    def cargar_datos(self):
        elementos = self.controlador.obtener_elementos()
        for elemento in elementos:
            self.tabla.insert("", "end", values=(elemento.id, elemento.element, elemento.group, elemento.period))
