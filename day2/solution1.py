import re

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

CODES_ME = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

CODES_THEM = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

WINS = [
    [ROCK, PAPER],
    [PAPER, SCISSORS],
    [SCISSORS, ROCK],
]

CHOICE_SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}


class Round:
    def __init__(self, them_code, me_code):
        self.me = CODES_ME[me_code]
        self.them = CODES_THEM[them_code]

    @property
    def win(self):
        return [self.them, self.me] in WINS

    @property
    def draw(self):
        return self.me == self.them

    @property
    def loss(self):
        return [self.me, self.them] in WINS

    @property
    def win_score(self):
        if self.win:
            return 6
        elif self.draw:
            return 3

        return 0

    @property
    def choice_score(self):
        return CHOICE_SCORES[self.me]

    @property
    def score(self):
        return self.win_score + self.choice_score


class Game:
    def __init__(self, rounds):
        self.rounds = rounds

    def __str__(self):
        return "Foo"

    @classmethod
    def from_input(cls, lines):
        rounds = []

        for line in lines:
            match = re.match(r"(?P<them>[ABC]) (?P<me>[XYZ])", line)
            if not match:
                continue

            them_code = match.group("them")
            me_code = match.group("me")

            rounds.append(Round(them_code, me_code))

        return cls(rounds)


def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    game = Game.from_input(lines)

    print(sum([r.score for r in game.rounds]))


if __name__ == "__main__":
    main()
