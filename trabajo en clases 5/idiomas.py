class Idiomas:
    def __init__(self, idioma, nivel_actual, comprension, expresion_oral, escritura, lectura, vocabulario, gramatica, fluidez, confianza):
        self.idioma = idioma                   # nombre del idioma
        self.nivel_actual = nivel_actual       # nivel: básico, intermedio, avanzado
        self.comprension = comprension         # comprensión auditiva (0-100)
        self.expresion_oral = expresion_oral   # expresión oral (0-100)
        self.escritura = escritura             # habilidad de escritura (0-100)
        self.lectura = lectura                 # comprensión de lectura (0-100)
        self.vocabulario = vocabulario         # nivel de vocabulario (0-100)
        self.gramatica = gramatica             # conocimiento gramatical (0-100)
        self.fluidez = fluidez                 # fluidez al hablar (0-100)
        self.confianza = confianza             # confianza al usar el idioma (0-100)

    def estudiar(self, horas, tipo_estudio):
        if horas > 0:
            mejora_base = horas * 2  # 2 puntos por hora
            
            if tipo_estudio == "vocabulario":
                self.vocabulario = self.vocabulario + mejora_base
                self.lectura = self.lectura + mejora_base * 0.5
            elif tipo_estudio == "gramatica":
                self.gramatica = self.gramatica + mejora_base
                self.escritura = self.escritura + mejora_base * 0.7
            elif tipo_estudio == "conversacion":
                self.expresion_oral = self.expresion_oral + mejora_base
                self.fluidez = self.fluidez + mejora_base * 0.8
                self.confianza = self.confianza + mejora_base * 0.6
            elif tipo_estudio == "escucha":
                self.comprension = self.comprension + mejora_base
                self.vocabulario = self.vocabulario + mejora_base * 0.3
            
            # Aplicar límites
            for attr in ['comprension', 'expresion_oral', 'escritura', 'lectura', 'vocabulario', 'gramatica', 'fluidez', 'confianza']:
                valor = getattr(self, attr)
                if valor > 100:
                    setattr(self, attr, 100)
            
            print(f"Estudiaste {tipo_estudio} en {self.idioma} por {horas} horas")
        else:
            print("Las horas deben ser mayor a 0")

    def practicar_conversacion(self, duracion_minutos):
        if duracion_minutos > 0:
            mejora = duracion_minutos / 10  # mejora según minutos
            self.expresion_oral = self.expresion_oral + mejora
            self.fluidez = self.fluidez + mejora * 1.2
            self.confianza = self.confianza + mejora * 0.8
            
            # Aplicar límites
            if self.expresion_oral > 100:
                self.expresion_oral = 100
            if self.fluidez > 100:
                self.fluidez = 100
            if self.confianza > 100:
                self.confianza = 100
            
            print(f"Practicaste conversación en {self.idioma} por {duracion_minutos} minutos")
        else:
            print("La duración debe ser mayor a 0")

    def evaluar_nivel(self):
        puntuacion_total = (self.comprension + self.expresion_oral + self.escritura + 
                           self.lectura + self.vocabulario + self.gramatica + 
                           self.fluidez + self.confianza) / 8
        
        if puntuacion_total >= 80:
            nivel = "Avanzado"
        elif puntuacion_total >= 60:
            nivel = "Intermedio Alto"
        elif puntuacion_total >= 40:
            nivel = "Intermedio"
        elif puntuacion_total >= 20:
            nivel = "Básico"
        else:
            nivel = "Principiante"
        
        print(f"{self.idioma}: Nivel {nivel} ({puntuacion_total:.1f}/100)")
        print(f"  Oral: {self.expresion_oral}/100 | Comprensión: {self.comprension}/100")

if __name__ == "__main__":
    # Objeto 1: Inglés intermedio
    ingles = Idiomas("Inglés", "intermedio", 65, 50, 45, 70, 60, 55, 40, 35)
    
    # Objeto 2: Francés básico
    frances = Idiomas("Francés", "básico", 25, 15, 20, 30, 20, 25, 10, 15)
    
    # Objeto 3: Italiano principiante
    italiano = Idiomas("Italiano", "principiante", 10, 5, 8, 15, 12, 10, 5, 8)
    
    # Probando 3 métodos principales
    print("=== APRENDIENDO IDIOMAS ===")
    idiomas = [ingles, frances, italiano]
    
    # Método 1: Evaluar nivel inicial
    print("\n--- 1. NIVEL INICIAL ---")
    for idioma in idiomas:
        idioma.evaluar_nivel()
    
    # Método 2: Estudiar diferentes aspectos
    print("\n--- 2. ESTUDIANDO ---")
    ingles.estudiar(3, "conversacion")
    frances.estudiar(2, "vocabulario")
    italiano.estudiar(4, "gramatica")
    
    # Método 3: Practicar conversación
    print("\n--- 3. PRACTICANDO CONVERSACIÓN ---")
    ingles.practicar_conversacion(45)
    frances.practicar_conversacion(20)
    italiano.practicar_conversacion(15)
    
    # Evaluación final
    print("\n--- PROGRESO ALCANZADO ---")
    for idioma in idiomas:
        idioma.evaluar_nivel()
