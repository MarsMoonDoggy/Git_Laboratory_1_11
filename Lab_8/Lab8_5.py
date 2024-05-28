from get_datetime import get_datetime
get_datetime()

class Planet:
    def __init__(self, name, mass, distance):
        self._name = name
        self._mass = mass
        self._distance = distance

    def get_info(self):
        return f"{self._name} | Mass: {self._mass} | Distance: {self._distance}"

    def describe(self):
        return f"{self._name} is a non-habitable planet."

class HabitablePlanet(Planet):
    def __init__(self, name, mass, distance, water_presence, atmosphere):
        super().__init__(name, mass, distance)
        self._water_presence = water_presence
        self._atmosphere = atmosphere

    def get_habitable_features(self):
        return f"Water: {self._water_presence}, Atmosphere: {self._atmosphere}"

    def describe(self):
        return f"{self._name} is a potentially habitable planet with {self._water_presence} water and {self._atmosphere} atmosphere."

mars = Planet("Mars", "6.39 × 10^23 kg", "227.9 million km")
kepler = HabitablePlanet("Kepler-22b", "Unknown", "600 light years", "Yes", "Likely")

print(mars.describe())
print(kepler.describe())
