class Casa:
    def __init__(self, direccion, metros_cuadrados, habitaciones, banos, precio, estado_construccion, seguridad, jardin, energia_electrica, agua_potable):
        self.direccion = direccion                     # dirección de la casa
        self.metros_cuadrados = metros_cuadrados       # área en metros cuadrados
        self.habitaciones = habitaciones               # número de habitaciones
        self.banos = banos                            # número de baños
        self.precio = precio                          # precio en colones
        self.estado_construccion = estado_construccion # estado: 0-100 (0=ruinas, 100=nuevo)
        self.seguridad = seguridad                    # nivel de seguridad: 0-100
        self.jardin = jardin                          # tiene jardín: True/False
        self.energia_electrica = energia_electrica     # tiene electricidad: True/False
        self.agua_potable = agua_potable              # tiene agua potable: True/False

    # Método 1: Renovar la casa
    def renovar(self, inversion):
        if inversion > 0:
            mejora = inversion / 1000000  # cada millón mejora 1 punto
            self.estado_construccion = self.estado_construccion + mejora
            if self.estado_construccion > 100:
                self.estado_construccion = 100
            
            # La renovación también aumenta el precio
            self.precio = self.precio + inversion * 1.2
            print(f"Casa renovada. Nuevo estado: {self.estado_construccion:.1f}/100")
        else:
            print("La inversión debe ser mayor a 0.")

    # Método 2: Instalar sistema de seguridad
    def mejorar_seguridad(self, inversion_seguridad):
        if inversion_seguridad > 0:
            mejora_seguridad = inversion_seguridad / 500000  # cada 500k mejora 1 punto
            self.seguridad = self.seguridad + mejora_seguridad
            if self.seguridad > 100:
                self.seguridad = 100
            
            self.precio = self.precio + inversion_seguridad * 0.8
            print(f"Seguridad mejorada. Nuevo nivel: {self.seguridad:.1f}/100")
        else:
            print("La inversión en seguridad debe ser mayor a 0.")

    # Método 3: Crear o mejorar jardín
    def trabajar_jardin(self, costo_jardin):
        if costo_jardin > 0:
            if not self.jardin:
                self.jardin = True
                print("¡Jardín creado!")
            else:
                print("Jardín mejorado y embellecido.")
            
            self.precio = self.precio + costo_jardin * 1.5
            # Mejorar también el estado general
            self.estado_construccion = self.estado_construccion + 2
            if self.estado_construccion > 100:
                self.estado_construccion = 100
        else:
            print("El costo del jardín debe ser mayor a 0.")

    # Método 4: Conectar servicios básicos
    def conectar_electricidad(self):
        if not self.energia_electrica:
            self.energia_electrica = True
            self.precio = self.precio + 2000000  # aumenta 2 millones el valor
            print("Electricidad conectada.")
        else:
            print("La casa ya tiene electricidad.")

    def conectar_agua(self):
        if not self.agua_potable:
            self.agua_potable = True
            self.precio = self.precio + 1500000  # aumenta 1.5 millones el valor
            print("Agua potable conectada.")
        else:
            print("La casa ya tiene agua potable.")

    # Método 5: Evaluar valor de mercado
    def evaluar_valor(self):
        # Calcular factor de servicios
        factor_servicios = 1.0
        if self.energia_electrica:
            factor_servicios = factor_servicios + 0.1
        if self.agua_potable:
            factor_servicios = factor_servicios + 0.1
        if self.jardin:
            factor_servicios = factor_servicios + 0.05
        
        # Calcular factor de estado
        factor_estado = self.estado_construccion / 100
        factor_seguridad = self.seguridad / 100
        
        valor_estimado = self.precio * factor_servicios * factor_estado * (1 + factor_seguridad * 0.2)
        
        print(f"Valor estimado de mercado: ¢{valor_estimado:,.0f}")
        return valor_estimado

    # Método 6: Expandir la casa
    def expandir(self, metros_adicionales, habitaciones_adicionales, banos_adicionales, costo):
        if metros_adicionales > 0 and costo > 0:
            self.metros_cuadrados = self.metros_cuadrados + metros_adicionales
            self.habitaciones = self.habitaciones + habitaciones_adicionales
            self.banos = self.banos + banos_adicionales
            self.precio = self.precio + costo
            
            print(f"Casa expandida: +{metros_adicionales}m², +{habitaciones_adicionales} habitaciones, +{banos_adicionales} baños")
        else:
            print("Los metros adicionales y el costo deben ser mayores a 0.")

    # Método 7: Mantenimiento preventivo
    def mantenimiento(self, costo_mantenimiento):
        if costo_mantenimiento > 0:
            # El mantenimiento evita deterioro y mejora ligeramente
            mejora = costo_mantenimiento / 2000000  # cada 2 millones = 1 punto
            self.estado_construccion = self.estado_construccion + mejora
            if self.estado_construccion > 100:
                self.estado_construccion = 100
            
            print(f"Mantenimiento realizado. Estado: {self.estado_construccion:.1f}/100")
        else:
            print("El costo de mantenimiento debe ser mayor a 0.")

    # Método 8: Simular deterioro por tiempo
    def pasar_tiempo(self, anos):
        if anos > 0:
            # La casa se deteriora con el tiempo
            deterioro = anos * 2  # 2 puntos por año
            self.estado_construccion = self.estado_construccion - deterioro
            if self.estado_construccion < 0:
                self.estado_construccion = 0
            
            # La seguridad también puede deteriorarse
            if self.seguridad > 0:
                deterioro_seguridad = anos * 1
                self.seguridad = self.seguridad - deterioro_seguridad
                if self.seguridad < 0:
                    self.seguridad = 0
            
            print(f"Han pasado {anos} años. La casa necesita mantenimiento.")
        else:
            print("Los años deben ser mayor a 0.")

    # Método 9: Mostrar información completa
    def mostrar_info(self):
        print(f"\n=== INFORMACIÓN DE LA CASA ===")
        print(f"Dirección: {self.direccion}")
        print(f"Área: {self.metros_cuadrados} m²")
        print(f"Habitaciones: {self.habitaciones}")
        print(f"Baños: {self.banos}")
        print(f"Precio: ¢{self.precio:,}")
        print(f"Estado de construcción: {self.estado_construccion:.1f}/100")
        print(f"Seguridad: {self.seguridad:.1f}/100")
        print(f"Jardín: {'Sí' if self.jardin else 'No'}")
        print(f"Electricidad: {'Sí' if self.energia_electrica else 'No'}")
        print(f"Agua potable: {'Sí' if self.agua_potable else 'No'}")
        
        # Evaluación general
        if self.estado_construccion >= 80 and self.seguridad >= 70:
            if self.energia_electrica and self.agua_potable:
                print("Estado general: ¡EXCELENTE! 🏠")
            else:
                print("Estado general: Bueno (faltan servicios) 🏡")
        elif self.estado_construccion >= 50:
            print("Estado general: Regular (necesita mejoras) 🏘️")
        else:
            print("Estado general: Malo (necesita renovación urgente) 🏚️")

    # Método 10: Comparar con otra casa
    def comparar_con(self, otra_casa):
        print(f"\n=== COMPARACIÓN DE CASAS ===")
        print(f"Casa 1 ({self.direccion}):")
        print(f"  Área: {self.metros_cuadrados}m² | Precio: ¢{self.precio:,}")
        print(f"  Estado: {self.estado_construccion:.1f}/100 | Seguridad: {self.seguridad:.1f}/100")
        
        print(f"Casa 2 ({otra_casa.direccion}):")
        print(f"  Área: {otra_casa.metros_cuadrados}m² | Precio: ¢{otra_casa.precio:,}")
        print(f"  Estado: {otra_casa.estado_construccion:.1f}/100 | Seguridad: {otra_casa.seguridad:.1f}/100")
        
        # Determinar cuál es mejor
        valor1 = self.evaluar_valor()
        valor2 = otra_casa.evaluar_valor()
        
        if valor1 > valor2:
            print(f"🏆 {self.direccion} tiene mejor valor de mercado")
        elif valor2 > valor1:
            print(f"🏆 {otra_casa.direccion} tiene mejor valor de mercado")
        else:
            print("🤝 Ambas casas tienen valor similar")

