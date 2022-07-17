#ALL APP HERE
# from clases import Razon_alta_chequera,Razon_alta_tarjeta_credito,Razon_compra_dolar,Razon_retiro_efectivo,Razon_transferencia_enviada,Razon_transferencia_recibida
from clases import *

razonAltaChequera = Razon_alta_chequera("ALTA_CHEQUERA")
razonAltaTarjetaCredito = Razon_alta_tarjeta_credito("ALTA_TARJETA_CREDITO")
razonCompraDolar = Razon_compra_dolar("COMPRA_DOLAR")
razonRetiroEfectivo = Razon_retiro_efectivo("RETIRO_EFECTIVO_CAJERO_AUTOMATICO")
razonTransferenciaEnviada = Razon_transferencia_enviada("TRANSFERENCIA_ENVIADA")
razonTransferenciaRecibida = Razon_transferencia_recibida("TRANSFERENCIA_RECIBIDA")

listaRazones=[razonAltaChequera,razonAltaTarjetaCredito,razonCompraDolar,razonRetiroEfectivo,razonTransferenciaEnviada,razonTransferenciaRecibida]

dataCliente = Buscar_datos.iniciar_objeto_cliente()
print(dataCliente.transacciones[5])

# for transaccion in transacciones:
# 	asd = razonAltaTarjetaCredito.resolver(cliente, transaccion)
# 	print(asd)

for transaccion in dataCliente.transacciones:
	for unaRazon in listaRazones:
		asd = unaRazon.resolver(dataCliente, transaccion)
		print(asd)


print(dataCliente.tipo)

# for transaccion in dataCliente.transacciones:
	# asd = razonAltaTarjetaCredito.resolver(dataCliente, transaccion)
	# asd = razonCompraDolar.resolver(dataCliente, transaccion)
	# asd = razonRetiroEfectivo.resolver(dataCliente, transaccion)
	# asd = razonTransferenciaEnviada.resolver(dataCliente, transaccion)
	# asd = razonTransferenciaRecibida.resolver(dataCliente, transaccion)

# cliente = {
#     "Nombre": "Roberto",
#     "Apellido":"Robertos",
#     "Dni":"42511235",
#     "tipo": "GOLD",
#     "PuedeComprarDolar":False,
#     "PuedeCrearChequera":False,
#     "PuedeCrearTarjetaCredito":False,
# 	"limiteRetiroDiario": 20000,
# 	"maximoTarjetaCredito":1,
# 	"maximoChequera":1,
# 	"comidionTransferencia":1.05,
# 	"maximoARecibirSinAviso":500000,
# 	"direccion": {
# 		"calle":"Corrientes",
# 		"altura":"1232"
# 	}
# }
# transacciones = [{
# 			"estado": "ACEPTADA",
# 			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 9000,
# 			"cantidadExtraccionesHechas": 1,
# 			"monto": 1000,
# 			"fecha": "10/06/2022 16:00:55",
# 			"numero": 1,
# 			"saldoEnCuenta": 100000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		},
# 		{
# 			"estado": "RECHAZADA",
# 			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 15000,
# 			"monto": 11000,
# 			"fecha": "10/06/2022 16:40:55",
# 			"numero": 2,
# 			"saldoEnCuenta": 10000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		},
# 		{
# 			"estado": "RECHAZADA",
# 			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 3000,
# 			"monto": 9000,
# 			"fecha": "10/06/2022 16:55:45",
# 			"numero": 3,
# 			"saldoEnCuenta": 100000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		},
# 		{
# 			"estado": "RECHAZADA",
# 			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 3000,
# 			"monto": 9000,
# 			"fecha": "10/06/2022 16:56:55",
# 			"numero": 4,
# 			"saldoEnCuenta": 100000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		},
# 		{
# 			"estado": "RECHAZADA",
# 			"tipo": "ALTA_TARJETA_CREDITO",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 3000,
# 			"monto": 9000,
# 			"fecha": "11/06/2022 16:00:55",
# 			"numero": 5,
# 			"saldoEnCuenta": 100000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		},
# 		{
# 			"estado": "RECHAZADA",
# 			"tipo": "ALTA_CHEQUERA",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 3000,
# 			"monto": 9000,
# 			"fecha": "12/06/2022 16:00:55",
# 			"numero": 6,
# 			"saldoEnCuenta": 100000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		},
# 		{
# 			"estado": "RECHAZADA",
# 			"tipo": "COMPRA_DOLAR",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 3000,
# 			"monto": 9000,
# 			"fecha": "13/06/2022 10:00:00",
# 			"numero": 7,
# 			"saldoEnCuenta": 1000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		},
# 		{
# 			"estado": "RECHAZADA",
# 			"tipo": "TRANSFERENCIA_ENVIADA",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 3000,
# 			"monto": 100000,
# 			"fecha": "14/06/2022 16:00:55",
# 			"numero": 8,
# 			"saldoEnCuenta": 100000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		},
# 		{
# 			"estado": "ACEPTADA",
# 			"tipo": "TRANSFERENCIA_RECIBIDA",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 3000,
# 			"monto": 9000,
# 			"fecha": "20/06/2022 16:00:55",
# 			"numero": 9,
# 			"saldoEnCuenta": 100000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		},
# 		{
# 			"estado": "RECHAZADA",
# 			"tipo": "TRANSFERENCIA_RECIBIDA",
# 			"cuentaNumero": 190,
# 			"cupoDiarioRestante": 3000,
# 			"monto": 600000,
# 			"fecha": "21/06/2022 16:00:55",
# 			"numero": 10,
# 			"saldoEnCuenta": 100000,
# 			"totalTarjetasDeCreditoActualmente" : 1,
# 			"totalChequerasActualmente" : 1
# 		}]

# for transaccion in transacciones:
# 	asd = razonAltaTarjetaCredito.resolver(cliente, transaccion)
# 	print(asd)
