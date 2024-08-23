class Pet:
    def __init__(self, name, age, breed, species):
        self._name = name  # Using encapsulation with a private attribute
        self._age = age
        self._breed = breed
        self._species = species
        self._adopted = False  # All pets are initially not adopted

    def get_details(self):
        return f"{self._name}, {self._species}, {self._breed}, {self._age} years old, Adopted: {self._adopted}"

    def adopt(self):
        self._adopted = True

    def is_adopted(self):
        return self._adopted

    def __str__(self):
        return self.get_details()
