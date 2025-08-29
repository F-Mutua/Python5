#OOP Inhertance
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
    
    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flying_speed):
        super().__init__(name, power, city)
        self.flying_speed = flying_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flying_speed} km/h!")

# Objects
hero1 = Superhero("Shadow Knight", "Invisibility", "Gotham")
hero2 = FlyingHero("Sky Falcon", "Wind Blast", "Metropolis", 200)

#Methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
hero2.fly()
