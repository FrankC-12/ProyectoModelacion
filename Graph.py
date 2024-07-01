#Clase grafo
from Edge import Edge
from Vertex import Vertex
import matplotlib.pyplot as plt
import networkx as nx
class Grafo():
    def __init__(self):
        self.graph_dict = {}
        
#Agrego un vertice
    def agregarVertice(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
        


#Agrego una arista
    def agregarArista(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 in self.graph_dict and v2 in self.graph_dict:
            self.graph_dict[v1].append(v2)
            self.graph_dict[v2].append(v1)
        

    def is_vertex_in(self,vertex):
        if vertex in self.graph_dict:
            return True
        else:
            return False
        
    def get_vertex(self,vertex_name):
        vertex_name = Vertex()
        for vertex in self.graph_dict:
            if vertex.get_name() == vertex_name:
                return vertex
        return None

    def get_neighbours(self,vertex):
        return self.graph_dict[vertex]
    
    def __str__(self):
        all_edges = ""
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                vertex = Vertex()
                neighbour = Vertex()
                all_edges += str(vertex.get_name()) + " - " + str(neighbour.get_name()) + "\n"

        return all_edges
    
    def build_graph(graph):
        graph = Grafo()
        archivo = open("caminos.txt", "r")
        caminos = []
        for x in archivo:
            i = 0
            origen = x.split(",")[0]
            destino = x.split(",")[i+1]
            if "\n" in x.split(",")[i+2]:
                costo = x.split(",")[i+2].replace("\n", "")
            else:
                costo = x.split(",")[i+2]
        
            caminos.append((origen, destino,float(costo)))
        archivo.close()

        #Muestra el grafo en una interfaz
        vertices = []
        aristas = []
        for x in caminos:
            v1 = Vertex(x[0])
            v2 = Vertex(x[1])
            costo = x[2]
            edge = Edge(v1,v2)
            graph.agregarVertice(v1)
            graph.agregarVertice(v2)
            graph.agregarArista(edge)
            vertices.append(v1.get_name())
            vertices.append(v2.get_name())
            aristas.append((v1.get_name(),v2.get_name(),costo))
            print(f"{v1.get_name()}---->{v2.get_name()}, {costo}")
        # Crear un grafo sencillo
        G = nx.Graph()
        G.add_nodes_from(vertices)
        for arista in aristas:
            G.add_edge(arista[0], arista[1], weight=arista[2])
        
        # Dibujar el grafo con pesos
        pos = nx.spring_layout(G, k=0.05, scale=0.5)
        edges = G.edges()
        weights = [G[u][v]['weight'] for u, v in edges]

        # Definir el tamaño mínimo y máximo de las aristas
        min_edge_size = 2
        max_edge_size = 6

        # Calcular el tamaño de cada arista en función de su peso
        edge_sizes = [min_edge_size + (max_edge_size - min_edge_size) * (w - min(weights)) / (max(weights) - min(weights)) for w in weights]

        # Dibujar los nodos y las aristas
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', width=edge_sizes)

        # Mostrar los pesos de las aristas
        font_size = 8
        edge_labels = dict([((u, v,), f"{d['weight']:0.1f}") for u, v, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,font_size=font_size)

        # Mostrar el gráfico
        #plt.show()


            

    #Con este metodo muestro el grafo en una interfaz
    def show():
        graph = Grafo()
        graph.build_graph()
        print(graph)




        

    


        



        

    
    

 
