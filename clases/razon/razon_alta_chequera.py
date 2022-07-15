import re
from .razon import Razon

class Razon_alta_chequera(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)
    
    def resolver(self, cliente, transacciones):
        if not(transacciones['tipo'] == self.tipo):
            return False
        if (self.clienteEsClasico(cliente['tipo'])):
            return 'Lo clientes de tipo Classic no pueden tener chequeras, raja de aca'
        if self.limiteChequeras(cliente['tipo'], transacciones['totalChequerasActualmente']):
            return 'Ya ha alcanzado el limite de chequeras que puede tener'

    def clienteEsClasico(self, tipoCliente):
        if tipoCliente == 'CLASSIC':
            return True
        return False

    def limiteChequeras(self, tipoCliente, cantidadChequeras):
        if tipoCliente == 'GOLD' and cantidadChequeras == 1:
            return True
        if tipoCliente == 'BLACK' and cantidadChequeras == 2:
            return True
        return False