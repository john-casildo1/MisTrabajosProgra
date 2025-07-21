from carro import Carro
from casa import Casa  
from perro import Perro
from empleo import Empleo
from amor import Amor
from empresa import Empresa

def main():
    print("*** MI SIMULACIÓN DE VIDA ***")
    print("Este programa simula un día en mi vida usando POO")
    
    print("\n=== CREANDO MIS OBJETOS ===")
    
    trabajo = Empleo("Estudiante de TI", "Universidad", 500000, 20, 1, 70, 40, 75, 80, 6)
    casa = Casa("Cartago", 80, 2, 1, 25000000, 60, 50, True, True, True)
    carro = Carro("Honda", "Civic", "gasolina", 70, False, 0, 25000, 75, True, 80)
    perro = Perro("Max", "Golden", 2, 25, "dorado", 80, 30, 85, 90, 50)
    novia = Amor("Ana", 12, 80, 75, 80, 85, 88, 80, 85, 70)
    empresa = Empresa("TechUni", "educación", 5000000, 4000000, 15, 70, 60, 50, 1, True)
    
    print("Todos los objetos creados correctamente!")
    
    print("\n=== SIMULANDO UN DÍA NORMAL ===")
    
    print("\n--- MAÑANA ---")
    print("Me voy al trabajo en carro:")
    carro.encender()
    carro.conducir(10)
    
    print("Trabajo medio tiempo:")
    trabajo.trabajar_mes()
    
    print("\n--- TARDE ---") 
    print("Llego a casa y cuido a Max:")
    perro.alimentar()
    perro.jugar()
    
    if trabajo.salario > 400000:
        print("Como me va bien, mejoro un poco la casa:")
        casa.renovar(1000000)
    
    print("\n--- NOCHE ---")
    print("Paso tiempo con mi novia:")
    novia.pasar_tiempo_juntos(80)
    
    if trabajo.estres > 50:
        print("Tenemos que resolver un pequeño conflicto:")
        novia.resolver_conflicto("dialogo")
    
    print("\n--- FIN DE SEMANA ---")
    print("Hago mantenimiento básico:")
    carro.mantenimiento()
    casa.mantenimiento(500000)
    perro.dormir()
    
    print("\n=== RESULTADOS FINALES ===")
    
    print("\n--- CÓMO ESTÁN LAS COSAS ---")
    trabajo.evaluar_empleo()
    casa.evaluar_valor()
    perro.estado_general()
    novia.evaluar_relacion()
    
    print("\n--- MIS ESTADÍSTICAS ---")
    print("💰 Salario: ¢" + str(trabajo.salario))
    print("🏠 Valor casa: ¢" + str(casa.precio))
    print("🚗 Kms del carro: " + str(carro.kilometraje))
    print("🐕 Felicidad de Max: " + str(perro.felicidad) + "/100")
    print("❤️ Felicidad con novia: " + str(novia.felicidad) + "/100")
    
    promedio_vida = (trabajo.satisfaccion + novia.felicidad + perro.felicidad) / 3
    
    print("\n--- MI PUNTUACIÓN DE VIDA ---")
    if promedio_vida >= 80:
        print("🎉 ¡Me va súper bien! Puntuación: " + str(round(promedio_vida, 1)) + "/100")
    elif promedio_vida >= 60:
        print("😊 Me va bien, pero puedo mejorar. Puntuación: " + str(round(promedio_vida, 1)) + "/100")
    else:
        print(" Necesito trabajar más en mi vida. Puntuación: " + str(round(promedio_vida, 1)) + "/100")
    
    print("\n*** FIN DE LA SIMULACIÓN ***")
    print("Gracias por probar mi programa!")

if __name__ == "__main__":
    main()
