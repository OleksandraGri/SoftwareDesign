class Hero:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)

class Paladin(Hero):
    def __init__(self, name):
        super().__init__(name)

class InventoryDecorator:
    def __init__(self, hero):
        self.hero = hero

    def __str__(self):
        return str(self.hero)

class Sword(InventoryDecorator):
    def __str__(self):
        return f"{self.hero} with a Sword"

class Shield(InventoryDecorator):
    def __str__(self):
        return f"{self.hero} with a Shield"
