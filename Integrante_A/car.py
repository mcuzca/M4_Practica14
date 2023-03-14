
class car:
    def __init__(self,tipo,marca,color,combustible,propietario):
        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.propietario = propietario

    # Imprimindo los datos que aparecen por pantalla

    def saludo(self):
        print("Tipo de vehiculo : " + self.tipo)
        print("Marca  : " + self.marca)
        print("Color  : " + self.color)
        print("Tipo de combustible  : " + self.combustible)
        print("Nombre del propietario  : " + self.propietario)

# Getters y Setters de la clase coche

    def getTipo(self):
        return self.tipo

    def setTipo(self,tipo):
         self.tipo = tipo

    def getMarca(self):
        return self.marca

    def setMarca(self ,marca):
        self.marca = marca

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

    def getCombustible(self):
        return self.combustible

    def setCombustible(self,combustible):
        self.combustible = combustible

    def getPropietario(self):
        return self.propietario

    def setPropietario(self,propietario):
         self.propietario = propietario

#  Devuelve un diccionario de la clase con formato diccionario

    def to_dict(self):
        return {
            "tipo":self.tipo,
            "marca":self.marca,
            "color":self.color,
            "combustible":self.combustible,
            "propietario":self.propietario
        }