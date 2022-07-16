from cliente import *

class Classic(Cliente):
    

    def __init__(self,nombre,apellido,numero,dni,direccion,tipo,transacciones):
        
        super().__init__(
            nombre,apellido,numero,dni,direccion,tipo,transacciones
        )

    def puede_crear_chequera(self):
        return False

    def puede_crear_tarjeta_credito(self):
        return False

    def puede_comprar_dolar(self):
        return False