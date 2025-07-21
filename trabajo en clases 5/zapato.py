class Zapato:
    def __init__(self, marca, modelo, talla, precio, material, color, comodidad, durabilidad, limpieza, kilometros_usados):
        self.marca = marca                    # marca del zapato
        self.modelo = modelo                  # modelo del zapato
        self.talla = talla                   # talla del zapato
        self.precio = precio                 # precio en colones
        self.material = material             # material: cuero, tela, sintético
        self.color = color                   # color del zapato
        self.comodidad = comodidad           # nivel de comodidad (0-100)
        self.durabilidad = durabilidad       # nivel de durabilidad (0-100)
        self.limpieza = limpieza             # nivel de limpieza (0-100)
        self.kilometros_usados = kilometros_usados  # kilómetros caminados

    def caminar(self, distancia):
        if distancia > 0:
            self.kilometros_usados = self.kilometros_usados + distancia
            desgaste = distancia * 0.5
            self.durabilidad = self.durabilidad - desgaste
            if self.durabilidad < 0:
                self.durabilidad = 0
            self.limpieza = self.limpieza - distancia * 2
            if self.limpieza < 0:
                self.limpieza = 0
            print(f"Caminaste {distancia}km con {self.marca}. Total: {self.kilometros_usados}km")
        else:
            print("La distancia debe ser mayor a 0")

    def limpiar(self):
        if self.limpieza < 100:
            self.limpieza = self.limpieza + 60
            if self.limpieza > 100:
                self.limpieza = 100
            self.comodidad = self.comodidad + 5
            if self.comodidad > 100:
                self.comodidad = 100
            print(f"{self.marca} {self.modelo} ha sido limpiado")
        else:
            print(f"{self.marca} ya está completamente limpio")

    def evaluar_estado(self):
        if self.durabilidad >= 80 and self.limpieza >= 70:
            estado = "Excelente"
        elif self.durabilidad >= 50 and self.limpieza >= 40:
            estado = "Bueno"
        elif self.durabilidad >= 20:
            estado = "Regular"
        else:
            estado = "Malo"
        print(f"{self.marca} {self.modelo}: {estado}")
        print(f"  Durabilidad: {self.durabilidad}/100, Limpieza: {self.limpieza}/100")

if __name__ == "__main__":
    # Objeto 1: Zapato deportivo nuevo
    zapato1 = Zapato("Nike", "Air Max", 42, 75000, "sintético", "negro", 95, 90, 100, 0)
    
    # Objeto 2: Zapato formal usado
    zapato2 = Zapato("Clarks", "Oxford", 41, 45000, "cuero", "marrón", 80, 60, 70, 150)
    
    # Objeto 3: Zapato casual muy usado
    zapato3 = Zapato("Converse", "All Star", 40, 25000, "tela", "blanco", 70, 30, 20, 500)
    
    # Probando 3 métodos principales
    print("=== CUIDANDO LOS ZAPATOS ===")
    zapatos = [zapato1, zapato2, zapato3]
    
    # Método 1: Evaluar estado inicial
    print("\n--- 1. ESTADO INICIAL ---")
    for zapato in zapatos:
        zapato.evaluar_estado()
    
    # Método 2: Caminar con los zapatos
    print("\n--- 2. CAMINANDO ---")
    zapato1.caminar(5)   # 5km con Nike
    zapato2.caminar(3)   # 3km con Clarks
    zapato3.caminar(2)   # 2km con Converse
    
    # Método 3: Limpiar los zapatos
    print("\n--- 3. LIMPIANDO ---")
    for zapato in zapatos:
        zapato.limpiar()
    
    # Estado final
    print("\n--- ESTADO FINAL ---")
    for zapato in zapatos:
        zapato.evaluar_estado()
