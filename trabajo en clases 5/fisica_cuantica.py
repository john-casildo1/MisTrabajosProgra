class FisicaCuantica:
    def __init__(self, particula, posicion, momentum, energia, spin, entrelazamiento, superposicion, coherencia, decoherencia, probabilidad_deteccion):
        self.particula = particula                       # tipo de partícula
        self.posicion = posicion                         # posición en nm
        self.momentum = momentum                         # momentum en unidades cuánticas
        self.energia = energia                           # energía en eV
        self.spin = spin                                 # spin cuántico
        self.entrelazamiento = entrelazamiento           # nivel de entrelazamiento (0-100)
        self.superposicion = superposicion               # estado de superposición (0-100)
        self.coherencia = coherencia                     # coherencia cuántica (0-100)
        self.decoherencia = decoherencia                 # nivel de decoherencia (0-100)
        self.probabilidad_deteccion = probabilidad_deteccion # probabilidad de detección (0-100)

    def medir_particula(self):
        # El acto de medir colapsa la función de onda
        if self.superposicion > 0:
            self.superposicion = 0  # colapso de la superposición
            self.decoherencia = self.decoherencia + 30
            if self.decoherencia > 100:
                self.decoherencia = 100
            
            self.coherencia = self.coherencia - 25
            if self.coherencia < 0:
                self.coherencia = 0
            
            # La posición se vuelve definida
            import random
            self.posicion = random.uniform(0, 100)
            print(f"Medición realizada en {self.particula}. Posición colapsada a {self.posicion:.2f} nm")
        else:
            print(f"La {self.particula} ya está en estado clásico")

    def entrelazar_con(self, otra_particula):
        if isinstance(otra_particula, FisicaCuantica):
            # Crear entrelazamiento cuántico
            entrelazamiento_nuevo = (self.entrelazamiento + otra_particula.entrelazamiento) / 2 + 20
            
            if entrelazamiento_nuevo > 100:
                entrelazamiento_nuevo = 100
            
            self.entrelazamiento = entrelazamiento_nuevo
            otra_particula.entrelazamiento = entrelazamiento_nuevo
            
            # El entrelazamiento reduce la superposición individual
            self.superposicion = self.superposicion - 10
            otra_particula.superposicion = otra_particula.superposicion - 10
            
            if self.superposicion < 0:
                self.superposicion = 0
            if otra_particula.superposicion < 0:
                otra_particula.superposicion = 0
            
            print(f"{self.particula} y {otra_particula.particula} ahora están entrelazadas")
        else:
            print("Solo se puede entrelazar con otra partícula cuántica")

    def evaluar_estado_cuantico(self):
        cuanticidad = (self.superposicion + self.coherencia + self.entrelazamiento - self.decoherencia) / 3
        
        if cuanticidad >= 70:
            estado = "Altamente cuántico"
        elif cuanticidad >= 50:
            estado = "Cuántico estable"
        elif cuanticidad >= 30:
            estado = "Parcialmente cuántico"
        elif cuanticidad >= 0:
            estado = "Transición cuántica-clásica"
        else:
            estado = "Estado clásico"
        
        print(f"{self.particula}: {estado} ({cuanticidad:.1f}/100)")
        print(f"  Superposición: {self.superposicion}/100 | Entrelazamiento: {self.entrelazamiento}/100")

if __name__ == "__main__":
    # Objeto 1: Electrón en superposición
    electron = FisicaCuantica("Electrón", 50.5, 12.3, 2.1, 0.5, 20, 85, 90, 15, 75)
    
    # Objeto 2: Fotón coherente
    foton = FisicaCuantica("Fotón", 75.2, 8.7, 1.8, 1, 10, 70, 95, 10, 90)
    
    # Objeto 3: Átomo en estado mixto
    atomo = FisicaCuantica("Átomo", 25.8, 15.6, 5.2, 0, 5, 40, 60, 45, 65)
    
    # Probando 3 métodos principales
    print("=== EXPERIMENTOS DE FÍSICA CUÁNTICA ===")
    particulas = [electron, foton, atomo]
    
    # Método 1: Evaluar estado cuántico inicial
    print("\n--- 1. ESTADO CUÁNTICO INICIAL ---")
    for particula in particulas:
        particula.evaluar_estado_cuantico()
    
    # Método 2: Entrelazar partículas
    print("\n--- 2. CREANDO ENTRELAZAMIENTO ---")
    electron.entrelazar_con(foton)
    foton.entrelazar_con(atomo)
    
    # Método 3: Realizar mediciones
    print("\n--- 3. REALIZANDO MEDICIONES ---")
    electron.medir_particula()
    foton.medir_particula()
    atomo.medir_particula()
    
    # Evaluación final
    print("\n--- ESTADO DESPUÉS DE EXPERIMENTOS ---")
    for particula in particulas:
        particula.evaluar_estado_cuantico()
