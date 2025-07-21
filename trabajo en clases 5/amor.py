class Amor:
    def __init__(self, nombre_pareja, tiempo_relacion, confianza, comunicacion, pasion, compatibilidad, respeto, apoyo, felicidad, compromiso):
        self.nombre_pareja = nombre_pareja       # nombre de la pareja
        self.tiempo_relacion = tiempo_relacion   # tiempo juntos en meses
        self.confianza = confianza               # nivel de confianza (0-100)
        self.comunicacion = comunicacion         # nivel de comunicación (0-100)
        self.pasion = pasion                     # nivel de pasión (0-100)
        self.compatibilidad = compatibilidad     # nivel de compatibilidad (0-100)
        self.respeto = respeto                   # nivel de respeto (0-100)
        self.apoyo = apoyo                       # nivel de apoyo mutuo (0-100)
        self.felicidad = felicidad               # nivel de felicidad (0-100)
        self.compromiso = compromiso             # nivel de compromiso (0-100)

    def pasar_tiempo_juntos(self, calidad_tiempo):
        if calidad_tiempo > 0:
            self.tiempo_relacion = self.tiempo_relacion + 1
            if calidad_tiempo >= 80:  # tiempo de alta calidad
                self.felicidad = self.felicidad + 8
                self.comunicacion = self.comunicacion + 5
                self.confianza = self.confianza + 3
            elif calidad_tiempo >= 50:  # tiempo regular
                self.felicidad = self.felicidad + 4
                self.comunicacion = self.comunicacion + 2
            else:  # tiempo de baja calidad
                self.felicidad = self.felicidad - 2
            if self.felicidad > 100:
                self.felicidad = 100
            if self.felicidad < 0:
                self.felicidad = 0
            print(f"Mes {self.tiempo_relacion} con {self.nombre_pareja}")
        else:
            print("La calidad del tiempo debe ser mayor a 0")

    def resolver_conflicto(self, metodo_resolucion):
        if metodo_resolucion == "dialogo":
            self.comunicacion = self.comunicacion + 10
            self.confianza = self.confianza + 8
            self.respeto = self.respeto + 5
            print("Conflicto resuelto mediante diálogo constructivo")
        elif metodo_resolucion == "compromiso":
            self.compatibilidad = self.compatibilidad + 8
            self.apoyo = self.apoyo + 6
            print("Conflicto resuelto llegando a un compromiso")
        else:  # método inadecuado
            self.confianza = self.confianza - 10
            self.comunicacion = self.comunicacion - 8
            self.felicidad = self.felicidad - 12
            print("Conflicto mal resuelto, afectó la relación")
        # Aplicar límites
        for attr in ['comunicacion', 'confianza', 'respeto', 'compatibilidad', 'apoyo', 'felicidad']:
            valor = getattr(self, attr)
            if valor > 100:
                setattr(self, attr, 100)
            elif valor < 0:
                setattr(self, attr, 0)

    def evaluar_relacion(self):
        puntuacion = (self.confianza + self.comunicacion + self.felicidad + self.respeto + self.apoyo) / 5
        if puntuacion >= 85:
            estado = "Relación sólida y saludable"
        elif puntuacion >= 70:
            estado = "Buena relación"
        elif puntuacion >= 50:
            estado = "Relación con potencial"
        else:
            estado = "Relación necesita trabajo"
        print(f"Relación con {self.nombre_pareja}: {estado} ({puntuacion:.1f}/100)")
        print(f"  Felicidad: {self.felicidad}/100 | Confianza: {self.confianza}/100")

if __name__ == "__main__":
    # Objeto 1: Relación nueva y prometedora
    amor1 = Amor("María", 6, 75, 80, 90, 85, 88, 70, 85, 60)
    
    # Objeto 2: Relación madura y estable
    amor2 = Amor("Carlos", 36, 95, 90, 70, 90, 95, 92, 88, 95)
    
    # Objeto 3: Relación con dificultades
    amor3 = Amor("Ana", 18, 45, 40, 60, 55, 50, 45, 40, 50)
    
    # Probando 3 métodos principales
    print("=== EVALUANDO RELACIONES ===")
    relaciones = [amor1, amor2, amor3]
    
    # Método 1: Evaluar estado inicial
    print("\n--- 1. ESTADO INICIAL ---")
    for relacion in relaciones:
        relacion.evaluar_relacion()
    
    # Método 2: Pasar tiempo de calidad
    print("\n--- 2. PASANDO TIEMPO JUNTOS ---")
    amor1.pasar_tiempo_juntos(85)  # alta calidad
    amor2.pasar_tiempo_juntos(75)  # buena calidad
    amor3.pasar_tiempo_juntos(30)  # baja calidad
    
    # Método 3: Resolver conflictos
    print("\n--- 3. RESOLVIENDO CONFLICTOS ---")
    amor1.resolver_conflicto("dialogo")
    amor2.resolver_conflicto("compromiso")
    amor3.resolver_conflicto("evitar")  # método inadecuado
    
    # Evaluación final
    print("\n--- EVALUACIÓN FINAL ---")
    for relacion in relaciones:
        relacion.evaluar_relacion()
