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
        '''self.cargar_datos()

    def cargar_datos(self):
        elementos = self.controlador.obtener_elementos()
        for elemento in elementos:
            self.tabla.insert("", "end", values=(elemento.id, elemento.element, elemento.group, elemento.period))'''

        self.tabla.pack(fill="both", expand=True)

        # Barra de búsqueda
        self.search_frame = tk.Frame(root)
        self.search_frame.pack(pady=10)

        tk.Label(self.search_frame, text="Buscar elemento por ID o Nombre:").pack(side="left")
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side="left", padx=5)

        self.search_btn = tk.Button(self.search_frame, text="Buscar", command=self.buscar_elemento)
        self.search_btn.pack(side="left", padx=5)

        # Botón para cargar 100 registros
        self.cargar_btn = tk.Button(root, text="Cargar 100 Elementos", command=self.cargar_datos)
        self.cargar_btn.pack(pady=10)

    def cargar_datos(self):
        # Limpiar la tabla antes de cargar nuevos datos
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Obtener y mostrar los elementos desde el controlador
        elementos = self.controlador.obtener_elementos()
        for elemento in elementos:
            # Inserta cada elemento en la tabla si todos los atributos existen
            self.tabla.insert("", "end", values=(getattr(elemento, 'id', ''),
                                                 getattr(elemento, 'element', ''),
                                                 getattr(elemento, 'group', ''),
                                                 getattr(elemento, 'period', '')))

    def buscar_elemento(self):
        # Obtener el valor de búsqueda
        query = self.search_entry.get().strip().lower()

        # Limpiar cualquier selección anterior
        for item in self.tabla.selection():
            self.tabla.selection_remove(item)

        # Recorrer los elementos de la tabla
        for item in self.tabla.get_children():
            item_values = self.tabla.item(item, "values")
            id_val, element_name = item_values[0], item_values[1].lower()
            if query == id_val or query == element_name:
                self.tabla.selection_add(item)
                self.tabla.see(item)  # Asegurarse de que el elemento sea visible
                break
        else:
            tk.messagebox.showinfo("Buscar Elemento", f"No se encontró el elemento '{query}'.")