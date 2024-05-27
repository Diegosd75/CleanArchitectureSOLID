from herbivoro import Herbivoro

class Vaca(Herbivoro):
    def respirar(self):
        return "La vaca respira tranquilamente."

    def comer(self):
        return "La vaca come hierba."

    def dormir(self):
        return "La vaca duerme en el campo."

    def pastar(self):
        return "La vaca pasta en el campo."