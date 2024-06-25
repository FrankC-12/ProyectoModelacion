class Viaje:
    def __init__(self, origen, destino, costo, escalas):
        self.origen = origen
        self.destino = destino
        self.costo = costo
        self.escalas = escalas
    
    def __str__(self):
        return f"Origen: {self.origen}, Destino: {self.destino}"
    

