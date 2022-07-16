import json
import pathlib
from urllib.parse import ParseResultBytes

class Clienteclassic:

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
            
            clienteclassic = Clienteclassic(nombre = reader['nombre'],
            apellido = reader['apellido'],
            numero = reader['numero'],
            dni = reader['dni'],
            direccion = reader['direccion'],
            tipo = reader['tipo']),

        return clienteclassic