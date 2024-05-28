from get_datetime import get_datetime
get_datetime()

class Planet:
    def __init__(self, name, mass, distance):
        self.name = name
        self.mass = mass
        self.distance = distance

    def display_basic_info(self):
        print(f"Name: {self.name}, Mass: {self.mass}, Distance: {self.distance}")

    def update_mass(self, new_mass):
        self.mass = new_mass
        print(f"Updated {self.name} mass to {self.mass}")

    def format_info(self):
        return f"{self.name} | Mass: {self.mass} | Distance from Sun: {self.distance}"

mars = Planet("Mars", "6.39 × 10^23 kg", "227.9 million km")
mars.display_basic_info()
mars.update_mass("6.41 × 10^23 kg")
formatted_info = mars.format_info()
print(formatted_info)