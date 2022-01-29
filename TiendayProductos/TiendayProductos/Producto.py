class Producto:
    def __init__(self, nombre, precio, categoria, codigo):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.codigo = codigo

    def __str__(self):
        return f"{self.nombre} {self.precio} {self.categoria}"

    def update_price(self, percent_change, is_increased):
        if(is_increased == True):
            self.precio += self.precio*(percent_change/100)
        else:
            self.precio -= self.precio*(percent_change/100)

    def print_info(self):
        print(
            f"nombre del producto:{self.nombre}, categoría:{self.categoria}, precio:{self.precio}, codigo:{self.codigo}\n")


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
