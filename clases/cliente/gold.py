from .cliente import Cliente

class Gold(Cliente):
    
    LIMITE_RETIRO_DIARIO = 20000
    COMISION_TRANSFERENCIA = 0.005
    MAXIMO_A_RECIBIR_SIN_AVISO = 500000
    DESCUBIERTO_CUENTA_CORRIENTE = 10000
    LIMITE_CUENTA_CORRIENTE = -10000
    LIMITE_CHEQUERAS_UNIDADES = 1
    LIMITE_TARJETA_UNIDADES = 1

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