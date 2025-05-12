class Hero:
    def __init__(self, height, build, hair_color, eye_color, attire, inventory):
        self.height = height
        self.build = build
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.attire = attire
        self.inventory = inventory

    def __str__(self):
        return f"Hero [Height: {self.height}, Build: {self.build}, Hair: {self.hair_color}, Eyes: {self.eye_color}, Attire: {self.attire}, Inventory: {self.inventory}]"

class HeroBuilder:
    def __init__(self):
        self.hero = Hero("", "", "", "", "", [])

    def set_height(self, height):
        self.hero.height = height
        return self

    def set_build(self, build):
        self.hero.build = build
        return self

    def set_hair_color(self, color):
        self.hero.hair_color = color
        return self

    def set_eye_color(self, color):
        self.hero.eye_color = color
        return self

    def set_attire(self, attire):
        self.hero.attire = attire
        return self

    def set_inventory(self, inventory):
        self.hero.inventory = inventory
        return self

    def build(self):
        return self.hero

def main():
    builder = HeroBuilder()
    hero = builder.set_height("180cm").set_build("Athletic").set_hair_color("Black").set_eye_color("Blue").set_attire("Armor").set_inventory(["Sword", "Shield"]).build()
    print(hero)

if __name__ == "__main__":
    main()
