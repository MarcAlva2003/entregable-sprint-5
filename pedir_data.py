class PedirData:
    def __init__(self) -> None:
        pass

    def pedirNombreHtml():
        nombreHtml = input('Nombre archivo')
        return nombreHtml

    def pedirNombreJson():
        nombreJson = input('Nombre archivo')
        return nombreJson

    def retornarCliente():
        if data['tipo'] == 'CLASSIC':
            client = ClientClassic(data['nombre'],data['apellido'],data['numero'],data['dni'], direccion)
        elif data['tipo'] == 'GOLD':
            client = ClientGold(data['nombre'],data['apellido'],data['numero'],data['dni'], direccion)
        else:
            client = ClientBlack(data['nombre'],data['apellido'],data['numero'],data['dni'], direccion)
        return client
    
    def tr5ansaccines():
        return transaccoines