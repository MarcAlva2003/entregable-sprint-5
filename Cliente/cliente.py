import json


class Cliente:

    def __init__(self,nombre,apellido,numero,dni,direccion,tipo):
        
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.direccion = direccion
        self.tipo = tipo


    @classmethod
    def iniciar_archivo(cls,nombre_archivo_Json):
       
        with open(nombre_archivo_Json,'r') as f:
            reader = json.load(f)
            
            cliente = Cliente(nombre = reader['nombre'],
            apellido = reader['apellido'],
            numero = reader['numero'],
            dni = reader['dni'],
            direccion = reader['direccion'],
            tipo = reader['tipo'])

        return cliente

    def puede_crear_chequera(self):
        pass

    def puede_crear_tarjeta_credito(self):
        pass

    def puede_comprar_dolar(self):
        pass
    
        
    def __repr__(self):
        return f"{self.nombre},{self.apellido},{self.tipo},{self.dni}"

           
cliente_black = Cliente.iniciar_archivo('Datos/eventos_black.json')
cliente_classic = Cliente.iniciar_archivo('Datos/eventos_classic.json')


"""
La mejor forma de abordar este problema es generar una aplicación que reciba como input la información del TPS, la procese y emita un reporte que
sea capaz de mostrar la razón de porque estas transacciones fueron rechazadas para ponerla a disposición del equipo de atención al cliente. Si son aceptadas simplemente se agrega al reporte la transacción que se hizo sin detalle particular, de esta forma quedara completo el informe.
En el reporte se debe incluir el nombre de cliente, número, DNI, dirección y para cada transacción la fecha , el tipo de operación, el estado, el monto y razón por la cual se rechazó (vacío en caso de ser aceptada)."""