from cliente import *

class Black(Cliente):

    LIMITE_RETIRO_DIARIO = 100000
    DESCUBIERTO_CUENTA_CORRIENTE = 10000
    LIMITE_CHEQUERAS_UNIDADES = 2
    LIMITE_TARJETA_UNIDADES = 5
    

    def __init__(self,nombre,apellido,numero,dni,direccion,tipo,transacciones):
        super().__init__(
            nombre,apellido,numero,dni,direccion,tipo,transacciones
        )

    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

    def puede_comprar_dolar(self):
        return True