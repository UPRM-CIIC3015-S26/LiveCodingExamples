class Character:
    def __init__(self, name_param, strength, defence):
        self.health = 100
        self.name = name_param
        self.strength = strength
        self.defence = defence

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return (f"Character: name:{self.name}, "
                f"strength:{self.strength},"
                f"defence: {self.defence},"
                f"health: {self.health}")

    def introduce(self):
        print(f"Hi! My name is {self.name}")

    def attacks(self, attacked):
        damage = self.strength - attacked.defence
        attacked.health -= damage



bienve = Character("Bienve", 100, 10)
alanis1 = Character("Alanis", 200, 20)
alanis2 = alanis1
alanis3 = Character("Alanis", 200, 20)

print(bienve)


alanis1.strength += 10
alanis3.strength += 20

print(alanis1 is alanis3) # False
print(alanis1 == alanis3 and alanis3 == alanis2) # True

bienve.introduce()
characters = [alanis1, bienve]

bienve.is_alive = True

print(bienve)

bienve = Character("Bienve", 30, 10)
alanis = Character("Alanis", 50, 20)

alanis.attacks(bienve)
bienve.attacks(alanis)

print("Class is Over!")

