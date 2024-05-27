from animal import Animal
from abc import abstractmethod

class Herbivoro(Animal):
    @abstractmethod
    def pastar(self):
        pass