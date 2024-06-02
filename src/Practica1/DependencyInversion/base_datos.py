from abc import ABC, abstractmethod

class BaseDatos(ABC):
    @abstractmethod
    def guardar(self, data):
        pass

    @abstractmethod
    def leer(self):
        pass
