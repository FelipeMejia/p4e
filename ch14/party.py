class PartyAnimal:
    x: int = 0
    name: str = ""

    def __init__(self, nam):
        self.name = nam
        print(f"{self.name} constructed")

    def party(self):
        self.x += 1
        print(f"{self.name} party count {self.x}")
