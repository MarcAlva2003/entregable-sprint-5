from .razon import Razon

class Razon_compra_dolar(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

    def resolver(self, cliente, transacciones):
        if not(transacciones['tipo']== self.tipo):
            return False
        if not(cliente["PuedeComprarDolar"]):
            return "Los clientes CLASSIC no pueden comprar dolares por no tener cuenta en dolares "
        return False








