class Tienda:
    def __init__(self, nombreTienda):
        self.nombre = nombreTienda
        self.listadeProductos = []

    def __str__(self):
        print(f"{self.nombre} {self.listadeProductos}")

    def add_product(self, new_product):
        self.listadeProductos.append(new_product)
        return self

    # El id es el codigo dentro de la lista
    def sell_product(self, id):
        for producto in self.listadeProductos:
            if producto.codigo == id:
                print(producto.codigo)
    # POP() elimina un elemento por su indice
    # REMOVE() elimina un elemento por su valor
                self.listadeProductos.remove(producto)
            else:
                print("Inserte un codigo existente")
        # if id== len(self.listadeProductos):
        #     self.listadeProductos.pop(id)
        # else:
        #     print("Este indice no existe")

    def inflation(self, percent_increase):
        # recorrer los objetos de la lista productos
        for producto in self.listadeProductos:
            # a cada prodducto se le aumenta el porcentaje de PRECIO
            producto.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        # recorrer los objetos de la lista producto
        for producto in self.listadeProductos:
            # si la categoria de cada producto, concuerda con la categoria ingresada
            # le aplica un descuento
            if producto.categoria == category:
                producto.update_price(percent_discount, False)
            # En caso de no existir la categoria, manda el mensaje de no existencia
            else:
                print("La categoria no existe")
        return self

    def print_lista(self):
        print(
            f"El nombre de mi tienda es:{self.nombre} y tiene los siguientes productos: \n")
        for item in self.listadeProductos:
            item.print_info()


if __name__ == '__main__':
    tienda = Tienda("La Tienda")
    cerveza = Producto("cerveza", 500, "bebidas", 879878)

    cerveza.print_info()

    # desde lo mas pequeño hacia lo más grande
    tienda.add_product(cerveza)
    tienda.add_product(Producto("Kross", 1990, "bebidasCalidad", 656787))

    cerveza.update_price(10, False)
    cerveza.print_info()

    tienda.inflation(10)
    tienda.print_lista()

    # responde dos veces porque existen dos categorias
    tienda.set_clearance("bebidas", 20)
    tienda.print_lista()

    tienda.sell_product(656787)
    tienda.print_lista()
