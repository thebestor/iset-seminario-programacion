from abc import ABC, abstractmethod 

class Transporte(ABC):
  def __init__(self,capacidad):
    self._capacidad = capacidad
  @abstractmethod
  def mover(self):
    pass

class Avion(Transporte):
  def mover(self):
    return f"El avion tiene una capacidad {self._capacidad} personas"
  
class Tren(Transporte):
  def mover(self):
     return f"El tren tiene una capacidad {self._capacidad} personas"
  
class Colectivo(Transporte):
  def mover(self):
    return f"El Colectivo tiene una capacidad {self._capacidad} personas"
  
def mostrasCapacidad(lista_transporte):
  for transporte in lista_transporte:
      print(transporte.mover())

avion1 = Avion(180)
tren1 = Tren(200)
colectivo1 = Colectivo(40)

transporte = [avion1,tren1,colectivo1]
mostrasCapacidad(transporte)