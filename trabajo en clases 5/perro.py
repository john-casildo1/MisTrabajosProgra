class Perro:
    def __init__(self, nombre, raza, edad, peso, color, energia, hambre, felicidad, salud, entrenamiento):
        self.nombre = nombre                # nombre del perro
        self.raza = raza                   # raza del perro
        self.edad = edad                   # edad en años
        self.peso = peso                   # peso en kg
        self.color = color                 # color del pelaje
        self.energia = energia             # nivel de energía (0-100)
        self.hambre = hambre               # nivel de hambre (0-100, 100 = muy hambriento)
        self.felicidad = felicidad         # nivel de felicidad (0-100)
        self.salud = salud                 # nivel de salud (0-100)
        self.entrenamiento = entrenamiento # nivel de entrenamiento (0-100)

    # Método 1: Alimentar al perro
    def alimentar(self):
        if self.hambre > 0:
            self.hambre = self.hambre - 30
            if self.hambre < 0:
                self.hambre = 0
            
            self.energia = self.energia + 10
            if self.energia > 100:
                self.energia = 100
            
            self.felicidad = self.felicidad + 5
            if self.felicidad > 100:
                self.felicidad = 100
            
            print(f"{self.nombre} ha sido alimentado. ¡Está satisfecho!")
        else:
            print(f"{self.nombre} no tiene hambre ahora.")

    # Método 2: Jugar con el perro
    def jugar(self):
        if self.energia >= 20:
            self.energia = self.energia - 20
            if self.energia < 0:
                self.energia = 0
            
            self.felicidad = self.felicidad + 15
            if self.felicidad > 100:
                self.felicidad = 100
            
            self.hambre = self.hambre + 10
            if self.hambre > 100:
                self.hambre = 100
            
            print(f"¡{self.nombre} ha jugado y está muy feliz!")
        else:
            print(f"{self.nombre} está muy cansado para jugar.")

    # Método 3: Entrenar al perro
    def entrenar(self):
        if self.energia >= 15 and self.hambre < 80:
            self.entrenamiento = self.entrenamiento + 8
            if self.entrenamiento > 100:
                self.entrenamiento = 100
            
            self.energia = self.energia - 15
            if self.energia < 0:
                self.energia = 0
            
            self.hambre = self.hambre + 5
            if self.hambre > 100:
                self.hambre = 100
            
            self.felicidad = self.felicidad + 3
            if self.felicidad > 100:
                self.felicidad = 100
            
            print(f"{self.nombre} ha completado una sesión de entrenamiento.")
        else:
            print(f"{self.nombre} necesita comer o descansar antes de entrenar.")

    # Método 4: Dormir/descansar
    def dormir(self):
        self.energia = self.energia + 40
        if self.energia > 100:
            self.energia = 100
        
        self.salud = self.salud + 5
        if self.salud > 100:
            self.salud = 100
        
        self.hambre = self.hambre + 5
        if self.hambre > 100:
            self.hambre = 100
        
        print(f"{self.nombre} ha descansado y recuperado energía.")

    # Método 5: Ir al veterinario
    def ir_veterinario(self):
        self.salud = self.salud + 25
        if self.salud > 100:
            self.salud = 100
        
        self.felicidad = self.felicidad - 10
        if self.felicidad < 0:
            self.felicidad = 0
        
        self.energia = self.energia - 10
        if self.energia < 0:
            self.energia = 0
        
        print(f"{self.nombre} ha visitado al veterinario. Su salud ha mejorado.")

    # Método 6: Pasear
    def pasear(self):
        if self.energia >= 10:
            self.energia = self.energia - 10
            if self.energia < 0:
                self.energia = 0
            
            self.felicidad = self.felicidad + 12
            if self.felicidad > 100:
                self.felicidad = 100
            
            self.salud = self.salud + 3
            if self.salud > 100:
                self.salud = 100
            
            self.hambre = self.hambre + 8
            if self.hambre > 100:
                self.hambre = 100
            
            print(f"¡{self.nombre} ha disfrutado del paseo!")
        else:
            print(f"{self.nombre} está muy cansado para pasear.")

    # Método 7: Bañar al perro
    def bañar(self):
        self.salud = self.salud + 8
        if self.salud > 100:
            self.salud = 100
        
        self.felicidad = self.felicidad - 5
        if self.felicidad < 0:
            self.felicidad = 0
        
        print(f"{self.nombre} ha sido bañado. Está limpio pero no muy contento.")

    # Método 8: Evaluar estado general
    def estado_general(self):
        print(f"\n=== ESTADO DE {self.nombre.upper()} ===")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Energía: {self.energia}/100")
        print(f"Hambre: {self.hambre}/100")
        print(f"Felicidad: {self.felicidad}/100")
        print(f"Salud: {self.salud}/100")
        print(f"Entrenamiento: {self.entrenamiento}/100")
        
        # Evaluar estado general
        if self.felicidad >= 80 and self.salud >= 80 and self.energia >= 50:
            print("Estado general: ¡EXCELENTE! 🐕")
        elif self.felicidad >= 60 and self.salud >= 60:
            print("Estado general: Bueno 🙂")
        elif self.hambre >= 80 or self.energia <= 20:
            print("Estado general: Necesita atención ⚠️")
        else:
            print("Estado general: Regular 😐")

    # Método 9: Simular paso del tiempo
    def pasar_tiempo(self):
        self.hambre = self.hambre + 10
        if self.hambre > 100:
            self.hambre = 100
        
        self.energia = self.energia - 5
        if self.energia < 0:
            self.energia = 0
        
        if self.hambre >= 90:
            self.felicidad = self.felicidad - 8
            if self.felicidad < 0:
                self.felicidad = 0
            
            self.salud = self.salud - 3
            if self.salud < 0:
                self.salud = 0
        
        print(f"Ha pasado tiempo... {self.nombre} tiene más hambre.")

    # Método 10: Trucos (depende del entrenamiento)
    def hacer_truco(self, truco):
        if self.entrenamiento >= 30 and self.energia >= 10:
            self.energia = self.energia - 10
            if self.energia < 0:
                self.energia = 0
            
            self.felicidad = self.felicidad + 8
            if self.felicidad > 100:
                self.felicidad = 100
            
            print(f"¡{self.nombre} ha realizado el truco '{truco}'! 🎉")
            return True
        elif self.entrenamiento < 30:
            print(f"{self.nombre} necesita más entrenamiento para hacer trucos.")
            return False
        else:
            print(f"{self.nombre} está muy cansado para hacer trucos.")
            return False

