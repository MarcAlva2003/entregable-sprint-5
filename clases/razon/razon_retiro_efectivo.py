from operator import truediv
from .razon import Razon

class Razon_retiro_efectivo(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)


    def resolver(self, cliente, transacciones):
        if transacciones['tipo'] == self.tipo:
            return False
        if self.maximoDiarioRetirado(transacciones['cupoDiarioRestante'], transacciones['monto']):
            return 'Ya ha superado el monto maximo que puede retirar por día.'

    def maximoDiarioRetirado(self, cupoDiarioRestante, montoARetirar):
        if cupoDiarioRestante < montoARetirar:
            return True
        return False

# Por falta de dinero
# Por maximo diario retirado
# 