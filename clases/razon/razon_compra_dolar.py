from .razon import Razon

class Razon_compra_dolar(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

    def resolver(self, cliente, transacciones):
        if not(transacciones['tipo']== self.tipo):
            return ""
        if not(cliente.puede_comprar_dolar()):
            return "Los clientes CLASSIC no pueden comprar dolares por no tener cuenta en dolares "
        return ""








