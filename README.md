# Assignment 1 & 2 – Python Classes & Polymorphism 🏗️🎭

## Overview
This repository contains solutions for **Assignment 1** and **Activity 2**.  
The main focus is on **Python Object-Oriented Programming (OOP)**, including:

- Classes and objects  
- Constructors (`__init__`)  
- Attributes and methods  
- Inheritance  
- Polymorphism (method overriding)  

---

## Assignment 1: Design Your Own Class

**Description:**  
We created a `Smartphone` class to represent a real-world object, along with a `Smartwatch` subclass to demonstrate inheritance and polymorphism.

**Features:**
- **Attributes:** `brand`, `model`, `battery_life`, `storage`, `strap_color` (for smartwatch), `apps`
- **Methods:**  
  - `install_app()` – adds apps to the device  
  - `make_call()` – demonstrates method overriding in the subclass  
  - `__str__()` – prints device details  

**Example Usage:**
```python
phone = Smartphone("Samsung", "Galaxy S24", 20, 256)
phone.install_app("WhatsApp")
phone.make_call("+254700123456")

watch = Smartwatch("Apple", "Watch Series 9", 18, 32, "Black")
watch.install_app("Fitness Tracker")
watch.make_call("+254711987654")
watch.track_heart_rate()
```


## Assignment 2: Polymorphism Challenge 🎭




**Description:**  
This activity demonstrates **polymorphism**, where multiple classes define the same method `move()`, but each class behaves differently.

**Classes Implemented:**  
- `Car` → Driving  
- `Plane` → Flying  
- `Boat` → Sailing  
- `Bike` → Pedaling

**Example Usage:**

```python
vehicles = [Car(), Plane(), Boat(), Bike()]
for v in vehicles:
    v.move()
```
