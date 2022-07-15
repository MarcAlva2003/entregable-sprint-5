from .razon import Razon

class Razon_transferencia_recibida(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)


    def resolver(self, cliente, transacciones):
        if not(transacciones['tipo'] == self.tipo):
            return False
        if self.limiteMonto(cliente['tipo'], transacciones['monto']):
            return 'Se excede de su monto limite de transacciones recibidas, debera avisar al banco para recibirla'
        return False


    def limiteMonto(self, tipoCliente, monto):
        if tipoCliente == 'CLASSIC'and monto >=150000:
            return True
        if tipoCliente == 'GOLD' and monto >= 500000:
            return True
        if tipoCliente == 'BLACK':
            return True
        return False