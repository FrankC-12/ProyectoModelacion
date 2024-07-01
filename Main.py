#Funcion para leer un txt

from Graph import Grafo
import tkinter as tk
from Interfaz import Interfaz

def main():
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
    # Llamada a get_input_values() después de cerrar la interfaz gráfica
    # Aquí se crea el objeto Grafo después de cerrar la interfaz gráfica
    graph = Grafo()
    graph.build_graph()

if __name__ == "__main__":
    main()

