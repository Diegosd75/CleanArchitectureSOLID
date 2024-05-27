from carnivoro import Carnivoro

class Perro(Carnivoro):
    
    def respirar(self):
        return "El perro respira agitado."

    def comer(self):
        return "El perro come carne."

    def dormir(self):
        return "El perro duerme en su casa."

    def cazar(self):
        return "El perro caza animales pequeños."