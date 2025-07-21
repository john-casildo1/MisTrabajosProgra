class Empresa:
    def __init__(self, nombre, sector, ingresos, gastos, empleados, productividad, reputacion, liquidez, proyectos_activos, en_operacion):
        self.nombre = nombre
        self.sector = sector  # Ej: tecnología, salud, etc.
        self.ingresos = ingresos  # colones mensuales
        self.gastos = gastos  # colones mensuales
        self.empleados = empleados  # número de empleados
        self.productividad = productividad  # 0-100
        self.reputacion = reputacion  # 0-100
        self.liquidez = liquidez  # % disponible de flujo de caja
        self.proyectos_activos = proyectos_activos  # número de proyectos
        self.en_operacion = en_operacion  # True o False

    # Método 1: Contratar empleados
    def contratar(self, cantidad):
        if cantidad > 0:
            self.empleados += cantidad
            self.gastos += cantidad * 600000  # salario promedio
            self.productividad = min(100, self.productividad + cantidad * 0.5)

    # Método 2: Despedir empleados
    def despedir(self, cantidad):
        if cantidad > 0 and cantidad <= self.empleados:
            self.empleados -= cantidad
            self.gastos -= cantidad * 600000
            self.productividad = max(0, self.productividad - cantidad * 1)

    # Método 3: Invertir en marketing
    def invertir_marketing(self, monto):
        if self.liquidez >= monto and monto > 0:
            self.liquidez -= monto
            self.reputacion = min(100, self.reputacion + monto / 100000)
            self.ingresos += monto * 0.2  # retorno estimado

    # Método 4: Lanzar nuevo proyecto
    def lanzar_proyecto(self, inversion):
        if self.liquidez >= inversion and self.productividad >= 50:
            self.liquidez -= inversion
            self.proyectos_activos += 1
            self.productividad = max(0, self.productividad - 10)
            self.reputacion = min(100, self.reputacion + 2)

    # Método 5: Evaluar balance financiero
    def evaluar_balance(self):
        ganancia = self.ingresos - self.gastos
        if ganancia < 0:
            self.liquidez = max(0, self.liquidez - abs(ganancia) * 0.05)
            self.reputacion = max(0, self.reputacion - 5)
        else:
            self.liquidez = min(100, self.liquidez + ganancia * 0.03)
            self.reputacion = min(100, self.reputacion + 1)

