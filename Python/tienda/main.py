from tienda import Tienda
from producto import Producto


tienda1 = Tienda("elian&mauricio")

producto1 = Producto("Polera 1",15000,"mujer")
producto2 = Producto("Polera 2",10000,"hombre")
producto3 = Producto("Polera 3",15000,"hombre")
producto4 = Producto("Polera 4",10000,"mujer")
producto5 = Producto("Polera 5",15000,"nina")
producto6 = Producto("Polera 6",10000,"nino")

tienda1.agregar_producto(producto1).agregar_producto(producto2).agregar_producto(producto3).agregar_producto(producto4).agregar_producto(producto5).agregar_producto(producto6)

tienda1.imprimir_productos()
"""
producto1.print_info()
producto2.print_info()
producto3.print_info()
producto4.print_info()
producto5.print_info()
producto6.print_info()
"""