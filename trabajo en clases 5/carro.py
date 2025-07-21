class Carro:
    def __init__(self, marca, modelo, combustible, nivel_combustible, encendido, velocidad, kilometraje, nivel_aceite, llantas_buen_estado, estado_motor):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible  # tipo: gasolina, diesel, eléctrico
        self.nivel_combustible = nivel_combustible  # en porcentaje
        self.encendido = encendido  # True o False
        self.velocidad = velocidad  # km/h
        self.kilometraje = kilometraje  # km
        self.nivel_aceite = nivel_aceite  # 0-100
        self.llantas_buen_estado = llantas_buen_estado  # True o False
        self.estado_motor = estado_motor  # 0-100

   
    def encender(self):
        if self.encendido:
            return  
        if self.nivel_combustible < 5 or self.nivel_aceite < 10 or not self.llantas_buen_estado:
            return  
        self.encendido = True

   
    def apagar(self):
        if not self.encendido:
            return
        self.velocidad = 0
        self.encendido = False

   
    def conducir(self, distancia):
        if not self.encendido or self.nivel_combustible < 10 or not self.llantas_buen_estado:
            return
        consumo = distancia * 0.2  # 0.2% por km
        desgaste_motor = distancia * 0.1
        self.kilometraje += distancia
        self.nivel_combustible = max(0, self.nivel_combustible - consumo)
        self.estado_motor = max(0, self.estado_motor - desgaste_motor)
        self.nivel_aceite = max(0, self.nivel_aceite - distancia * 0.05)

   
    def repostar(self, cantidad):
        if self.combustible == "eléctrico":
            return  # necesita cargar, no repostar
        self.nivel_combustible = min(100, self.nivel_combustible + cantidad)

   
    def mantenimiento(self):
        self.estado_motor = min(100, self.estado_motor + 30)
        self.nivel_aceite = min(100, self.nivel_aceite + 50)
        self.llantas_buen_estado = True


if __name__ == "__main__":
   
    carro1 = Carro(
        marca="Toyota",
        modelo="Corolla",
        combustible="gasolina",
        nivel_combustible=80,
        encendido=False,
        velocidad=0,
        kilometraje=15000,
        nivel_aceite=75,
        llantas_buen_estado=True,
        estado_motor=85
    )
    
   
    carro2 = Carro(
        marca="Tesla",
        modelo="Model 3",
        combustible="eléctrico",
        nivel_combustible=95,
        encendido=False,
        velocidad=0,
        kilometraje=5000,
        nivel_aceite=100,
        llantas_buen_estado=True,
        estado_motor=98
    )
    
   
    carro3 = Carro(
        marca="Ford",
        modelo="Focus",
        combustible="diesel",
        nivel_combustible=25,
        encendido=False,
        velocidad=0,
        kilometraje=85000,
        nivel_aceite=15,
        llantas_buen_estado=False,
        estado_motor=45
    )
    
   
   
    print(f"\nIntentando encender {carro1.marca} {carro1.modelo}...")
    carro1.encender()
    print(f"¿Está encendido? {carro1.encendido}")
    
   
    if carro1.encendido:
        print(f"Conduciendo 50 km...")
        carro1.conducir(50)
        print(f"Nuevo kilometraje: {carro1.kilometraje} km")
        print(f"Combustible restante: {carro1.nivel_combustible:.1f}%")
    
   
    print(f"\nIntentando encender {carro3.marca} {carro3.modelo}...")
    carro3.encender()
    print(f"¿Está encendido? {carro3.encendido}")
    
   