import json
import pathlib

class Cliente:

    def __init__(self,nombre,apellido,numero,dni,direccion,tipo,transacciones):
        
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
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,nuevo_apellido):
        self._nombre = nuevo_apellido

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self,nuevo_numero):
        self._numero = nuevo_numero

    @property
    def dni(self):
        return self._dni
    @dni.setter
    def dni(self,nuevo_dni):
        self._dni = nuevo_dni
    
    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self,nuevo_direccion):
        self._direccion = nuevo_direccion

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,nuevo_tipo):
        self._tipo = nuevo_tipo
    
    @property
    def transacciones(self):
        return self._transacciones
    @transacciones.setter
    def transacciones(self,nuevo_transacciones):
        self._transacciones = nuevo_transacciones
    

    def puede_crear_chequera(self):
        pass

    def puede_crear_tarjeta_credito(self):
        pass

    def puede_comprar_dolar(self):
        pass
    
        
    def __repr__(self):
        return f"nombre: {self.nombre}, apellido: {self.apellido}, numero: {self.numero},dni: {self.dni},tipo:{self.tipo}"

