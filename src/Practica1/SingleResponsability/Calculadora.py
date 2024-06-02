class calculadora:

    @staticmethod
    def suma(valor1,valor2):
        try:
            return f"El resultado de la suma es: {valor1+valor2}"
        except TypeError:
            return "Valor no valido"
    
    @staticmethod
    def resta(valor1,valor2):
        try:
            return f"El resultado de la resta es: {valor1-valor2}"
        except TypeError:
            return "Valor no valido"
    
    @staticmethod
    def multiplicacion(valor1,valor2):
        try:
            return f"El resultado de la multiplicación es: {valor1*valor2}"
        except TypeError:
            return "Valor no valido"
    
    @staticmethod
    def division(valor1,valor2):
        try:
            return f"El resultado de la división es: {valor1/valor2}"
        except ZeroDivisionError:
            return "Error, se trata dividir por cero"
        except TypeError:
            return "Valor no valido"
