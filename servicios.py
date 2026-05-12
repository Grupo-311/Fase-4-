from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self):
        return self.precio * 2


class AlquilerEquipo(Servicio):
    def calcular_costo(self):
        return self.precio * 1.5
    