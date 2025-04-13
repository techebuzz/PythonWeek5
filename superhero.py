class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and I'm level {self.level}!")

    def fight_crime(self):
        print(f"{self.name} is fighting crime using {self.power}!")

# Inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    def fight_crime(self):
        print(f"{self.name} flies at {self.flight_speed} km/h to stop villains using {self.power}!")

# Create objects
hero1 = Superhero("IronFist", "Martial Arts", 7)
hero2 = FlyingHero("SkyBlazer", "Wind Control", 9, 500)

hero1.introduce()
hero1.fight_crime()

hero2.introduce()
hero2.fight_crime()
