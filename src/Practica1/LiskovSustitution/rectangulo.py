from figura import Figura

class Rectangulo(Figura):
    def __init__(self,ancho,largo) -> None:
        super().__init__()
        self.ancho=ancho
        self.largo=largo
    
    def area(self):
        return f"El área del rectagulo es {self.ancho*self.largo}"
    
    def perimetro(self):
        return f"El parímetro del rectangulo es {(self.ancho*2)+(self.largo*2)}"