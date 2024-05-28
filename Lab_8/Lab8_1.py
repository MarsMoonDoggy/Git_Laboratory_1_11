from get_datetime import get_datetime
get_datetime()

class Planet:
    def __init__(self, name, mass, distance):
        self.name = name
        self.mass = mass
        self.distance = distance

mars = Planet("Mars", "6.39 × 10^23 kg", "227.9 million km")

print(f"Planet Name: {mars.name}")
print(f"Mass: {mars.mass}")
print(f"Distance from Sun: {mars.distance}")