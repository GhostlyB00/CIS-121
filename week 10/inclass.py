

class Star:
    def __init__(self, _name, _mass, _distance):
        self.name = _name
        self.mass = _mass
        self.distance = _distance
    def get_name(self):
        return self.name
    def get_mass(self):
        return self.mass
    def get_distance(self):
        return self.distance
    

sun = Star('Sol')

class planetarySystem:
    def __init__(self, _star):
        self.star = _star
        self.planets = []

    def add_planet(self, _planet):
        self.planets.append(_planet)

    def show_planets(self):
        for planet in self.planets:
            print(planet.get_name())


class Cake:
    def __init__ (self, _batter, _frosting, _flavor ):
        self.batter = _batter
        self.frosting = _frosting
        self.flavor = _flavor
    def get

        


    
