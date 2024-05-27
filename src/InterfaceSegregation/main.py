from perro import Perro
from vaca import Vaca

def main():
    perro1 = Perro()
    print(perro1.respirar())
    print(perro1.comer())
    print(perro1.dormir())
    print(perro1.cazar())
    vaca1 = Vaca()
    print(vaca1.respirar())
    print(vaca1.comer())
    print(vaca1.dormir())
    print(vaca1.pastar())


if __name__ == "__main__":
    main() 