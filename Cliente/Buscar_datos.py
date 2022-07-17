import json
import pathlib
from cliente import Cliente
from classic import Classic
from gold import Gold
from black import Black


class Buscar_datos:
    
    @classmethod
    def buscar_archivo(cls):

        ruta = pathlib.Path('./datos')

        print('Los archivos de clientes disponibles son los siguientes:')
        for archivo_json in ruta.glob('*.json'):
            print(f"Archivo: {archivo_json}")
            
        archivo_cliente = input('Ingrese el nombre del archivo del cliente: ')
           
        with open(archivo_cliente,'r') as f:
                 reader = json.load(f)
           
        return reader

    @classmethod
    def iniciar_objeto_cliente(cls):

        reader = Buscar_datos.buscar_archivo()

        if reader['tipo'] == 'CLASSIC':
            cliente = Classic(nombre = reader['nombre'],
            apellido = reader['apellido'],
            numero = reader['numero'],
            dni = reader['dni'],
            direccion = reader['direccion'],
            tipo = reader['tipo'],
            transacciones = reader['transacciones'])
        elif reader['tipo'] == 'GOLD':
            cliente = Gold(nombre = reader['nombre'],
            apellido = reader['apellido'],
            numero = reader['numero'],
            dni = reader['dni'],
            direccion = reader['direccion'],
            tipo = reader['tipo'],
            transacciones = reader['transacciones'])
        elif reader['tipo'] == 'BLACK':
            cliente = Black(nombre = reader['nombre'],
            apellido = reader['apellido'],
            numero = reader['numero'],
            dni = reader['dni'],
            direccion = reader['direccion'],
            tipo = reader['tipo'],
            transacciones = reader['transacciones'])
        else:
            print('ATENCION CONTROLAR ERROR EN EL TIPO DEL CLIENTE')
            cliente = Cliente(nombre = reader['nombre'],
            apellido = reader['apellido'],
            numero = reader['numero'],
            dni = reader['dni'],
            direccion = reader['direccion'],
            tipo = reader['tipo'],
            transacciones = reader['transacciones'])

        return cliente

datos_cliente = Buscar_datos.iniciar_objeto_cliente()
print(datos_cliente)
print(type(datos_cliente))
print(datos_cliente)