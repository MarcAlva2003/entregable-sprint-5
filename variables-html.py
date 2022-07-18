nombreHTML = 'ingresado_por_cliente'+'.html'
cliente = {
    "Nombre": "Roberto",
    "Apellido":"Robertos",
    "Dni":"42511235",
    "tipo": "GOLD",
    "PuedeComprarDolar":False,
    "PuedeCrearChequera":False,
    "PuedeCrearTarjetaCredito":False,
	"direccion": {
		"calle":"Corrientes",
		"altura":"1232"
	}
}
transacciones = [{
			"estado": "ACEPTADA",
			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 9000,
			"cantidadExtraccionesHechas": 1,
			"monto": 1000,
			"fecha": "10/06/2022 16:00:55",
			"numero": 1,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
			"razon" : ""

		},
		{
			"estado": "RECHAZADA",
			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 15000,
			"monto": 11000,
			"fecha": "10/06/2022 16:40:55",
			"numero": 2,
			"saldoEnCuenta": 10000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
            "razon":"Esta es una razon de rechazo"
		},
		{
			"estado": "RECHAZADA",
			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 3000,
			"monto": 9000,
			"fecha": "10/06/2022 16:55:45",
			"numero": 3,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
            "razon":"Esta es una razon de rechazo"
		},
		{
			"estado": "RECHAZADA",
			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 3000,
			"monto": 9000,
			"fecha": "10/06/2022 16:56:55",
			"numero": 4,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
            "razon":"Esta es una razon de rechazo"
		},
		{
			"estado": "RECHAZADA",
			"tipo": "ALTA_TARJETA_CREDITO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 3000,
			"monto": 9000,
			"fecha": "11/06/2022 16:00:55",
			"numero": 5,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
            "razon":"Esta es una razon de rechazo"
		},
		{
			"estado": "RECHAZADA",
			"tipo": "ALTA_CHEQUERA",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 3000,
			"monto": 9000,
			"fecha": "12/06/2022 16:00:55",
			"numero": 6,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
            "razon":"Esta es una razon de rechazo"
		},
		{
			"estado": "RECHAZADA",
			"tipo": "COMPRA_DOLAR",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 3000,
			"monto": 9000,
			"fecha": "13/06/2022 10:00:00",
			"numero": 7,
			"saldoEnCuenta": 1000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
            "razon":"Esta es una razon de rechazo"
		},
		{
			"estado": "RECHAZADA",
			"tipo": "TRANSFERENCIA_ENVIADA",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 3000,
			"monto": 100000,
			"fecha": "14/06/2022 16:00:55",
			"numero": 8,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
            "razon":"Esta es una razon de rechazo"
		},
		{
			"estado": "ACEPTADA",
			"tipo": "TRANSFERENCIA_RECIBIDA",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 3000,
			"monto": 9000,
			"fecha": "20/06/2022 16:00:55",
			"numero": 9,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
			"razon" : ""
		},
		{
			"estado": "RECHAZADA",
			"tipo": "TRANSFERENCIA_RECIBIDA",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 3000,
			"monto": 600000,
			"fecha": "21/06/2022 16:00:55",
			"numero": 10,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 1,
			"totalChequerasActualmente" : 1,
            "razon":"Esta es una razon de rechazo"
		}]

content = ''
for transaccion in transacciones:
	row = '<tr><td>'+transaccion['fecha']+'</td><td>' + transaccion['tipo']+'</td><td>' + transaccion['estado']+'</td><td>' + str (transaccion['monto'])+'</td><td>' + transaccion['razon']+'</td></tr>'
	

	content += row