from TiendayProductos import Tienda
from TiendayProductos import Producto

print("Hola")

print(__name__)


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
