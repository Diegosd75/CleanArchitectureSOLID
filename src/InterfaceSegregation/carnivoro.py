from abc import abstractmethod
from animal import Animal

class Carnivoro(Animal):
    @abstractmethod
    def cazar(self):
        pass