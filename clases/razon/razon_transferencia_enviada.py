from cmath import log
from .razon import Razon
from ..cliente import *

class Razon_transferencia_enviada(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

    def resolver(self, cliente, transacciones):
        print('entro')
        if transacciones['tipo'] == self.tipo:
            return False
        if self.dineroInsuficiente(cliente.tipo, transacciones['saldoEnCuenta'], transacciones['monto']):
            return 'Dinero en cuenta insuficiente, pruebe con un monto menor.'
        return False
        

    def dineroInsuficiente(self, tipoCuenta, saldoEnCuenta, montoARetirar):
        if tipoCuenta == 'CLASSIC' and saldoEnCuenta < (montoARetirar * 1.1):
            return True
        if saldoEnCuenta >= 0:
            if tipoCuenta == 'GOLD' and (saldoEnCuenta + 10000) < (montoARetirar * 1.05):
                return True
            if tipoCuenta == 'BLACK' and (saldoEnCuenta + 10000) < montoARetirar:
                return True
        else:
            if tipoCuenta == 'GOLD' and (10000 + saldoEnCuenta) < (montoARetirar * 1.05):
                return True
            if tipoCuenta == 'BLACK' and (10000 + saldoEnCuenta) < montoARetirar:
                return True
        return False

# Que tenga dinero para enviarla + pagar comision