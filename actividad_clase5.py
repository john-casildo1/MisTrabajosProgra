class Persona:
    def __init__(self, nombre, edad, direccion, telefono, cedula, genero, correo, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.cedula = cedula
        self.genero = genero
        self.correo = correo
        self.ocupacion = ocupacion
        self.carro = None
        self.materias = []
        self.cuenta_banco = None

    def __str__(self):
        return f'{self.nombre}, {self.edad} años, {self.ocupacion}'

    def encender_carro(self):
        if self.carro:
            self.carro.encender()
        else:
            print(f'{self.nombre} no tiene un carro asignado.')

    def matricular_materia(self, materia):
        self.materias.append(materia)
        print(f'{self.nombre} ha matriculado {materia.nombre}.')

    def asignar_cuenta(self, cuenta):
        self.cuenta_banco = cuenta

    def depositar(self, cantidad):
        if self.cuenta_banco:
            self.cuenta_banco.depositar(cantidad)

    def retirar(self, cantidad):
        if self.cuenta_banco:
            self.cuenta_banco.retirar(cantidad)

    def consultar_balance(self):
        if self.cuenta_banco:
            self.cuenta_banco.mostrar_balance()


class Carro:
    def __init__(self, marca, modelo, color, placa, tipo, combustible, motor, year, owner):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.placa = placa
        self.tipo = tipo
        self.combustible = combustible
        self.motor = motor
        self.year = year
        self.owner = owner
        self.encendido = True
        self.productos = []

    def encender(self):
        if self.encendido == True:
            print(f'El carro esta encendido.')
        else:
            print(f'El carro esta apagado.')
       

    def apagar(self):
        self.encendido = False
        print(f'{self.marca} {self.modelo} se ha apagado.')

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f'Producto {producto.nombre} agregado al carro.')


class Materia:
    def __init__(self, nombre, codigo, profesor, creditos, horario, aula, cuatrimestre, modalidad):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.creditos = creditos
        self.horario = horario
        self.aula = aula
        self.cuatrimestre = cuatrimestre
        self.modalidad = modalidad

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'


class Producto:
    def __init__(self, nombre, categoria, precio, cantidad, marca, codigo_barras, fecha_vencimiento, peso):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        self.marca = marca
        self.codigo_barras = codigo_barras
        self.fecha_vencimiento = fecha_vencimiento
        self.peso = peso

    def __str__(self):
        return f'{self.nombre} ({self.marca}) - ${self.precio}'


class CuentaBanco:
    def __init__(self, numero_cuenta, banco, tipo_cuenta, moneda, balance, titular, estado, interes):
        self.numero_cuenta = numero_cuenta
        self.banco = banco
        self.tipo_cuenta = tipo_cuenta
        self.moneda = moneda
        self.balance = balance
        self.titular = titular
        self.estado = estado
        self.interes = interes

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f'Depósito exitoso. Nuevo balance: {self.balance} {self.moneda}')

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f'Retiro exitoso. Nuevo balance: {self.balance} {self.moneda}')
        else:
            print('Fondos insuficientes.')

    def mostrar_balance(self):
        print(f'El balance actual es: {self.balance} {self.moneda}')


# Ejemplo de uso
if __name__ == "__main__":
    p1 = Persona("Ana", 25, "San José", "8888-9999", "1-2345-6789", "Femenino", "ana@email.com", "Estudiante")
    cuenta1 = CuentaBanco("123456", "BAC", "Ahorros", "CRC", 10000, p1.nombre, "Activa", 0.01)
    p1.asignar_cuenta(cuenta1)
    p1.depositar(2000)
    p1.retirar(500)
    p1.consultar_balance()

    mat1 = Materia("Programación 1", "ISC101", "Prof. Eduardo", 4, "8am-10am", "Lab A", "III", "Presencial")
    p1.matricular_materia(mat1)

    carro1 = Carro("Toyota", "Yaris", "Gris", "123ABC", "Sedan", "Gasolina", "1.5L", 2022, p1.nombre)
    p1.carro = carro1
    p1.encender_carro()

    prod1 = Producto("Leche", "Lácteos", 850, 2, "Dos Pinos", "1234567890", "2025-01-01", "1L")
    carro1.agregar_producto(prod1)
