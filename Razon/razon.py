class Razon:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def resolver(cliente,evento):
        print("Aca estoy")


class RazonTipoChequera(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)
    def resolver(cliente, evento):
        return super().resolver(evento)

class RazonAltaTarjetaCredito(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

class RazonComprarDolar(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

class RazonVentaDolar(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

class RazonRetiroEfectivo(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

class RazonTransferenciaEnviada(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)

class RazonTransferenciaRecibida(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)


objeto = RazonTipoChequera("asjadsd")
objeto.resolver("HOLA")


