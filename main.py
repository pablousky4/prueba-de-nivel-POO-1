from subclase.coche import Coche
from subclase.bicicleta import Bicicleta
from subsubclase.moto import Moto
from catalogo import catalogar

# Crear objetos
vehiculos = [
    Coche("rojo", 4, 120, 1500),
    Bicicleta("azul", 2, "montaña"),
    Moto("negra", 2, 180, 600),
    Coche("blanco", 4, 100, 1300)
]

# Mostrar todos los vehículos
print("Lista completa de vehículos:")
catalogar(vehiculos)
print("\nFiltrar por número de ruedas:")
catalogar(vehiculos, 2)
catalogar(vehiculos, 4)
