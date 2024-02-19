class Auto:
    cantidadCreados = 0 #atributo de clase

    def __init__(self, modelo, precio, asientos, marca, motor,
    registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro        
    
    def cantidadAsientos(self):

        counter = 0

        for i in range(len(self.asientos)):
            
             counter += 1
        return counter
        
        
    
    def verificarIntegridad(self):
        return self.registro


################################################################################################################################################################

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):

        validos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in validos:
            self.color = color

################################################################################################################################################################


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
        

    
    def asignarTipo(self, tipo):
        if tipo == "electrico" or "gasolina":
            self.tipo = tipo



################################################################################################################################################################

if __name__ == "__main__":

    asiento1 = Asiento("amarillo", 2000, 1, )
    motor1 = Motor(4, "gasolina", 1)
    auto1 = Auto("sendero", 40000, [Asiento], "chevro", Motor, 1)

    print(auto1.cantidadAsientos())


