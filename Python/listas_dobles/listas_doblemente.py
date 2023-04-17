class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cola is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar_inicio(self):
        if self.cabeza is None:
            return None
        else:
            valor_eliminado = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente

            if self.cabeza is not None:
                self.cabeza.anterior = None
            else:
                self.cola = None

            return valor_eliminado

    def eliminar_final(self):
        if self.cola is None:
            return None
        else:
            valor_eliminado = self.cola.valor
            self.cola = self.cola.anterior

            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None

            return valor_eliminado
milista = ListaDobleEnlazada()
milista.agregar_inicio(1)
milista.agregar_inicio(2)
print(milista)
