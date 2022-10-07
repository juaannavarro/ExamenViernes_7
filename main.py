from ejercicios.ejercicio1_2 import *
from ejercicios.ejercicio3 import *
from ejercicios.ejercicio5 import *

if __name__=="__main__":
    alumno.crear_alumno()

if __name__=="__main__":
    Producto.crear_producto()

if __name__=="__main__":
    Vehiculo()
Coche
Bicicleta
Camioneta
Motocicleta
c = Coche("azul", 4, 150, 1200)
b = Bicicleta("roja", 2, "urbana")
C = Camioneta("verde", 4, 90, 2000, 500)
m = Motocicleta("negra", 2, 180, 600, "deportiva")
catalogar([c, b, C, m],0)