# Smartphone class with inheritance

class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery: {self.battery_life}h")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, gpu):
        super().__init__(brand, model, battery_life)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!")

    # Encapsulation example
    def get_gpu(self):
        return self.gpu

# Polymorphism Challenge: Vehicles

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("The Prado is driving")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing")

# Example usage
if __name__ == "__main__":
    # Smartphone objects
    phone1 = Smartphone("Xiaomi", "X7 Pro", 18)
    phone2 = GamingSmartphone("Asus", "ROG Phone 6", 24, "Adreno 730")

    phone1.info()
    phone2.info()
    phone2.play_game("Mahjong")

    # Vehicle objects
    vehicle = Vehicle()
    car = Car()
    plane = Plane()
    boat = Boat()

    vehicle.move()
    car.move()
    plane.move()
    boat.move()