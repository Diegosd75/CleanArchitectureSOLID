from cuadrado import Cuadrado
from rectangulo import Rectangulo

def main():
    cuadrado1=Cuadrado(0.25)
    print(cuadrado1.area())
    print(cuadrado1.perimetro())
    cuadrado2=Cuadrado(10)
    print(cuadrado2.area())
    print(cuadrado2.perimetro())
    rectangulo1=Rectangulo(10,20)
    print(rectangulo1.area())
    print(rectangulo1.perimetro())

if __name__ == "__main__":
    main()