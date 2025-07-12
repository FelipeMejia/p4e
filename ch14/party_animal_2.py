from party import PartyAnimal


class CricketFan(PartyAnimal):
    points: int = 0

    def six(self):
        self.points += 6
        self.party()
        print(f"{self.name} points {self.points}")


def main():
    s = PartyAnimal("Sally")
    s.party()

    j = CricketFan("Jim")
    j.party()
    j.six()
    print(dir(j))


if __name__ == "__main__":
    main()
