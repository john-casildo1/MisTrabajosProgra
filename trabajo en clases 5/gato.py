class Gato:
    def __init__(self, nombre, raza, edad, peso, color, hambre, energia, felicidad, salud, carino):
        self.nombre = nombre        # nombre del gato
        self.raza = raza           # raza del gato
        self.edad = edad           # edad en años
        self.peso = peso           # peso en kg
        self.color = color         # color del pelaje
        self.hambre = hambre       # nivel de hambre (0-100, 100=muy hambriento)
        self.energia = energia     # nivel de energía (0-100)
        self.felicidad = felicidad # nivel de felicidad (0-100)
        self.salud = salud         # nivel de salud (0-100)
        self.carino = carino       # nivel de cariño hacia el dueño (0-100)

    def alimentar(self):
        if self.hambre > 0:
            self.hambre = self.hambre - 40
            if self.hambre < 0:
                self.hambre = 0
            self.energia = self.energia + 15
            if self.energia > 100:
                self.energia = 100
            self.felicidad = self.felicidad + 10
            if self.felicidad > 100:
                self.felicidad = 100
            print(f"{self.nombre} ha comido y está satisfecho")
        else:
            print(f"{self.nombre} no tiene hambre")

    def jugar(self):
        if self.energia >= 25:
            self.energia = self.energia - 25
            self.felicidad = self.felicidad + 20
            if self.felicidad > 100:
                self.felicidad = 100
            self.carino = self.carino + 5
            if self.carino > 100:
                self.carino = 100
            self.hambre = self.hambre + 15
            if self.hambre > 100:
                self.hambre = 100
            print(f"¡{self.nombre} ha jugado y está muy feliz!")
        else:
            print(f"{self.nombre} está muy cansado para jugar")

    def dormir(self):
        self.energia = self.energia + 50
        if self.energia > 100:
            self.energia = 100
        self.salud = self.salud + 5
        if self.salud > 100:
            self.salud = 100
        self.hambre = self.hambre + 10
        if self.hambre > 100:
            self.hambre = 100
        print(f"{self.nombre} ha dormido y recuperó energía")

if __name__ == "__main__":
    # Objeto 1: Gato joven y activo
    gato1 = Gato("Miau", "Siamés", 2, 4.5, "crema", 60, 80, 70, 90, 85)
    
    # Objeto 2: Gato adulto tranquilo
    gato2 = Gato("Pelusa", "Persa", 5, 6.2, "blanco", 40, 60, 85, 95, 90)
    
    # Objeto 3: Gatito que necesita cuidados
    gato3 = Gato("Travieso", "Mestizo", 1, 2.8, "negro", 90, 45, 60, 75, 50)
    
    # Probando 3 métodos principales
    print("=== CUIDANDO A LOS GATOS ===")
    gatos = [gato1, gato2, gato3]
    
    # Método 1: Alimentar a todos
    print("\n--- 1. ALIMENTANDO ---")
    for gato in gatos:
        gato.alimentar()
    
    # Método 2: Jugar con todos
    print("\n--- 2. JUGANDO ---")
    for gato in gatos:
        gato.jugar()
    
    # Método 3: Que todos duerman
    print("\n--- 3. DURMIENDO ---")
    for gato in gatos:
        gato.dormir()
    
    # Estado final
    print("\n--- ESTADO FINAL ---")
    for gato in gatos:
        print(f"{gato.nombre}: Energía={gato.energia}, Felicidad={gato.felicidad}, Cariño={gato.carino}")