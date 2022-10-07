class Producto():
    def __init__(self, codigo, tipo, nombre, precio):
        self.codigo = codigo
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return "Codigo: {}, Tipo: {}, Nombre: {}, Precio: {}".format(self.codigo, self.tipo, self.nombre, self.precio)
    def crear_producto():
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        codigo = input("Codigo: ")
        tipo = input("Tipo: ")
        nombre = input("Nombre: ")
        for elemento in nombre:
            if elemento not in letras:
                print("El nombre no puede contener numeros")
            else:
                print("El nombre es correcto")
        precio = float(input("Precio: "))
        print("Producto creado: ", Producto(codigo, tipo, nombre, precio))
Producto.crear_producto()
    
