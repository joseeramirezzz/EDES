class barco:

    def __init__ (self,nombre,posicionX,posicionY,velocidad,rumbo,numeroMunicion):

        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.velocidad = velocidad
        self.rumbo = rumbo
        self.numeroMunicion = numeroMunicion

    def disparar (self):

        if self.numeroMunicion > 0:
            
            self.numeroMunicion -= 1
            return "El barco "+ self.nombre + " ha disparado"
        else:
            return "No tienes munición"
    
    def setvelocidad (self,nuevaVelocidad):

        self.velocidad = nuevaVelocidad
    
    def setRumbo (self,nuevoRumbo):

        self.rumbo = nuevoRumbo
    
    def __str__(self):
        
        return (f"\n------ DATOS DEL BARCO ------"
                f"\nNombre: {self.nombre}"
                f"\nPosición X: {self.posicionX}, Posición Y: {self.posicionY}"
                f"\nVelocidad: {self.velocidad}"
                f"\nRumbo: {self.rumbo}"
                f"\nMunición: {self.numeroMunicion}")
    

barco1 = barco(nombre="Jose1",posicionX="4",posicionY="6",velocidad="13",rumbo="200",numeroMunicion=15)
barco2 = barco("Jose2","7","3","17","126",20)
barco3 = barco("Jose3","6","7","10","145",1)


print("------ ANTES DE LOS METODOS ------ ")
print(barco1,barco2,barco3)

print( " ------ DESPUÉS DE  DISPARAR ------ ")

barco1.disparar()
barco2.disparar()
barco3.disparar()

print(barco1,barco2,barco3)

print(" ------ DESPUÉS DE CAMBIAR LA VELOCIDAD ------")

barco1.setvelocidad(10)
barco2.setvelocidad(15)
barco3.setvelocidad(1)

print(barco1,barco2,barco3)

print(" ------ DESPUÉS DE ESTABLECER NUEVO RUMBO ------ ")

barco1.setRumbo(156)
barco2.setRumbo(136)
barco3.setRumbo(300)

print(barco1,barco2,barco3)