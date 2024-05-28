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

class HabitablePlanet(Planet):
    def __init__(self, name, mass, distance, water_presence, atmosphere):
        super().__init__(name, mass, distance)
        self.water_presence = water_presence
        self.atmosphere = atmosphere

    def display_habitable_features(self):
        print(f"{self.name} has water: {self.water_presence} and an atmosphere: {self.atmosphere}")

earth = Planet("Earth", "5.97 × 10^24 kg", "149.6 million km")
earth.display_basic_info()

kepler = HabitablePlanet("Kepler-22b", "Unknown", "600 light years", "Yes", "Likely")
kepler.display_basic_info()
kepler.display_habitable_features()