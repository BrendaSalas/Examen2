import tkinter as tk
from ControladorElemento import ControladorElemento
from VistaElemento import VistaElemento

if __name__ == "__main__":
    url = "https://6720637be7a5792f05315535.mockapi.io/ElementosQuimicos"
    controlador = ControladorElemento(url)

    root = tk.Tk()  # Crear la ventana principal
    root.resizable(False, False)  # La ventana no es redimensionable
    app = VistaElemento(root, controlador)  # Crear la vista
    root.mainloop()  # Ejecutar el bucle principal de la aplicación