# Crear tres objetos de la clase Empresa
if __name__ == "__main__":
    # Objeto 1: Empresa de tecnología exitosa
    empresa1 = Empresa(
        nombre="TechCorp",
        sector="tecnología",
        ingresos=15000000,  # 15 millones mensuales
        gastos=12000000,    # 12 millones mensuales
        empleados=50,
        productividad=85,
        reputacion=90,
        liquidez=75,
        proyectos_activos=3,
        en_operacion=True
    )
    
    # Objeto 2: Startup en crecimiento
    empresa2 = Empresa(
        nombre="InnovateLab",
        sector="salud",
        ingresos=5000000,   # 5 millones mensuales
        gastos=4500000,     # 4.5 millones mensuales
        empleados=15,
        productividad=70,
        reputacion=60,
        liquidez=40,
        proyectos_activos=1,
        en_operacion=True
    )
    
    # Objeto 3: Empresa en dificultades
    empresa3 = Empresa(
        nombre="OldIndustries",
        sector="manufactura",
        ingresos=8000000,   # 8 millones mensuales
        gastos=9500000,     # 9.5 millones mensuales (pérdidas)
        empleados=80,
        productividad=45,
        reputacion=30,
        liquidez=15,
        proyectos_activos=0,
        en_operacion=True
    )
    
    # Demostrar el uso de los objetos
    print("=== INFORMACIÓN DE LAS EMPRESAS ===")
    print(f"Empresa 1: {empresa1.nombre} ({empresa1.sector})")
    print(f"  Empleados: {empresa1.empleados}, Productividad: {empresa1.productividad}%, Reputación: {empresa1.reputacion}%")
    print(f"  Ingresos: ¢{empresa1.ingresos:,}, Gastos: ¢{empresa1.gastos:,}")
    
    print(f"\nEmpresa 2: {empresa2.nombre} ({empresa2.sector})")
    print(f"  Empleados: {empresa2.empleados}, Productividad: {empresa2.productividad}%, Reputación: {empresa2.reputacion}%")
    print(f"  Ingresos: ¢{empresa2.ingresos:,}, Gastos: ¢{empresa2.gastos:,}")
    
    print(f"\nEmpresa 3: {empresa3.nombre} ({empresa3.sector})")
    print(f"  Empleados: {empresa3.empleados}, Productividad: {empresa3.productividad}%, Reputación: {empresa3.reputacion}%")
    print(f"  Ingresos: ¢{empresa3.ingresos:,}, Gastos: ¢{empresa3.gastos:,}")
    
    print("\n=== PROBANDO MÉTODOS ===")
    
    # Empresa 1: Invertir en marketing y lanzar proyecto
    print(f"\n--- {empresa1.nombre} ---")
    print(f"Liquidez inicial: {empresa1.liquidez}%")
    print(f"Invirtiendo ¢500,000 en marketing...")
    empresa1.invertir_marketing(500000)
    print(f"Nueva reputación: {empresa1.reputacion}%")
    print(f"Nuevos ingresos: ¢{empresa1.ingresos:,}")
    
    print(f"Lanzando nuevo proyecto con inversión de ¢2,000,000...")
    empresa1.lanzar_proyecto(2000000)
    print(f"Proyectos activos: {empresa1.proyectos_activos}")
    print(f"Nueva liquidez: {empresa1.liquidez}%")
    
    # Empresa 2: Contratar empleados
    print(f"\n--- {empresa2.nombre} ---")
    print(f"Empleados iniciales: {empresa2.empleados}")
    print(f"Contratando 5 empleados...")
    empresa2.contratar(5)
    print(f"Nuevos empleados: {empresa2.empleados}")
    print(f"Nuevos gastos: ¢{empresa2.gastos:,}")
    print(f"Nueva productividad: {empresa2.productividad}%")
    
    # Empresa 3: Evaluar balance y reestructurar
    print(f"\n--- {empresa3.nombre} ---")
    print(f"Evaluando balance financiero...")
    empresa3.evaluar_balance()
    ganancia = empresa3.ingresos - empresa3.gastos
    print(f"Ganancia/Pérdida: ¢{ganancia:,}")
    print(f"Nueva liquidez: {empresa3.liquidez}%")
    print(f"Nueva reputación: {empresa3.reputacion}%")
    
    print(f"Despidiendo 20 empleados para reducir gastos...")
    empresa3.despedir(20)
    print(f"Empleados restantes: {empresa3.empleados}")
    print(f"Gastos reducidos: ¢{empresa3.gastos:,}")
    print(f"Productividad afectada: {empresa3.productividad}%")
    
    print(f"Invirtiendo ¢300,000 en marketing para mejorar imagen...")
    empresa3.invertir_marketing(300000)
    print(f"Reputación mejorada: {empresa3.reputacion}%")
    
    print("\n=== RESUMEN FINAL ===")
    empresas = [empresa1, empresa2, empresa3]
    for i, empresa in enumerate(empresas, 1):
        ganancia_final = empresa.ingresos - empresa.gastos
        estado = "RENTABLE" if ganancia_final > 0 else "EN PÉRDIDAS"
        print(f"Empresa {i} ({empresa.nombre}): {estado} - Ganancia: ¢{ganancia_final:,}")
        print(f"  Liquidez: {empresa.liquidez}% | Reputación: {empresa.reputacion}% | Empleados: {empresa.empleados}")
