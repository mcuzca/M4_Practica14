
class animal:
    def __init__(self,name,habitat,familia,comida ,sexo):
        self.name = name
        self.familia = familia
        self.comida = comida
        self.habitat = habitat
        self.sexo = sexo

    # Getters y Setters de la clase animales

    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name

    def getHabitat(self):
        return self.habitat
    def setHabitat(self,habitat):
        self.habitat = habitat

    def getComida(self):
        return self.comida
    def setComida(self,comida):
        self.comida = comida

    def getFamilia(self):
        return self.familia
    def setFamilia(self,familia):
        self.familia = familia

    def getSexo(self):
        return self.sexo
    def setSexo(self,sexo):
        self.sexo = sexo

    # Imprimindo los datos que aparecen por pantalla

    def saludo(self):
        print("Nombre comun del animal : " + self.name)
        print("Habitat natural : " + self.habitat)
        print("Familia del animal : " + self.familia)
        print("Comida  : " + self.comida)
        print("Sexo : " + self.sexo)

    #  Devuelve un diccionario de la clase con formato diccionario

    def to_dict(self):
        return {
            "nombre":self.name,
            "habitat":self.habitat,
            "familia animal":self.familia,
            "comida":self.comida,
            "sexo":self.sexo
        }