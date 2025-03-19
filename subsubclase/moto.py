from subclase.bicicleta import Bicicleta

class Moto(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", {self.velocidad} km/h, {self.cilindrada} cc"
