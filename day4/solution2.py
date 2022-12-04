import re


class ElfPair:
    def __init__(self, range1, range2):
        self.range1 = range1
        self.range2 = range2

    @classmethod
    def from_input(cls, lines):
        things = []

        for line in lines:
            match = re.match(r"(?P<n1>\d+)-(?P<n2>\d+),(?P<n3>\d+)-(?P<n4>\d+)", line)
            if not match:
                continue

            n1 = int(match.group("n1"))
            n2 = int(match.group("n2"))
            n3 = int(match.group("n3"))
            n4 = int(match.group("n4"))

            things.append(cls([n1, n2], [n3, n4]))

        return things

    @property
    def complete_overlap(self):
        if (self.range1[0] >= self.range2[0]) and (self.range1[1] <= self.range2[1]):
            return True

        if (self.range2[0] >= self.range1[0]) and (self.range2[1] <= self.range1[1]):
            return True

        return False

    @property
    def partial_overlap(self):
        if self.range1[1] < self.range2[0]:
            return False

        if self.range1[0] > self.range2[1]:
            return False

        return True


def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    elf_pairs = ElfPair.from_input(lines)

    print(len([ep for ep in elf_pairs if ep.partial_overlap]))


if __name__ == "__main__":
    main()
