
#Hacer importaciones en JSON

import json
from animales import animal
from car import car

#Crear una lista para cada clase que hemos creado
car = [
    car("Coche","Masserati","Violeta","Diesel","Paco"),
    car("Coche","Citroen","Negro","Diesel","Juan"),
    car("Camion","Tesla","Rojo","Diesel","Marcos"),
    car("Moto","Volkswagen","Azul","Gasolina","Iñaki"),
    car("Ciclomotor","Seat","Amarillo","Diesel","Jorge")
]

animal = [
    animal("Perro","Calle","Mamiferos","Carne","Masculino"),
    animal("Pantera","Bosque","Felino","Conejos","Femenino"),
    animal("Zorro","Bosque","Felino","Conejos","Masculino"),
    animal("Abejas","Campo","Insectos","Miel","Masculino"),
    animal("Gato","Calle","Felinos","Pescado","Femenino")
]

# Convertir las instancias de las personas en una lista de diccionario JSON

animal_list = [a.to_dict() for a in animal]

car_list = [c.to_dict() for c in car]

# Ponemos las listas en un contenedor

data = {"animal":animal_list, "car":car_list}

# Guardar el objecto contenedor en un archivo

with open("jsonAPI2/a.json", "w") as file:
    json.dump(data,file)

