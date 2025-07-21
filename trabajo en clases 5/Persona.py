class Persona:
    def __init__(self, nombre, edad, occupacion, altura, peso, nacionalidad):

        self.nombre = nombre
        self.edad = edad
        self.occupacion = occupacion
        self.despierto = True
        self.Enfermo = False
        self.hambre = False
        self.sed = False
        self.altura = altura
        self.peso = peso
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.occupacion}.")
    def despertar(self):
        if not self.despierto:
            self.despierto = True
            print(f"{self.nombre} se ha despertado.")
        else:
            print(f"{self.nombre} ya está despierto.")
            
    def dormir(self):
        if self.despierto:
            self.despierto = False
            print(f"{self.nombre} se ha ido a dormir.")
        else:
            print(f"{self.nombre} ya está dormido.")
            
    def comer(self):
        if self.hambre:
            self.hambre = False
            print(f"{self.nombre} ha comido y ya no tiene hambre.")
        else:
            print(f"{self.nombre} no tiene hambre.")
            
    def beber(self):
        if self.sed:
            self.sed = False
            print(f"{self.nombre} ha bebido y ya no tiene sed.")
        else:
            print(f"{self.nombre} no tiene sed.")
            
    def enfermar(self):
        if not self.Enfermo:
            self.Enfermo = True
            print(f"{self.nombre} se ha enfermado.")
        else:
            print(f"{self.nombre} ya está enfermo.")
            
datos = Persona("Juan", 30, "Ingeniero", 1.75, 70, "Mexicano")
datos2 = Persona("Ana", 25, "Doctora", 1.65, 60, "Española")
datos3 = Persona("Carlos", 28, "Profesor", 1.80, 75, "Argentino")

datos.saludar()
