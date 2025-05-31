from abc import ABC, abstractmethod

# Clase abstracta
class Transporte(ABC):
    def __init__(self, capacidad):
        self._capacidad = capacidad  # Atributo protegido (con un guion bajo)

    @abstractmethod
    def mover(self):
        pass

# Subclase Colectivo
class Colectivo(Transporte):
    def mover(self):
        return f"El colectivo con capacidad {self._capacidad} personas rueda por la calle."

# Subclase Tren
class Tren(Transporte):
    def mover(self):
        return f"El tren con capacidad {self._capacidad} personas riela por las vías."

# Subclase Avion
class Avion(Transporte):
    def mover(self):
        return f"El avión con capacidad {self._capacidad} personas vuela por el cielo."

# Función que demuestra polimorfismo
def mostrar_movimientos(lista_transportes):
    for transporte in lista_transportes:
        print(transporte.mover())

# Prueba
if __name__ == "__main__":
    t1 = Colectivo(50)
    t2 = Tren(200)
    t3 = Avion(180)

    transportes = [t1, t2, t3]
    mostrar_movimientos(transportes)
