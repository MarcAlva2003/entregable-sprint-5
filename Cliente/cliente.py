import json
from traceback import print_tb


class Cliente:

    def __init__(self,nombre,apellido,numero,dni,direccion,tipo):
        
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.direccion = direccion
        self.tipo = tipo

    # @property
    # #Property Decorator: read-only Attribute
    # def tipo(self):
    #     return self.tipo

    @classmethod
    def iniciar_archivo(cls,nombre_archivo_Json):
       
        with open(nombre_archivo_Json,'r') as f:
            reader = json.load(f)
            
            cliente = Cliente(nombre = reader['nombre'],
            apellido = reader['apellido'],
            numero = reader['numero'],
            dni = reader['dni'],
            direccion = reader['direccion'],
            tipo = reader['tipo'],)

        return cliente
        
    def __repr__(self):
        return f"{self.nombre},{self.apellido},{self.tipo},{self.dni}"

           
cliente_black = Cliente.iniciar_archivo('Datos/eventos_black.json')


cliente_classic = Cliente.iniciar_archivo('Datos/eventos_classic.json')
print(cliente_black)

