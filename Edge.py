from Vertex import Vertex
class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def get_v1(self):
        return self.v1
    
    def get_v2(self):
        return self.v2
    
    def __str__(self):
        v1 = Vertex()
        v2 = Vertex()
        return str(v1.get_name()) + " - " + str(v2.get_name())
    

        

    