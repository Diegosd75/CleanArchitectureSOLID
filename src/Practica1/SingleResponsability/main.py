from Calculadora import calculadora

def main():

    print(calculadora.suma(1, 2))
    print(calculadora.suma(1, "A"))
    print(calculadora.resta(3, 5))
    print(calculadora.multiplicacion(5, 5))
    print(calculadora.division(0, 5))
    print(calculadora.division(5, 0))
    print(calculadora.division(0, "e"))

if __name__ == "__main__":
    main()