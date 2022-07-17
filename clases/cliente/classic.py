from .cliente import Cliente

class Classic(Cliente):

    LIMITE_RETIRO_DIARIO = 10000
    COMISION_TRANSFERENCIA = 0.01
    MAXIMO_A_RECIBIR_SIN_AVISO = 150000
    

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