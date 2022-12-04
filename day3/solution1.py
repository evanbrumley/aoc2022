import string


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


def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    rucksacks = [Rucksack(line) for line in lines]

    total_priority = sum([r.shared_item_priority for r in rucksacks])

    print(total_priority)


if __name__ == "__main__":
    main()
