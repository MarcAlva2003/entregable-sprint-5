class Account:
    def __init__(self, limiteExtraccion, limiteTransferenciaRecibida, monto, costoTransferencia, saldoDescubiertoDisponible, tipoMoneda):
        self.limiteExtraccion = limiteExtraccion
        self.limiteTransferenciaRecibida = limiteTransferenciaRecibida
        self.monto = monto
        self.costoTransferencia = costoTransferencia
        self.saldoDescubiertoDisponible = saldoDescubiertoDisponible
        self.tipoMoneda = tipoMoneda