# Crear tres objetos de la clase Perro
if __name__ == "__main__":
    # Objeto 1: Perro joven y enérgico
    perro1 = Perro(
        nombre="Max",
        raza="Golden Retriever",
        edad=2,
        peso=25.5,
        color="dorado",
        energia=90,
        hambre=30,
        felicidad=85,
        salud=95,
        entrenamiento=40
    )
    
    # Objeto 2: Perro adulto bien entrenado
    perro2 = Perro(
        nombre="Luna",
        raza="Border Collie",
        edad=5,
        peso=18.0,
        color="negro y blanco",
        energia=75,
        hambre=50,
        felicidad=80,
        salud=90,
        entrenamiento=85
    )
    
    # Objeto 3: Cachorro que necesita cuidados
    perro3 = Perro(
        nombre="Rocky",
        raza="Bulldog Francés",
        edad=1,
        peso=8.5,
        color="atigrado",
        energia=60,
        hambre=80,
        felicidad=70,
        salud=85,
        entrenamiento=15
    )
    
    # Demostrar el uso de los objetos
    print("=== INFORMACIÓN DE LOS PERROS ===")
    perros = [perro1, perro2, perro3]
    
    for perro in perros:
        perro.estado_general()
        print()
    
    print("=== PROBANDO MÉTODOS ===")
    
    # Cuidar a Max (perro1)
    print(f"\n--- Cuidando a {perro1.nombre} ---")
    perro1.jugar()
    perro1.alimentar()
    perro1.entrenar()
    perro1.hacer_truco("sentado")
    
    # Cuidar a Luna (perro2)
    print(f"\n--- Cuidando a {perro2.nombre} ---")
    perro2.pasear()
    perro2.hacer_truco("dar la pata")
    perro2.hacer_truco("rodar")
    perro2.bañar()
    
    # Cuidar a Rocky (perro3)
    print(f"\n--- Cuidando a {perro3.nombre} ---")
    print("Rocky tiene mucha hambre, vamos a alimentarlo:")
    perro3.alimentar()
    perro3.alimentar()  # Segunda vez porque tenía mucha hambre
    perro3.entrenar()   # Intentar entrenar
    perro3.hacer_truco("sentado")  # Intentar truco
    perro3.dormir()     # Que descanse
    
    # Simular paso del tiempo para todos
    print(f"\n--- SIMULANDO PASO DEL TIEMPO ---")
    for perro in perros:
        perro.pasar_tiempo()
    
    # Estado final
    print(f"\n=== ESTADO FINAL DE LOS PERROS ===")
    for perro in perros:
        perro.estado_general()
        print()
    
    # Demostrar entrenamiento avanzado con Luna
    print(f"--- SESIÓN DE TRUCOS CON {perro2.nombre} ---")
    trucos = ["sentado", "quieto", "dar la pata", "rodar", "hacerse el muerto"]
    for truco in trucos:
        exito = perro2.hacer_truco(truco)
        if not exito:
            break
    
    print(f"\nEstado final de {perro2.nombre}:")
    perro2.estado_general()