class Tareas:
    def __init__(self, nombre, descripcion, prioridad, dificultad, tiempo_estimado, progreso, fecha_limite, categoria, recursos_necesarios, completada):
        self.nombre = nombre                         # nombre de la tarea
        self.descripcion = descripcion               # descripción detallada
        self.prioridad = prioridad                   # prioridad (0-100, 100=muy urgente)
        self.dificultad = dificultad                 # dificultad (0-100)
        self.tiempo_estimado = tiempo_estimado       # tiempo estimado en horas
        self.progreso = progreso                     # progreso actual (0-100)
        self.fecha_limite = fecha_limite             # días restantes para entrega
        self.categoria = categoria                   # tipo: trabajo, estudio, personal
        self.recursos_necesarios = recursos_necesarios  # recursos que necesita (0-100)
        self.completada = completada                 # está completada: True/False

    def trabajar_en_tarea(self, horas_trabajadas):
        if not self.completada and horas_trabajadas > 0:
            progreso_ganado = (horas_trabajadas / self.tiempo_estimado) * 100
            self.progreso = self.progreso + progreso_ganado
            if self.progreso >= 100:
                self.progreso = 100
                self.completada = True
                print(f"¡Tarea '{self.nombre}' completada!")
            else:
                print(f"Trabajaste {horas_trabajadas}h en '{self.nombre}'. Progreso: {self.progreso:.1f}%")
        elif self.completada:
            print(f"La tarea '{self.nombre}' ya está completada")
        else:
            print("Las horas trabajadas deben ser mayor a 0")

    def extender_fecha_limite(self, dias_extra):
        if dias_extra > 0:
            self.fecha_limite = self.fecha_limite + dias_extra
            self.prioridad = self.prioridad - 10  # reduce urgencia
            if self.prioridad < 0:
                self.prioridad = 0
            print(f"Fecha límite extendida {dias_extra} días para '{self.nombre}'")
        else:
            print("Los días extra deben ser mayor a 0")

    def evaluar_urgencia(self):
        urgencia_tiempo = 100 - (self.fecha_limite * 10)  # menos días = más urgente
        if urgencia_tiempo < 0:
            urgencia_tiempo = 0
        if urgencia_tiempo > 100:
            urgencia_tiempo = 100
        
        urgencia_final = (self.prioridad + urgencia_tiempo) / 2
        
        if urgencia_final >= 80:
            nivel = "MUY URGENTE"
        elif urgencia_final >= 60:
            nivel = "Urgente"
        elif urgencia_final >= 40:
            nivel = "Moderada"
        else:
            nivel = "Baja prioridad"
        
        estado = "✅ Completada" if self.completada else f"🔄 {self.progreso:.0f}% completada"
        print(f"'{self.nombre}' ({self.categoria}): {nivel} - {estado}")
        print(f"  Días restantes: {self.fecha_limite} | Dificultad: {self.dificultad}/100")

if __name__ == "__main__":
    # Objeto 1: Tarea urgente de trabajo
    tarea1 = Tareas("Presentación cliente", "Crear presentación para cliente importante", 
                    90, 70, 8, 20, 2, "trabajo", 80, False)
    
    # Objeto 2: Tarea de estudio a mediano plazo
    tarea2 = Tareas("Proyecto programación", "Desarrollar aplicación web en Python", 
                    60, 85, 20, 0, 7, "estudio", 90, False)
    
    # Objeto 3: Tarea personal simple
    tarea3 = Tareas("Organizar cuarto", "Limpiar y organizar habitación", 
                    30, 20, 3, 50, 5, "personal", 10, False)
    
    # Probando 3 métodos principales
    print("=== GESTIONANDO TAREAS ===")
    tareas = [tarea1, tarea2, tarea3]
    
    # Método 1: Evaluar urgencia inicial
    print("\n--- 1. EVALUACIÓN INICIAL ---")
    for tarea in tareas:
        tarea.evaluar_urgencia()
    
    # Método 2: Trabajar en las tareas
    print("\n--- 2. TRABAJANDO EN TAREAS ---")
    tarea1.trabajar_en_tarea(6)   # 6 horas en presentación
    tarea2.trabajar_en_tarea(4)   # 4 horas en proyecto
    tarea3.trabajar_en_tarea(2)   # 2 horas organizando
    
    # Método 3: Gestionar fechas límite
    print("\n--- 3. GESTIONANDO FECHAS ---")
    tarea1.trabajar_en_tarea(3)   # Terminar presentación
    tarea2.extender_fecha_limite(3)  # Extender proyecto
    tarea3.trabajar_en_tarea(1)   # Terminar organización
    
    # Evaluación final
    print("\n--- EVALUACIÓN FINAL ---")
    for tarea in tareas:
        tarea.evaluar_urgencia()
