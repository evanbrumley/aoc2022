import re


class Blarg:
    def __init__(self, things):
        self.things = things

    def __str__(self):
        return "Foo"

    @classmethod
    def from_input(cls, lines):
        things = []

        for line in lines:
            match = re.match(r"(?P<x>.+)", line)
            if not match:
                continue

            x = match.group("x")

            things.append(x)

        return cls(things)


def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    blarg = Blarg.from_input(lines)

    print(blarg)


if __name__ == "__main__":
    main()
