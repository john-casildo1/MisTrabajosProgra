class Vacaciones:
    def __init__(self, destino, duracion, presupuesto, gastos_actuales, relajacion, diversión, cultura, aventura, clima, acompañantes):
        self.destino = destino                 # lugar de vacaciones
        self.duracion = duracion               # duración en días
        self.presupuesto = presupuesto         # presupuesto total en colones
        self.gastos_actuales = gastos_actuales # gastos acumulados
        self.relajacion = relajacion           # nivel de relajación (0-100)
        self.diversión = diversión             # nivel de diversión (0-100)
        self.cultura = cultura                 # experiencia cultural (0-100)
        self.aventura = aventura               # nivel de aventura (0-100)
        self.clima = clima                     # calidad del clima (0-100)
        self.acompañantes = acompañantes       # número de acompañantes

    def realizar_actividad(self, tipo_actividad, costo):
        if self.gastos_actuales + costo <= self.presupuesto:
            self.gastos_actuales = self.gastos_actuales + costo
            
            if tipo_actividad == "playa":
                self.relajacion = self.relajacion + 20
                self.diversión = self.diversión + 15
            elif tipo_actividad == "museo":
                self.cultura = self.cultura + 25
                self.relajacion = self.relajacion + 10
            elif tipo_actividad == "aventura":
                self.aventura = self.aventura + 30
                self.diversión = self.diversión + 20
            elif tipo_actividad == "spa":
                self.relajacion = self.relajacion + 35
            
            # Aplicar límites
            for attr in ['relajacion', 'diversión', 'cultura', 'aventura']:
                valor = getattr(self, attr)
                if valor > 100:
                    setattr(self, attr, 100)
            
            print(f"Actividad '{tipo_actividad}' realizada en {self.destino}. Costo: ¢{costo:,}")
        else:
            print(f"No hay presupuesto suficiente para '{tipo_actividad}'")

    def evaluar_presupuesto(self):
        restante = self.presupuesto - self.gastos_actuales
        porcentaje_usado = (self.gastos_actuales / self.presupuesto) * 100
        
        if porcentaje_usado <= 50:
            estado = "Presupuesto holgado"
        elif porcentaje_usado <= 80:
            estado = "Presupuesto controlado"
        elif porcentaje_usado <= 100:
            estado = "Presupuesto ajustado"
        else:
            estado = "Presupuesto excedido"
        
        print(f"Presupuesto en {self.destino}: {estado}")
        print(f"  Gastado: ¢{self.gastos_actuales:,} | Restante: ¢{restante:,}")

    def evaluar_experiencia(self):
        puntuacion = (self.relajacion + self.diversión + self.cultura + self.aventura) / 4
        
        if puntuacion >= 80:
            calidad = "Vacaciones increíbles"
        elif puntuacion >= 65:
            calidad = "Muy buenas vacaciones"
        elif puntuacion >= 50:
            calidad = "Vacaciones agradables"
        else:
            calidad = "Vacaciones regulares"
        
        print(f"Vacaciones en {self.destino}: {calidad} ({puntuacion:.1f}/100)")
        print(f"  Relajación: {self.relajacion}/100 | Diversión: {self.diversión}/100")

if __name__ == "__main__":
    # Objeto 1: Vacaciones de playa relajantes
    vacaciones1 = Vacaciones("Guanacaste", 7, 500000, 0, 30, 40, 20, 25, 85, 2)
    
    # Objeto 2: Viaje cultural europeo
    vacaciones2 = Vacaciones("París", 10, 1200000, 0, 20, 35, 60, 30, 70, 1)
    
    # Objeto 3: Aventura en montaña
    vacaciones3 = Vacaciones("Monteverde", 5, 300000, 0, 25, 30, 40, 70, 75, 3)
    
    # Probando 3 métodos principales
    print("=== DISFRUTANDO VACACIONES ===")
    vacaciones = [vacaciones1, vacaciones2, vacaciones3]
    
    # Método 1: Evaluar experiencia inicial
    print("\n--- 1. INICIO DE VACACIONES ---")
    for viaje in vacaciones:
        viaje.evaluar_experiencia()
    
    # Método 2: Realizar actividades según destino
    print("\n--- 2. REALIZANDO ACTIVIDADES ---")
    vacaciones1.realizar_actividad("playa", 50000)
    vacaciones1.realizar_actividad("spa", 80000)
    
    vacaciones2.realizar_actividad("museo", 40000)
    vacaciones2.realizar_actividad("cultura", 100000)
    
    vacaciones3.realizar_actividad("aventura", 75000)
    vacaciones3.realizar_actividad("aventura", 60000)
    
    # Método 3: Evaluar presupuestos
    print("\n--- 3. EVALUANDO PRESUPUESTOS ---")
    for viaje in vacaciones:
        viaje.evaluar_presupuesto()
    
    # Evaluación final
    print("\n--- EXPERIENCIA FINAL ---")
    for viaje in vacaciones:
        viaje.evaluar_experiencia()
