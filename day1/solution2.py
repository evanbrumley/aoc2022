class CalorieCounter:
    def __init__(self, elves):
        self.elves = elves

    @classmethod
    def from_input(cls, lines):
        elves = []
        current_elf = []

        for line in lines:
            if not line:
                elves.append(current_elf)
                current_elf = []
            else:
                current_elf.append(int(line))

        if current_elf:
            elves.append(current_elf)

        return CalorieCounter(elves)

    @property
    def elf_totals(self):
        return [sum(elf) for elf in self.elves]


def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    counter = CalorieCounter.from_input(lines)

    print(sum((sorted(counter.elf_totals)[-3:])))


if __name__ == "__main__":
    main()
