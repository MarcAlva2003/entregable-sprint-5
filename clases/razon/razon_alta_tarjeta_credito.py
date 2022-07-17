from .razon import Razon

class Razon_alta_tarjeta_credito(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

    def resolver(self, cliente, transacciones):
        if not(transacciones['tipo'] == self.tipo):
            return False
        if (self.clienteClassic(cliente.tipo)):
            return 'Lo clientes de tipo Classic no pueden tener tarjetas de credito'
        if self.limiteTarjetasCredito(cliente.tipo, transacciones['totalTarjetasDeCreditoActualmente']):
            return 'Ya ha alcanzado el limite de Tarjetas que puede tener'

    def clienteClassic(self, tipoCliente):
        if tipoCliente == 'CLASSIC':
            return True
        return False

    def limiteTarjetasCredito(self, tipoCliente, cantidadTarjetas):
        if tipoCliente == 'GOLD' and cantidadTarjetas == 1:
            return True
        if tipoCliente == 'BLACK' and cantidadTarjetas == 5:
            return True
        return False