class TiempoLibre:
    def __init__(self, actividad, duracion, costo, energia_requerida, diversion, social, ubicacion, equipamiento, clima_dependiente, nivel_habilidad):
        self.actividad = actividad               # nombre de la actividad
        self.duracion = duracion                 # duración en horas
        self.costo = costo                      # costo en colones
        self.energia_requerida = energia_requerida  # energía necesaria (0-100)
        self.diversion = diversion              # nivel de diversión (0-100)
        self.social = social                    # es actividad social: True/False
        self.ubicacion = ubicacion              # lugar donde se realiza
        self.equipamiento = equipamiento        # necesita equipo especial: True/False
        self.clima_dependiente = clima_dependiente  # depende del clima: True/False
        self.nivel_habilidad = nivel_habilidad  # nivel de habilidad requerido (0-100)

    def realizar_actividad(self, energia_actual):
        if energia_actual >= self.energia_requerida:
            energia_gastada = self.energia_requerida
            diversion_obtenida = self.diversion
            print(f"¡Realizaste {self.actividad}! Diversión: {diversion_obtenida}/100")
            return energia_gastada
        else:
            print(f"No tienes suficiente energía para {self.actividad}")
            return 0

    def calcular_presupuesto(self, veces):
        costo_total = self.costo * veces
        print(f"Hacer {self.actividad} {veces} veces costará: ¢{costo_total:,}")
        return costo_total

    def evaluar_dificultad(self):
        if self.nivel_habilidad <= 30:
            dificultad = "Fácil"
        elif self.nivel_habilidad <= 70:
            dificultad = "Intermedio"
        else:
            dificultad = "Difícil"
        print(f"{self.actividad}: {dificultad} ({self.nivel_habilidad}/100)")

if __name__ == "__main__":
    # Objeto 1: Actividad relajante
    actividad1 = TiempoLibre(
        actividad="Leer un libro",
        duracion=2,
        costo=0,
        energia_requerida=10,
        diversion=70,
        social=False,
        ubicacion="casa",
        equipamiento=False,
        clima_dependiente=False,
        nivel_habilidad=20
    )
    
    # Objeto 2: Actividad deportiva
    actividad2 = TiempoLibre(
        actividad="Jugar fútbol",
        duracion=1.5,
        costo=5000,
        energia_requerida=80,
        diversion=90,
        social=True,
        ubicacion="cancha",
        equipamiento=True,
        clima_dependiente=True,
        nivel_habilidad=60
    )
    
    # Objeto 3: Actividad creativa
    actividad3 = TiempoLibre(
        actividad="Pintar cuadros",
        duracion=3,
        costo=15000,
        energia_requerida=40,
        diversion=85,
        social=False,
        ubicacion="estudio",
        equipamiento=True,
        clima_dependiente=False,
        nivel_habilidad=75
    )
    
    # Probando 3 métodos principales
    print("=== ACTIVIDADES DE TIEMPO LIBRE ===")
    actividades = [actividad1, actividad2, actividad3]
    
    # Método 1: Evaluar dificultad
    print("\n--- 1. EVALUANDO DIFICULTAD ---")
    for act in actividades:
        act.evaluar_dificultad()
    
    # Método 2: Realizar actividades
    print("\n--- 2. REALIZANDO ACTIVIDADES ---")
    energia_disponible = 85
    for act in actividades:
        energia_gastada = act.realizar_actividad(energia_disponible)
        energia_disponible = energia_disponible - energia_gastada
        if energia_disponible < 0:
            energia_disponible = 0
    
    # Método 3: Calcular presupuestos
    print("\n--- 3. CALCULANDO PRESUPUESTOS ---")
    for act in actividades:
        act.calcular_presupuesto(4)  # 4 veces por mes