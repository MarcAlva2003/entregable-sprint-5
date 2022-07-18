from .razon import Razon
from ..cliente import *

class Razon_transferencia_enviada(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

    def resolver(self, cliente, transacciones):
        if not(transacciones['tipo'] == self.tipo):
            return ""
        if self.dineroInsuficiente(cliente.tipo, transacciones['saldoEnCuenta'], transacciones['monto']):
            return 'Dinero en cuenta insuficiente, pruebe con un monto menor.'
        return ""

    def dineroInsuficiente(self, tipoCuenta, saldoEnCuenta, montoARetirar):
        if tipoCuenta == 'CLASSIC' and saldoEnCuenta < (montoARetirar * 1.1):
            return True
        # if saldoEnCuenta >= 0:
        if tipoCuenta == 'GOLD' and (saldoEnCuenta) < (montoARetirar * 1.05):
            return True
        if tipoCuenta == 'BLACK' and (saldoEnCuenta) < montoARetirar:
            return True

# Que tenga dinero para enviarla + pagar comision