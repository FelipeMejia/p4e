class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x = self.x + 1
        print(f"So far {self.x}")

    def __del__(self):
        print("I am destructed", self.x)


def main():
    an = PartyAnimal()
    an.party()
    an.party()
    an.party()
    PartyAnimal.party(an)
    an = 42
    print("an contains", an)


if __name__ == "__main__":
    main()
