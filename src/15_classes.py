# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon():

    def __init__(self, Lat, Lon):
        self.Lat = Lat
        self.Lon = Lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, Lat, Lon):
        super().__init__(Lat, Lon)
        self.name = name

    def __str__(self):
        return f'{self.name}, is located at Lat: {self.Lat}, Lon: {self.Lon}'


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, Lat, Lon, difficulty, size):
        super().__init__(name, Lat, Lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f'''{self.name}:
        Location: Lat {self.Lat}, Lon {self.Lon}.
        Difficulty: {self.difficulty}
        Size: {self.size}'''

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 44.052137, -121.41556, 1.5, 2)
# Print it--also make this print more nicely

print(geocache)
