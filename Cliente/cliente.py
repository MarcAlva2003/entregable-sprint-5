import json
import pathlib
from urllib.parse import ParseResultBytes

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
            tipo = reader['tipo']),

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

"""

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
           
        cliente = Cliente(nombre = reader['nombre'],
            apellido = reader['apellido'],
            numero = reader['numero'],
            dni = reader['dni'],
            direccion = reader['direccion'],
            tipo = reader['tipo'],
            transacciones = reader['transacciones'])

        return cliente


class Cliente:

    def _init_(self,nombre,apellido,numero,dni,direccion,tipo,transacciones):
        
        self._nombre = nombre
        self._apellido = apellido
        self._numero = numero
        self._dni = dni
        self._direccion = direccion
        self._tipo = tipo
        self._transacciones = transacciones
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def numero(self):
        return self._numero

    @property
    def dni(self):
        return self._dni
    
    @property
    def direccion(self):
        return self._direccion

    @property
    def tipo(self):
        return self._tipo
    
    @property
    def transacciones(self):
        return self._transacciones

    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre

    @apellido.setter
    def apellido(self,nuevo_apellido):
        self._nombre = nuevo_apellido

    @numero.setter
    def numero(self,nuevo_numero):
        self._numero = nuevo_numero
    
    @dni.setter
    def dni(self,nuevo_dni):
        self._dni = nuevo_dni

    @direccion.setter
    def direccion(self,nuevo_direccion):
        self._direccion = nuevo_direccion

    @tipo.setter
    def tipo(self,nuevo_tipo):
        self._tipo = nuevo_tipo

    @transacciones.setter
    def transacciones(self,nuevo_transacciones):
        self._transacciones = nuevo_transacciones
    

    def puede_crear_chequera(self):
        pass

    def puede_crear_tarjeta_credito(self):
        pass

    def puede_comprar_dolar(self):
        pass
    
        
    def _repr_(self):
        return f"nombre: {self.nombre}, apellido: {self.apellido}, numero: {self.numero},dni: {self.dni},tipo:{self.tipo}"

           
cliente = Buscar_datos.iniciar_objeto_cliente()
cliente.nombre('Juan Carlos') # Esto no funka
print(cliente.nombre)"""