from collections import deque

def contar_escalas(grafo, origen, destino):
    queue = deque([(origen, 0)])
    visitados = set()
    while queue:
        nodo, escalas = queue.popleft()
        if nodo == destino:
            return escalas
        if nodo not in visitados:
            visitados.add(nodo)
            if nodo in grafo:
                for vecino in grafo[nodo]:
                    queue.append((vecino, escalas + 1))
            else:
                # Si el nodo no existe en el grafo, se asume que no tiene conexiones
                continue
    return -1

# Definir el grafo a partir de los datos
grafo = {}
with open("caminos.txt", "r") as data:
    for line in data:
        origen, destino, _ = line.strip().split(",")
        if origen not in grafo:
            grafo[origen] = []
        grafo[origen].append(destino)

# Contar las escalas entre CCS y SXM
escalas = contar_escalas(grafo, "CCS", "SXM")
if escalas == -1:
    print("No se encontró un camino entre CCS y SXM")
else:
    print(f"Se necesitan {escalas} escalas para ir de CCS a SXM")