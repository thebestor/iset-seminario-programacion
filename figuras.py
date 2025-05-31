from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclase Cuadrado
class Cuadrado(Figura):
    def __init__(self):
        self.lado = 4

    def area(self):
        return self.lado * self.lado

# Subclase Circulo
class Circulo(Figura):
    def __init__(self):
        self.radio = 3

    def area(self):
        return math.pi * self.radio * self.radio
# Subclase Trianguulo
class Triangulo(Figura):
    def __init__(self):
        self.base = 3
        self.altura = 3
    def area(self):
        return self.altura * self.base / 2

figuras = [Cuadrado(), Circulo(), Triangulo()]

for pepito in figuras:
    print(f"{type(pepito).__name__}-->Area: {pepito.area()}")

    