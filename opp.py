# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"
    

# Child Class with Encapsulation
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Inheriting from Device
        self.storage = storage
        self.__battery = battery   # Encapsulated (private)

    def charge(self, amount):
        self.__battery += amount
        return f"Battery charged to {self.__battery}% 🔋"

    def get_battery(self):  # Controlled access
        return f"Battery at {self.__battery}%"

    def call(self, number):
        return f"Calling {number}... 📞"


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 80)
phone2 = Smartphone("Apple", "iPhone 15", "128GB", 65)

print(phone1.info())           # From parent class
print(phone1.get_battery())    # Controlled access
print(phone1.charge(15))       # Charging battery
print(phone2.call("+254707796000"))




class Animal:
    def move(self):
        pass   # Empty method (will be overridden)


class Dog(Animal):
    def move(self):
        return "Running 🐕"


class Bird(Animal):
    def move(self):
        return "Flying 🐦"


class Fish(Animal):
    def move(self):
        return "Swimming 🐟"


# Polymorphism in action
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())
