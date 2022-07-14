from account import *
from address import *
from reason import *
from .pedir_data import PedirData
import json
import csv

#pedir_data
    # hace
        #Pide nombre json a recorrer
        #Pide nombre del html a retornar
        #Crea cliente dependiendo el tipo
    # retorna
        #Cliente
        #transacciones
        #evento
        #nombre del html a retornar

#razones
    # hace
        #Analiza cual es la raxon de la transferencia cancelada
    # retorna
        #raxon de la transferencia cancelada

#crearHtml
    # hace
        #Crea el archivo html con el nombre que el usuario ingresó
        #Toma una lista con transacciones y las escribe en el html
        #Debe diferenciar si la transaccion es aceptada (no escribe razón) o rechazada (escribe razón)
        

def obtenerData():
    with open('data/eventos_black.json','r') as f:
        reader = json.load(f)
        return reader

data = obtenerData()

transacciones = data.transacciones()
cliente = data.getCliente()
evento = data.getEvento()

direccion = Address(data['direccion']['calle'], data['direccion']['numero'], data['direccion']['ciudad'], data['direccion']['provincia'], data['direccion']['pais'])

razon = razonCrearTarjeta(cliente, transacciones, )

# if data['tipo'] == 'CLASSIC':
#     clientClassic = ClientClassic(data['nombre'],data['apellido'],data['numero'],data['dni'], direccion)
# elif data['tipo'] == 'GOLD':
#     clientClassic = ClientGold(data['nombre'],data['apellido'],data['numero'],data['dni'], direccion)
# else:
#     clientClassic = ClientBlack(data['nombre'],data['apellido'],data['numero'],data['dni'], direccion)

print(clientClassic.__dict__)

# razon = RazonTipoChequera('asd')

# razon.resolver(clientClassic)