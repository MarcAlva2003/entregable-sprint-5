from cliente import *

class Black(Cliente):
    

    def __init__(self,nombre,apellido,numero,dni,direccion,tipo,transacciones):
        
        #Call to super funtion to have access to all atributes/methods
        super().__init__(
            nombre,apellido,numero,dni,direccion,tipo,transacciones
        )

    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

    def puede_comprar_dolar(self):
        return True