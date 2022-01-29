class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def __str__(self):
        return f"{self.name} {self.animals}"

    def add_animal(self, name):
        self.animals.append(name)

    # def add_lion(self, name):
    #     self.animals.append(Lion(name))

    # def add_tiger(self, name, edad):
    #     self.animals.append(Tiger(name,edad))

    # def add_bear(self, name):
    #     self.animals.append(Bear(name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

# 1. Comience creando una clase Animal.


class Animal:
    def __init__(self, animal, name, edad, nivelSalud, nivelFelicidad):
        self.animal = animal
        self.name = name
        self.edad = edad
        self.nivelSalud = nivelSalud
        self.nivelFelicidad = nivelFelicidad

    def __str__(self):
        return f"{self.animal} {self.name} {self.edad} {self.nivelSalud} {self.nivelFelicidad}"
    # 4. La clase Animal debe tener un método display_info que muestre el nombre, la salud y la felicidad del animal

    def display_info(self):
        print(f"Animal:{self.animal} - Nombre:{self.name} - Edad:{self.edad} - Nivel de Salud:{self.nivelSalud} - Nivel de Felicidad:{self.nivelFelicidad} \n")

    # 5. También debe tener un método de alimentación que aumente la salud y la felicidad en 10.
    # 8. Los animales también deben responder al método de alimentación con diferentes niveles de cambios en la salud y la felicidad.
    def comida(self):
        self.nivelFelicidad += 5
        self.nivelSalud += 5


# 2.luego al menos 3 clases específicas de animales que hereden de Animal. (Tal vez leones, tigres y osos, ¡Dios mío!)
# Cada animal debe tener al menos un nombre, una edad, un nivel de salud y un nivel de felicidad.
# 6. En al menos una de las clases de Animal child que ha creado, agregue al menos un atributo único.
# 7. Dele a cada animal diferentes niveles predeterminados de salud y felicidad
class Tiger(Animal):
    def __init__(self, name, edad, nivelSalud=15, nivelFelicidad=10, animal="Tigre"):
        super().__init__(animal, name, edad, nivelSalud, nivelFelicidad)

    def comida(self):
        self.nivelFelicidad += 15
        self.nivelSalud += 20


class Lion(Animal):
    def __init__(self, name, edad, nivelSalud=20, nivelFelicidad=15, animal="León"):
        super().__init__(animal, name, edad, nivelSalud, nivelFelicidad)

    def comida(self):
        self.nivelFelicidad += 10
        self.nivelSalud += 15


class Bear(Animal):
    def __init__(self, name, edad, nivelGordura, nivelSalud=25, nivelFelicidad=30, animal="Oso"):
        super().__init__(animal, name, edad, nivelSalud, nivelFelicidad)
        self.nivelGordura = nivelGordura

    def comida(self):
        self.nivelFelicidad += 20
        self.nivelSalud -= 3


# 9. Una vez que haya probado sus diferentes animales y se sienta más cómodo con la herencia, cree una clase de zoológico para
# ayudar a manejar a todos sus animales.


zoo1 = Zoo("John's Zoo")

tigre1 = Tiger("Rajah", 3, 3, 3)
tigre1.display_info()
tigre1.comida()
print(tigre1.__dict__, "\n")
zoo1.add_animal(tigre1)

print("##################################################################### \n")

tigre2 = Tiger("Nirah", 3, 3, 3)
tigre2.display_info()
tigre2.comida()
print(tigre2.__dict__, "\n")

# zoo1.add_tiger(tigre2)

print("##################################################################### \n")

leon1 = Lion('Nala', 2, 25, 15)
leon1.display_info()
leon1.comida()
print(leon1.__dict__, "\n")

# zoo1.add_lion("Nala")

print("##################################################################### \n")

oso1 = Bear("OsitoGominola", 3, "Piola")
oso1.display_info()
oso1.comida()
print(oso1.__dict__, "\n")

zoo1.print_all_info()

# zoo1.add_lion("Nala")
# zoo1.add_lion("Simba")
# zoo1.add_tiger("Rajah")
# zoo1.add_tiger("Shere Khan")

# BONUS: Debe crear una forma interactiva (while True; )) para poder ir creando animales e ir agregándolos al ZOO.
# 10. Debe subir esta tarea con nombre zoo a Github.
