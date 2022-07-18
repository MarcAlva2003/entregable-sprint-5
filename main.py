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
transaccionesCliente = dataCliente.transacciones


for transaccion in transaccionesCliente:
	razonRechazo = ''
	for unaRazon in listaRazones:
		razonRechazo = unaRazon.resolver(dataCliente, transaccion)
		if not(razonRechazo == ''):
			break
	transaccion['razon'] = razonRechazo

