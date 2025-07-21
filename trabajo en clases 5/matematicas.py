class Matematicas:
    def __init__(self, tema, dificultad, comprension, practica_horas, problemas_resueltos, problemas_correctos, confianza, velocidad_calculo, teoria_dominada, aplicacion_practica):
        self.tema = tema                           # tema matemático
        self.dificultad = dificultad               # dificultad del tema (0-100)
        self.comprension = comprension             # nivel de comprensión (0-100)
        self.practica_horas = practica_horas       # horas de práctica acumuladas
        self.problemas_resueltos = problemas_resueltos  # total de problemas resueltos
        self.problemas_correctos = problemas_correctos  # problemas resueltos correctamente
        self.confianza = confianza                 # confianza en el tema (0-100)
        self.velocidad_calculo = velocidad_calculo # velocidad de cálculo (0-100)
        self.teoria_dominada = teoria_dominada     # dominio teórico (0-100)
        self.aplicacion_practica = aplicacion_practica  # aplicación práctica (0-100)

    def estudiar_teoria(self, horas):
        if horas > 0:
            self.practica_horas = self.practica_horas + horas
            mejora = horas * 8
            self.teoria_dominada = self.teoria_dominada + mejora
            if self.teoria_dominada > 100:
                self.teoria_dominada = 100
            
            self.comprension = self.comprension + horas * 5
            if self.comprension > 100:
                self.comprension = 100
            
            print(f"Estudiaste teoría de {self.tema} por {horas} horas")
        else:
            print("Las horas deben ser mayor a 0")

    def resolver_problemas(self, cantidad, correctos):
        if cantidad > 0 and correctos >= 0 and correctos <= cantidad:
            self.problemas_resueltos = self.problemas_resueltos + cantidad
            self.problemas_correctos = self.problemas_correctos + correctos
            
            porcentaje_acierto = (correctos / cantidad) * 100
            
            if porcentaje_acierto >= 80:
                self.confianza = self.confianza + 10
                self.velocidad_calculo = self.velocidad_calculo + 8
                self.aplicacion_practica = self.aplicacion_practica + 6
            elif porcentaje_acierto >= 60:
                self.confianza = self.confianza + 5
                self.velocidad_calculo = self.velocidad_calculo + 4
                self.aplicacion_practica = self.aplicacion_practica + 3
            else:
                self.confianza = self.confianza - 3
                if self.confianza < 0:
                    self.confianza = 0
            
            if self.confianza > 100:
                self.confianza = 100
            if self.velocidad_calculo > 100:
                self.velocidad_calculo = 100
            if self.aplicacion_practica > 100:
                self.aplicacion_practica = 100
            
            print(f"Resolviste {cantidad} problemas, {correctos} correctos ({porcentaje_acierto:.1f}%)")
        else:
            print("Cantidad o correctos inválidos")

    def evaluar_dominio(self):
        if self.problemas_resueltos > 0:
            precision = (self.problemas_correctos / self.problemas_resueltos) * 100
        else:
            precision = 0
        
        puntuacion_total = (self.comprension + self.confianza + self.velocidad_calculo + 
                           self.teoria_dominada + self.aplicacion_practica + precision) / 6
        
        if puntuacion_total >= 85:
            nivel = "Experto"
        elif puntuacion_total >= 70:
            nivel = "Avanzado"
        elif puntuacion_total >= 55:
            nivel = "Intermedio"
        elif puntuacion_total >= 40:
            nivel = "Básico"
        else:
            nivel = "Principiante"
        
        print(f"{self.tema}: Nivel {nivel} ({puntuacion_total:.1f}/100)")
        print(f"  Precisión: {precision:.1f}% | Horas práctica: {self.practica_horas}")

if __name__ == "__main__":
    algebra = Matematicas("Álgebra", 60, 45, 20, 50, 35, 40, 55, 50, 30)
    calculo = Matematicas("Cálculo", 85, 25, 5, 15, 8, 20, 30, 35, 15)
    geometria = Matematicas("Geometría", 40, 70, 30, 80, 70, 75, 80, 85, 65)
    
    print("=== PROGRESO EN MATEMÁTICAS ===")
    materias = [algebra, calculo, geometria]
    
    print("\n--- 1. EVALUACIÓN INICIAL ---")
    for materia in materias:
        materia.evaluar_dominio()
    
    print("\n--- 2. ESTUDIANDO TEORÍA ---")
    algebra.estudiar_teoria(5)
    calculo.estudiar_teoria(8)
    geometria.estudiar_teoria(3)
    
    print("\n--- 3. RESOLVIENDO PROBLEMAS ---")
    algebra.resolver_problemas(20, 16)
    calculo.resolver_problemas(10, 6)
    geometria.resolver_problemas(15, 14)
    
    print("\n--- PROGRESO FINAL ---")
    for materia in materias:
        materia.evaluar_dominio()
