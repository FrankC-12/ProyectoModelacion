class Persona:
    def __init__(self, name, visa):
        self.name = name
        self.visa = visa
    def __str__(self):
        return f"{self.name} {self.visa}"
    