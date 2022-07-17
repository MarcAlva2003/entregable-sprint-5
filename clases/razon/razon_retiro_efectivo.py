from .razon import Razon

class Razon_retiro_efectivo(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)


    def resolver(self, cliente, transacciones):
        print(type(transacciones['tipo']))
        print(type(self.tipo))
        if transacciones['tipo'] == self.tipo:
            return False
        if self.dineroInsuficiente(cliente.tipo, transacciones['saldoEnCuenta'], transacciones['monto']):
            return 'Dinero en cuenta insuficiente, pruebe con un monto menor.'
        if self.maximoDiarioRetirado(transacciones['cupoDiarioRestante'], transacciones['monto']):
            return 'Ya ha superado el monto maximo que puede retirar por día.'
        return False
        
    def maximoDiarioRetirado(self, cupoDiarioRestante, montoARetirar):
        if cupoDiarioRestante < montoARetirar:
            return True
        return False

    def dineroInsuficiente(self, tipoCuenta, saldoEnCuenta, montoARetirar):
        if tipoCuenta == 'CLASSIC' and saldoEnCuenta < montoARetirar:
            return True
        if saldoEnCuenta >= 0:
            if tipoCuenta == 'GOLD' and (saldoEnCuenta + 10000) < montoARetirar:
                return True
            if tipoCuenta == 'BLACK' and (saldoEnCuenta + 10000) < montoARetirar:
                return True
        else:
            if tipoCuenta == 'GOLD' and (10000 + saldoEnCuenta) < montoARetirar:
                return True
            if tipoCuenta == 'BLACK' and (10000 + saldoEnCuenta) < montoARetirar:
                return True
        return False