import copy

class Virus:
    def __init__(self, name, age, weight, species):
        self.name = name
        self.age = age
        self.weight = weight
        self.species = species
        self.children = []

    def clone(self):
        clone_virus = copy.deepcopy(self)
        return clone_virus

# Створення вірусів
def main():
    parent_virus = Virus("Virus1", 5, 10, "Flu")
    child_virus = Virus("Virus2", 2, 5, "Flu")
    parent_virus.children.append(child_virus)

    cloned_virus = parent_virus.clone()
    print(f"Cloned Virus: {cloned_virus.name}, Children: {[v.name for v in cloned_virus.children]}")

if __name__ == "__main__":
    main()