# Crear tres objetos de la clase Casa
if __name__ == "__main__":
    # Objeto 1: Casa moderna en buen estado
    casa1 = Casa(
        direccion="Escazú, San José",
        metros_cuadrados=250,
        habitaciones=4,
        banos=3,
        precio=85000000,  # 85 millones
        estado_construccion=90,
        seguridad=85,
        jardin=True,
        energia_electrica=True,
        agua_potable=True
    )
    
    # Objeto 2: Casa en desarrollo
    casa2 = Casa(
        direccion="Heredia Centro",
        metros_cuadrados=180,
        habitaciones=3,
        banos=2,
        precio=45000000,  # 45 millones
        estado_construccion=70,
        seguridad=50,
        jardin=False,
        energia_electrica=True,
        agua_potable=False
    )
    
    # Objeto 3: Casa antigua que necesita renovación
    casa3 = Casa(
        direccion="Cartago, Centro Histórico",
        metros_cuadrados=320,
        habitaciones=5,
        banos=2,
        precio=30000000,  # 30 millones
        estado_construccion=35,
        seguridad=20,
        jardin=True,
        energia_electrica=False,
        agua_potable=False
    )
    
    # Demostrar el uso de los objetos
    print("=== INFORMACIÓN INICIAL DE LAS CASAS ===")
    casas = [casa1, casa2, casa3]
    
    for i, casa in enumerate(casas, 1):
        print(f"\n--- CASA {i} ---")
        casa.mostrar_info()
    
    print("\n=== PROBANDO 3 MÉTODOS PRINCIPALES ===")
    
    # Método 1: Mostrar información inicial
    print(f"\n--- 1. INFORMACIÓN INICIAL ---")
    casa1.mostrar_info()
    casa2.mostrar_info()
    casa3.mostrar_info()
    
    # Método 2: Renovar las casas
    print(f"\n--- 2. RENOVANDO LAS CASAS ---")
    print(f"Renovando {casa1.direccion}...")
    casa1.renovar(5000000)  # 5 millones
    
    print(f"Renovando {casa2.direccion}...")
    casa2.renovar(8000000)  # 8 millones
    
    print(f"Renovando {casa3.direccion}...")
    casa3.renovar(15000000)  # 15 millones
    
    # Método 3: Evaluar valor final
    print(f"\n--- 3. EVALUANDO VALORES FINALES ---")
    print(f"Valor de {casa1.direccion}:")
    casa1.evaluar_valor()
    
    print(f"\nValor de {casa2.direccion}:")
    casa2.evaluar_valor()
    
    print(f"\nValor de {casa3.direccion}:")
    casa3.evaluar_valor()