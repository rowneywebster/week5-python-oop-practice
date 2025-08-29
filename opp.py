# Activity 1: Designing a Smartphone class with inheritance and polymorphism
# This class demonstrates constructors, attributes, methods, and overriding

class Smartphone:
    def __init__(self, brand, model, battery_life, storage):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
        self.storage = storage  # in GB
        self.apps = []

    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed on {self.model}.")

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery_life}h battery life."



class Smartwatch(Smartphone):  # inherits from Smartphone
    def __init__(self, brand, model, battery_life, storage, strap_color):
        # call parent constructor
        super().__init__(brand, model, battery_life, storage)
        self.strap_color = strap_color

    # Override method (Polymorphism)
    def make_call(self, number):
        print(f"Voice call to {number} via {self.model} smartwatch.")

    def track_heart_rate(self):
        print(f"{self.model} is tracking heart rate...")

    def __str__(self):
        return f"{self.brand} {self.model} Smartwatch with {self.strap_color} strap."

# Create Smartphone
phone1 = Smartphone("Samsung", "Galaxy S24", 20, 256)
print(phone1)
phone1.install_app("WhatsApp")
phone1.make_call("+254700123456")

print("-----")

# Create Smartwatch
watch1 = Smartwatch("Apple", "Watch Series 9", 18, 32, "Black")
print(watch1)
watch1.install_app("Fitness Tracker")
watch1.make_call("+254711987654")
watch1.track_heart_rate()


# Activity 2: Polymorphism Challenge
# Different vehicles define the same move() method in their own way

class Vehicle:
    def move(self):
        # This will be overridden in child classes
        pass


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")


class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water...")


class Bike(Vehicle):
    def move(self):
        print("🚴 Pedaling along the path...")


vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    v.move()  # same method name, different behavior
