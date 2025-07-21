class Silla:
    def __init__(self, material, color, altura, peso, precio, comodidad, durabilidad, limpieza, estilo, horas_uso):
        self.material = material         # material: madera, metal, plástico
        self.color = color              # color de la silla
        self.altura = altura            # altura en cm
        self.peso = peso               # peso en kg
        self.precio = precio           # precio en colones
        self.comodidad = comodidad     # nivel de comodidad (0-100)
        self.durabilidad = durabilidad # nivel de durabilidad (0-100)
        self.limpieza = limpieza       # nivel de limpieza (0-100)
        self.estilo = estilo           # estilo: moderna, clásica, ergonómica
        self.horas_uso = horas_uso     # horas de uso acumuladas

    def usar(self, horas):
        if horas > 0:
            self.horas_uso = self.horas_uso + horas
            desgaste = horas * 0.2
            self.durabilidad = self.durabilidad - desgaste
            if self.durabilidad < 0:
                self.durabilidad = 0
            self.limpieza = self.limpieza - horas * 0.5
            if self.limpieza < 0:
                self.limpieza = 0
            if self.comodidad > 10:
                self.comodidad = self.comodidad - horas * 0.1
                if self.comodidad < 0:
                    self.comodidad = 0
            print(f"Usaste la silla {horas} horas. Total: {self.horas_uso} horas")
        else:
            print("Las horas deben ser mayor a 0")

    def limpiar(self):
        if self.limpieza < 100:
            self.limpieza = self.limpieza + 50
            if self.limpieza > 100:
                self.limpieza = 100
            self.comodidad = self.comodidad + 3
            if self.comodidad > 100:
                self.comodidad = 100
            print(f"Silla {self.color} de {self.material} ha sido limpiada")
        else:
            print("La silla ya está completamente limpia")

    def evaluar_calidad(self):
        puntuacion = (self.comodidad + self.durabilidad + self.limpieza) / 3
        if puntuacion >= 80:
            calidad = "Excelente"
        elif puntuacion >= 60:
            calidad = "Buena"
        elif puntuacion >= 40:
            calidad = "Regular"
        else:
            calidad = "Mala"
        print(f"Silla {self.estilo} {self.color}: {calidad} ({puntuacion:.1f}/100)")
        print(f"  Comodidad: {self.comodidad}/100, Durabilidad: {self.durabilidad}/100")

if __name__ == "__main__":
    # Objeto 1: Silla de oficina nueva
    silla1 = Silla("cuero", "negro", 120, 15, 180000, 95, 90, 100, "ergonómica", 0)
    
    # Objeto 2: Silla de comedor usada
    silla2 = Silla("madera", "café", 85, 8, 45000, 75, 70, 60, "clásica", 200)
    
    # Objeto 3: Silla vieja que necesita cuidados
    silla3 = Silla("plástico", "blanco", 80, 3, 15000, 50, 40, 30, "moderna", 800)
    
    # Probando 3 métodos principales
    print("=== CUIDANDO LAS SILLAS ===")
    sillas = [silla1, silla2, silla3]
    
    # Método 1: Evaluar calidad inicial
    print("\n--- 1. CALIDAD INICIAL ---")
    for silla in sillas:
        silla.evaluar_calidad()
    
    # Método 2: Usar las sillas
    print("\n--- 2. USANDO LAS SILLAS ---")
    silla1.usar(8)   # 8 horas de trabajo
    silla2.usar(4)   # 4 horas comiendo
    silla3.usar(2)   # 2 horas ocasionales
    
    # Método 3: Limpiar las sillas
    print("\n--- 3. LIMPIANDO ---")
    for silla in sillas:
        silla.limpiar()
    
    # Calidad final
    print("\n--- CALIDAD FINAL ---")
    for silla in sillas:
        silla.evaluar_calidad()
