class Human:
    def __init__(self, name, pets):
        self.name = name
        self.pets = pets
        if self.pets is None:
            self.pets = []

    def add_pet(self, new_pet):
        self.pets.append(new_pet)
        new_pet.owners.append(self)


class Animal:
    count = 0

    def __init__(self, name, color, height, diet, species, owners=None):
        self.name = name
        self.color = color
        self.height = height
        self.diet = diet
        self.species = species
        self.owners = owners
        Animal.count += 1

    def speak(self):
        pass

    def eat(self, food):
        pass

    def sleep(self):
        print("zzz...")

    def move(self):
        pass


class Dog(Animal):
    def __init__(self, name, color, height, owners=None):
        super().__init__(name, color, height, "CARNIVORE", "DOG")
        self.owners = owners

    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "MEAT":
            print("Yum")
        else:
            print("Yuck")

    def move(self):
        print(f"{self.name} walks.")
