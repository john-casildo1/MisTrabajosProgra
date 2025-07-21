class SaludMental:
    def __init__(self, bienestar_general, estres, ansiedad, autoestima, motivacion, energia_mental, equilibrio_emocional, relaciones_sociales, proposito_vida, horas_sueno):
        self.bienestar_general = bienestar_general     # bienestar general (0-100)
        self.estres = estres                           # nivel de estrés (0-100, 100=muy estresado)
        self.ansiedad = ansiedad                       # nivel de ansiedad (0-100)
        self.autoestima = autoestima                   # nivel de autoestima (0-100)
        self.motivacion = motivacion                   # nivel de motivación (0-100)
        self.energia_mental = energia_mental           # energía mental (0-100)
        self.equilibrio_emocional = equilibrio_emocional # equilibrio emocional (0-100)
        self.relaciones_sociales = relaciones_sociales # calidad relaciones (0-100)
        self.proposito_vida = proposito_vida           # sentido de propósito (0-100)
        self.horas_sueno = horas_sueno                 # horas de sueño promedio

    def meditar(self, minutos):
        if minutos > 0:
            mejora = minutos / 5  # mejora según minutos de meditación
            self.estres = self.estres - mejora
            if self.estres < 0:
                self.estres = 0
            
            self.ansiedad = self.ansiedad - mejora * 0.8
            if self.ansiedad < 0:
                self.ansiedad = 0
            
            self.equilibrio_emocional = self.equilibrio_emocional + mejora * 1.2
            if self.equilibrio_emocional > 100:
                self.equilibrio_emocional = 100
            
            print(f"Meditaste {minutos} minutos. Estrés y ansiedad reducidos")
        else:
            print("Los minutos deben ser mayor a 0")

    def ejercitarse(self, intensidad):
        if intensidad > 0:
            if intensidad <= 50:  # ejercicio suave
                self.energia_mental = self.energia_mental + 10
                self.motivacion = self.motivacion + 8
                self.estres = self.estres - 5
            else:  # ejercicio intenso
                self.energia_mental = self.energia_mental + 15
                self.motivacion = self.motivacion + 12
                self.estres = self.estres - 10
                self.autoestima = self.autoestima + 5
            
            # Aplicar límites
            if self.energia_mental > 100:
                self.energia_mental = 100
            if self.motivacion > 100:
                self.motivacion = 100
            if self.autoestima > 100:
                self.autoestima = 100
            if self.estres < 0:
                self.estres = 0
            
            print(f"Ejercicio de intensidad {intensidad}/100 completado")
        else:
            print("La intensidad debe ser mayor a 0")

    def evaluar_salud_mental(self):
        # Calcular puntuación considerando factores negativos
        factores_positivos = (self.bienestar_general + self.autoestima + self.motivacion + 
                             self.energia_mental + self.equilibrio_emocional + 
                             self.relaciones_sociales + self.proposito_vida) / 7
        
        factores_negativos = (self.estres + self.ansiedad) / 2
        puntuacion_final = factores_positivos - (factores_negativos * 0.3)
        
        if puntuacion_final >= 80:
            estado = "Excelente salud mental"
        elif puntuacion_final >= 65:
            estado = "Buena salud mental"
        elif puntuacion_final >= 50:
            estado = "Salud mental estable"
        elif puntuacion_final >= 35:
            estado = "Necesita atención"
        else:
            estado = "Requiere ayuda profesional"
        
        print(f"Estado: {estado} ({puntuacion_final:.1f}/100)")
        print(f"  Estrés: {self.estres}/100 | Bienestar: {self.bienestar_general}/100")

if __name__ == "__main__":
    # Objeto 1: Persona con buen equilibrio
    persona1 = SaludMental(75, 30, 20, 80, 85, 70, 75, 85, 80, 8)
    
    # Objeto 2: Persona con estrés moderado
    persona2 = SaludMental(60, 65, 55, 60, 50, 45, 55, 70, 65, 6)
    
    # Objeto 3: Persona que necesita cuidados
    persona3 = SaludMental(40, 85, 80, 35, 25, 30, 35, 45, 40, 4)
    
    # Probando 3 métodos principales
    print("=== CUIDANDO LA SALUD MENTAL ===")
    personas = [persona1, persona2, persona3]
    
    # Método 1: Evaluar estado inicial
    print("\n--- 1. EVALUACIÓN INICIAL ---")
    for i, persona in enumerate(personas, 1):
        print(f"Persona {i}:")
        persona.evaluar_salud_mental()
    
    # Método 2: Practicar meditación
    print("\n--- 2. SESIONES DE MEDITACIÓN ---")
    persona1.meditar(15)  # 15 minutos
    persona2.meditar(25)  # 25 minutos
    persona3.meditar(30)  # 30 minutos
    
    # Método 3: Hacer ejercicio
    print("\n--- 3. ACTIVIDAD FÍSICA ---")
    persona1.ejercitarse(70)  # ejercicio intenso
    persona2.ejercitarse(50)  # ejercicio moderado
    persona3.ejercitarse(30)  # ejercicio suave
    
    # Evaluación final
    print("\n--- EVALUACIÓN DESPUÉS DEL CUIDADO ---")
    for i, persona in enumerate(personas, 1):
        print(f"Persona {i}:")
        persona.evaluar_salud_mental()
