class Empleo:
    def __init__(self, puesto, empresa, salario, horas_semanales, experiencia_requerida, satisfaccion, estres, productividad, relacion_jefe, meses_trabajados):
        self.puesto = puesto                         # nombre del puesto
        self.empresa = empresa                       # nombre de la empresa
        self.salario = salario                       # salario mensual en colones
        self.horas_semanales = horas_semanales       # horas de trabajo por semana
        self.experiencia_requerida = experiencia_requerida  # años de experiencia
        self.satisfaccion = satisfaccion             # nivel de satisfacción (0-100)
        self.estres = estres                         # nivel de estrés (0-100)
        self.productividad = productividad           # nivel de productividad (0-100)
        self.relacion_jefe = relacion_jefe           # relación con el jefe (0-100)
        self.meses_trabajados = meses_trabajados     # meses en el empleo

    def trabajar_mes(self):
        self.meses_trabajados = self.meses_trabajados + 1
        # Ganar experiencia reduce estrés pero puede reducir satisfacción si es rutinario
        if self.meses_trabajados % 6 == 0:  # cada 6 meses
            self.productividad = self.productividad + 5
            if self.productividad > 100:
                self.productividad = 100
        if self.estres > 20:
            self.estres = self.estres - 2
        if self.satisfaccion > 30 and self.meses_trabajados > 12:
            self.satisfaccion = self.satisfaccion - 1
        print(f"Mes {self.meses_trabajados} trabajado en {self.empresa}")

    def pedir_aumento(self, porcentaje):
        if porcentaje > 0 and self.productividad >= 70 and self.meses_trabajados >= 6:
            self.salario = self.salario + (self.salario * porcentaje / 100)
            self.satisfaccion = self.satisfaccion + 15
            if self.satisfaccion > 100:
                self.satisfaccion = 100
            self.relacion_jefe = self.relacion_jefe + 5
            if self.relacion_jefe > 100:
                self.relacion_jefe = 100
            print(f"¡Aumento aprobado! Nuevo salario: ¢{self.salario:,.0f}")
        else:
            self.satisfaccion = self.satisfaccion - 10
            if self.satisfaccion < 0:
                self.satisfaccion = 0
            print("Aumento denegado. Necesitas más experiencia o productividad.")

    def evaluar_empleo(self):
        puntuacion = (self.satisfaccion + (100 - self.estres) + self.productividad + self.relacion_jefe) / 4
        if puntuacion >= 80:
            calidad = "Excelente empleo"
        elif puntuacion >= 65:
            calidad = "Buen empleo"
        elif puntuacion >= 50:
            calidad = "Empleo promedio"
        else:
            calidad = "Considera cambiar"
        print(f"{self.puesto} en {self.empresa}: {calidad} ({puntuacion:.1f}/100)")
        print(f"  Salario: ¢{self.salario:,} | Satisfacción: {self.satisfaccion}/100")

if __name__ == "__main__":
    # Objeto 1: Empleo junior prometedor
    empleo1 = Empleo("Desarrollador Jr", "TechCorp", 850000, 40, 1, 75, 60, 70, 80, 3)
    
    # Objeto 2: Empleo senior estable
    empleo2 = Empleo("Gerente", "FinanceInc", 1500000, 45, 5, 85, 70, 85, 75, 18)
    
    # Objeto 3: Empleo con problemas
    empleo3 = Empleo("Asistente", "OldCompany", 450000, 48, 0, 40, 85, 50, 45, 8)
    
    # Probando 3 métodos principales
    print("=== EVALUANDO EMPLEOS ===")
    empleos = [empleo1, empleo2, empleo3]
    
    # Método 1: Evaluar estado inicial
    print("\n--- 1. ESTADO INICIAL ---")
    for empleo in empleos:
        empleo.evaluar_empleo()
    
    # Método 2: Trabajar varios meses
    print("\n--- 2. TRABAJANDO MESES ---")
    for i in range(3):  # 3 meses
        empleo1.trabajar_mes()
    empleo2.trabajar_mes()
    empleo3.trabajar_mes()
    
    # Método 3: Pedir aumentos
    print("\n--- 3. PIDIENDO AUMENTOS ---")
    empleo1.pedir_aumento(15)  # 15%
    empleo2.pedir_aumento(10)  # 10%
    empleo3.pedir_aumento(20)  # 20%
    
    # Evaluación final
    print("\n--- EVALUACIÓN FINAL ---")
    for empleo in empleos:
        empleo.evaluar_empleo()
