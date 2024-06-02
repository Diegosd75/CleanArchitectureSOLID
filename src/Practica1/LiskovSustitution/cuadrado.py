from figura import Figura

class Cuadrado(Figura):
    def __init__(self, lado) -> None:
        super().__init__()
        self.lado=lado

    def area(self):
        return f"El área del cuadrado es {self.lado**2}"
    
    def perimetro(self):
        return f"El parímetro del cuadrado es {self.lado*4}"    
