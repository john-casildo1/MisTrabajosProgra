class Computadora:
    def __init__(self, encendido, marca, modelo, procesador, memoria_ram, almacenamiento, pantalla, teclado, tarjeta_grafica):
        self.encendido = True
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento
        self.pantalla = pantalla
        self.teclado = teclado
        self.tarjeta_grafica = tarjeta_grafica
        self.tiene_wifi = True

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, "
                f"Procesador: {self.procesador}, Memoria RAM: {self.memoria_ram}GB, "
                f"Almacenamiento: {self.almacenamiento}GB")
    
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("La computadora se ha encendido.")
        else:
            print("La computadora ya está encendida.")
            
    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("La computadora se ha apagado.")
        else:
            print("La computadora ya está apagada.")
            
    def reiniciar(self):
        if self.encendido:
            print("Reiniciando la computadora...")
        else:
            print("La computadora está apagada. No se puede reiniciar.")
            
    
    def instalar_programa(self, programa):
        if self.encendido:
            print(f"Instalando {programa}...")
        else:
            print("La computadora está apagada. No se puede instalar el programa.")
            
    def desinstalar_programa(self, programa):
        if self.encendido:
            print(f"Desinstalando {programa}...")
        else:
            print("La computadora está apagada. No se puede desinstalar el programa.")
            
on = Computadora(True, "Dell", "XPS 15", "Intel i7", 16, 512, "15.6 pulgadas", "Teclado retroiluminado", "NVIDIA GTX 1650")

on.encender()
on.apagar()
on.reiniciar()