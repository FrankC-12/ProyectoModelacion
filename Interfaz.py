import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Toplevel
from Dijkstra import dijkstra
from Graph import Grafo

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Agencia de Viajes")
        
        # Tamaño de la ventana y posición centrada
        window_width = 350
        window_height = 300
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Eliminar el ícono de la pluma
        self.root.iconbitmap(default="")
        
        self.create_widgets()
        self.load_cities()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Configurar el grid para que se expanda con la ventana
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Configurar el grid del main_frame
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_rowconfigure(3, weight=1)
        
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        main_frame.grid_columnconfigure(3, weight=1)

        # Crear estilo personalizado
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 14))
        style.configure('TCombobox', font=('Arial', 14))
        style.configure('TButton', font=('Arial', 14))
        style.configure('TCheckbutton', font=('Arial', 14))

        # Etiqueta y combobox para el lugar de origen
        origen_label = ttk.Label(main_frame, text="Lugar de origen:", style='TLabel')
        origen_label.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.origen_combobox = ttk.Combobox(main_frame, style='TCombobox')
        self.origen_combobox.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Etiqueta y combobox para el lugar de destino
        destino_label = ttk.Label(main_frame, text="Lugar de destino:", style='TLabel')
        destino_label.grid(row=1, column=1, padx=5, pady=5, sticky="e")
        self.destino_combobox = ttk.Combobox(main_frame, style='TCombobox')
        self.destino_combobox.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        # Checkbox para la visa
        self.visa_var = tk.BooleanVar()
        visa_check = ttk.Checkbutton(main_frame, text="¿Posee Visa?", variable=self.visa_var, style='TCheckbutton')
        visa_check.grid(row=2, column=1, columnspan=2, padx=5, pady=(30, 5), sticky="n")

        # Botón para buscar vuelos (con tamaño de fuente más grande y más ancho)
        search_button = ttk.Button(main_frame, text="Buscar Vuelos", command=self.search_flights, width=12, style='TButton')
        search_button.grid(row=3, column=1, pady=10)

        # Botón para mostrar grafo
        graph_button = ttk.Button(main_frame, text="Mostrar Grafo", command=self.mostrar_grafo, width=12, style='TButton')
        graph_button.grid(row=3, column=2, pady=10)

    def load_cities(self):
        # Diccionario para asociar siglas a nombres de ciudades
        city_dict = {
            "CCS": "Caracas",
            "AUA": "Aruba",
            "CUR": "Curazao",
            "BON": "Bonaire",
            "SXM": "Sint Maarten",
            "SDQ": "Santo Domingo",
            "SBH": "San Bartolomé",
            "POS": "Puerto España",
            "BGI": "Barbados",
            "PTP": "Pointe-à-Pitre",
            "FDF": "Fort-de-France"
            # Añade más asociaciones según sea necesario
        }

        # Leer el archivo y obtener los símbolos únicos
        file_path = "caminos.txt"
        cities = set()
        
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    cities.add(parts[0])
                    cities.add(parts[1])
        
        # Convertir los símbolos a nombres completos junto con el código
        city_names = [f"{code} - {city_dict.get(code, code)}" for code in cities]

        # Rellenar los comboboxes
        self.origen_combobox['values'] = city_names
        self.destino_combobox['values'] = city_names

    def get_input_values(self):
        origen = self.origen_combobox.get()
        destino = self.destino_combobox.get()
        visa_required = self.visa_var.get()
        
        # Crear un diccionario con los valores obtenidos
        input_values = {
            "Origen": origen,
            "Destino": destino,
            "Visa": "Requiere Visa" if visa_required else "No Requiere Visa"
        }
        
        # Mostrar los valores en consola (opcional)
        print("Valores de entrada:", input_values)
        
        # Puedes devolver el diccionario o utilizarlo como necesites
        return input_values

    def search_flights(self):
        input_values = self.get_input_values()
        
        if not input_values["Origen"] or not input_values["Destino"]:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")
            return
        

        # Llamar a la función dijkstra con los valores de entrada
        start_node = input_values['Origen'].split(" - ")[0]
        end_node = input_values['Destino'].split(" - ")[0]
        visa = input_values['Visa'].split(" - ")[0]
        graph = Grafo()
        path, distance = dijkstra(graph.build_graph(), start_node, end_node)
        if path:
            dijkstra.crear(path)
        else:
            print(f"No se encontró una ruta de {start_node} a {end_node}")
    
    def mostrar_grafo(self):
        # Leer el archivo y construir el grafo
        graph = nx.Graph()
        file_path = "caminos.txt"
        
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    origen, destino, peso = parts
                    graph.add_edge(origen, destino, weight=float(peso))
        
        # Dibujar el grafo
        pos = nx.spring_layout(graph, seed=42, k=100, scale=3.0, iterations=100)  # Ajusta 'k', 'scale' e 'iterations' según sea necesario
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        
        # Crear una figura inicial
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Dibujar nodos, bordes y etiquetas de bordes
        nx.draw(graph, pos, with_labels=True, node_size=1200, node_color="skyblue", font_size=10, font_weight="bold", ax=ax)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red', font_size=10, ax=ax)
        
        # Configurar título y márgenes
        ax.set_title("Grafo de Rutas", fontsize=20, pad=20)
        plt.margins(0.1)
        
        # Crear una nueva ventana de Tkinter
        new_window = Toplevel(self.root)
        new_window.title("Grafo de Rutas")

        # Mostrar en pantalla completa
        new_window.attributes('-fullscreen', True)
        
        # Integrar la figura de matplotlib en la ventana de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Función para cerrar la ventana y liberar recursos
        def cerrar_ventana():
            new_window.destroy()  # Cerrar la ventana de grafo
            plt.close(fig)  # Cerrar la figura de matplotlib
        
        # Configurar que la ventana se cierre al presionar el botón de cerrar
        new_window.protocol("WM_DELETE_WINDOW", cerrar_ventana)
        
        # Redibujar el grafo cuando se redimensiona la ventana
        def on_resize(event):
            new_width = event.width
            new_height = event.height
            canvas.figure.set_size_inches(new_width / 100, new_height / 100)  # Ajustar el tamaño de la figura según la nueva ventana
            canvas.draw()
        

        # Botón para cerrar la ventana (opcional, si deseas mantenerlo)
        cerrar_button = ttk.Button(new_window, text="Cerrar", command=cerrar_ventana)
        cerrar_button.pack(side=tk.BOTTOM, pady=10)