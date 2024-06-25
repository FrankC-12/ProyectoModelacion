from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, end):
    # Obtener los nodos únicos del grafo
    nodes = set()
    for origin, neighbors in graph.items():
        nodes.add(origin)
        for neighbor in neighbors:
            nodes.add(neighbor)

    # Inicializar distancias y caminos
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0
    paths = {node: [] for node in nodes}
    paths[start] = [start]

    # Crear cola de prioridad
    pq = [(0, start)]

    while pq:
        # Obtener nodo con la distancia más corta
        curr_distance, curr_node = heapq.heappop(pq)

        # Si hemos llegado al nodo final, devolver el camino
        if curr_node == end:
            return paths[curr_node], distances[curr_node]

        # Si la distancia actual es mayor que la distancia almacenada, ignorar el nodo
        if curr_distance > distances[curr_node]:
            continue

        # Actualizar distancias y caminos para los nodos adyacentes
        for neighbor, weight in graph[curr_node].items():
            if neighbor in distances:
                distance = curr_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[curr_node] + [neighbor]
                    heapq.heappush(pq, (distance, neighbor))

    # Si no se encuentra un camino, devolver None
    return None, None

# Definir los datos
data = """CCS,AUA,40.00
CCS,CUR,35.00
CCS,BON,60.00
CCS,SXM,300.0
AUA,CUR,15.00
AUA,BON,15.00
CUR,BON,15.00
CCS,SDQ,180.0
SDQ,SXM,50.00
SXM,SBH,45.00
CCS,POS,150.0
CCS,BGI,180.0
POS,BGI,35.00
POS,SXM,90.00
BGI,SXM,70.00
POS,PTP,80.00
POS,FDF,75.00
PTP,SXM,100.0
PTP,SBH,80.00
CUR,SXM,80.00
AUA,SXM,85.00"""

# Crear grafo a partir de los datos
graph = defaultdict(dict)
for line in data.split('\n'):
    origin, dest, weight = line.split(',')
    graph[origin][dest] = float(weight)

# Encontrar el camino más corto entre CCS y SXM
path, distance = dijkstra(graph, 'CCS', 'SXM')
if path:
    print(f"El camino más corto entre CCS y SXM es: {' -> '.join(path)}")
    print(f"La distancia total es: {distance:.2f}")

    # Crear grafo con el camino más corto
    G_shortest = nx.Graph()
    for i in range(len(path) - 1):
        G_shortest.add_edge(path[i], path[i+1], weight=graph[path[i]][path[i+1]])

    # Dibujar el grafo con el camino más corto
    pos = nx.spring_layout(G_shortest)
    nx.draw(G_shortest, pos, with_labels=True)
    labels = nx.get_edge_attributes(G_shortest, 'weight')
    nx.draw_networkx_edge_labels(G_shortest, pos, edge_labels=labels)
    plt.show()
else:
    print(f"No se encontró un camino entre CCS y SXM")