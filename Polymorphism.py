import sys
sys.stdout.reconfigure(encoding='utf-8')
# Parent Class
class Entity:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Child Classes: Animals
class Dog(Entity):
    def move(self):
        print("The dog is running 🐕.")

class Bird(Entity):
    def move(self):
        print("The bird is flying 🦅.")

class Fish(Entity):
    def move(self):
        print("The fish is swimming 🐟.")

# Child Classes: Vehicles
class Car(Entity):
    def move(self):
        print("The car is driving 🚗.")

class Plane(Entity):
    def move(self):
        print("The plane is flying ✈️.")

class Boat(Entity):
    def move(self):
        print("The boat is sailing 🚤.")

# Function to demonstrate polymorphism
def make_it_move(entity):
    entity.move()

# Create objects
dog = Dog()
bird = Bird()
fish = Fish()
car = Car()
plane = Plane()
boat = Boat()

# Test the move() method for each object
entities = [dog, bird, fish, car, plane, boat]
for entity in entities:
    make_it_move(entity)