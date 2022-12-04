import string


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class Rucksack:
    def __init__(self, items):
        self.items = items

    @property
    def compartments(self):
        compartment_size = int(len(self.items) / 2)
        return [
            self.items[:compartment_size],
            self.items[compartment_size:]
        ]

    @property
    def shared_item(self):
        compartment1, compartment2 = self.compartments

        return list(set(compartment1).intersection(set(compartment2)))[0]

    @property
    def shared_item_priority(self):
        return string.ascii_letters.index(self.shared_item) + 1


class ElfGroup:
    def __init__(self, rucksacks):
        self.rucksacks = rucksacks

    @property
    def shared_item(self):
        return list(set.intersection(*[set(r.items) for r in self.rucksacks]))[0]

    @property
    def shared_item_priority(self):
        return string.ascii_letters.index(self.shared_item) + 1


def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    groups = []

    for line_set in chunks(lines, 3):
        rucksacks = [Rucksack(line) for line in line_set]
        group = ElfGroup(rucksacks)
        groups.append(group)

    total_priority = sum([g.shared_item_priority for g in groups])

    print(total_priority)


if __name__ == "__main__":
    main()
