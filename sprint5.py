import json

class Cliente:
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.transacciones = transacciones
    def __str__(self):
        return f"{self.numero} {self.nombre} {self.apellido} {self.dni} {self.tipo} {self.transacciones}"

class Transacciones:
    def __init__(self, estado, tipo, cuentaNumero, permitidoActualParaTransaccion, monto, fecha, numero):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.permitidoActualParaTransaccion = permitidoActualParaTransaccion
        self.monto = monto
        self.fecha = fecha
        self.numero = numero

class Classic(Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        super().__init__(numero, nombre, apellido, dni,"Classic", transacciones)
    def tarjeta_debito(self):
        tarjeta_debito=1
        print(f"Puede tener {tarjeta_debito} tarjeta de debito.")
    
    def caja_ahorro(self):
        caja_ahorro="pesos"
        print(f"Puede tener una caja de ahorro en {caja_ahorro} o opcionalmente de dolares con cargo mensual.")
    
    def retiros(self):
        retiros=5
        limite=10000
        print(f"Puede tener {retiros} retiros sin comisiones, luego se aplican una tarifa y tienes un limite de {limite} pesos por cajero.")
    
    def tarjeta_credito(self):
        print("No tienes acceso a tarjeta de credito")
    
    def transferencias(self):
        print("Comisión del 1% por transferencias salientes y 0.5% por transferencias entrantes.")

class Gold(Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        super().__init__(numero, nombre, apellido, dni,"Gold", transacciones)

    def tarjeta_debito(self):
        tarjeta_debito=1
        print(f"Puede tener {tarjeta_debito} tarjeta de debito.")
    
    def caja_ahorro(self):
        n_caja_ahorro=2
        caja_ahorro="pesos"
        print(f"Puede tener hasta {n_caja_ahorro} cajas de ahorro en {caja_ahorro} o opcionalmente de dolares con cargo mensual y una cuenta corriente sin cargos adicionales.")
    
    def retiros(self):
        retiros="ilimitados"
        limite=20000
        print(f"Puede tener  retiros {retiros} sin comisiones y tienes un limite de {limite} pesos en retiros diarios.")
    
    def tarjeta_credito(self):
        tartejas_credito="VISA, Mastercard y/o American Express"
        extensiones=5
        limite_un_pago=150000
        limite_cuotas=100000
        print(f"Tiene tarjetas {tartejas_credito} con {extensiones} extensiones cada una y un limite de {limite_un_pago} pesos en un pago y limite de {limite_cuotas} pesos en cuotas")
    
    def transferencias(self):
        print("Comisión del 0.5% por transferencias salientes y 0.1% por transferencias entrantes.")

class Black(Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        super().__init__(numero, nombre, apellido, dni,"Black", transacciones)
    def tarjeta_debito(self):
        tarjeta_debito=5
        print(f"Puede tener {tarjeta_debito} tarjetas de debito.")
    
    def caja_ahorro(self):
        n_caja_ahorro=5
        caja_ahorro="pesos"
        caja_ahorro_usd="dolares"
        print(f"Puede tener hasta {n_caja_ahorro} cajas de ahorro en {caja_ahorro} o {caja_ahorro_usd} sin comisiones, luego se aplica uncargo extra.")
    
    def cuenta_corrinete(self):
        n_cuenta_corriente=3
        print(f"Hasta {n_cuenta_corriente}  cuentas corrientes sin cargos adicionales.")
    
    def retiros(self):
        retiros="ilimitados"
        limite=100000
        print(f"Puede tener  retiros {retiros} sin comisiones y tienes un limite de {limite} pesos en retiros diarios.")
    
    def tarjeta_credito(self):
        tartejas_credito="VISA, Mastercard y/o American Express"
        extensiones=10
        limite_un_pago=500000
        limite_cuotas=600000
        print(f"Tiene tarjetas {tartejas_credito} con {extensiones} extensiones cada una y un limite de {limite_un_pago} pesos en un pago y limite de {limite_cuotas} pesos en cuotas")
    
    def cuentas_inversion(self):
        print("Tiene acceso a cuentas inversiones.")

    def chequeras(self):
        print("Posibilidad de tener hasta 2 chequeras.")

    def transferencias(self):
        print("No se aplican comisiones en las transferencias.")

cliente = Classic(1,"Juanse", "Guilisasti", "43351326","Classic","transaccion")
cliente2 = Gold(2,"Anabella", "Lezcano", "45233001", "a", "transaccion" )
cliente3 = Black(3,"Luciano", "Duarte", "43321564","b", "transacciones" )

cliente_json = json.dumps(cliente.__dict__, indent=4)
cliente2_json = json.dumps(cliente2.__dict__, indent=4)
cliente3_json = json.dumps(cliente3.__dict__, indent=4) 

print(cliente_json)
cliente.tarjeta_credito()

print(cliente2_json)
cliente2.tarjeta_credito()

print(cliente3_json)
cliente3.tarjeta_credito()

