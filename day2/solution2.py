import re

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

CODES_THEM = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

WINS = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}

LOSSES = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

CHOICE_SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

LOSS = "loss"
DRAW = "draw"
WIN = "win"

CODES_RESULT = {
    "X": LOSS,
    "Y": DRAW,
    "Z": WIN,
}

class Round:
    def __init__(self, them_code, result_code):
        self.result = CODES_RESULT[result_code]
        self.them = CODES_THEM[them_code]

    @property
    def me(self):
        if self.draw:
            return self.them
        elif self.win:
            return WINS[self.them]
        return LOSSES[self.them]

    @property
    def win(self):
        return self.result == WIN

    @property
    def draw(self):
        return self.result == DRAW

    @property
    def loss(self):
        return self.result == LOSS

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

    @classmethod
    def from_input(cls, lines):
        rounds = []

        for line in lines:
            match = re.match(r"(?P<them>[ABC]) (?P<result>[XYZ])", line)
            if not match:
                continue

            them_code = match.group("them")
            result_code = match.group("result")

            rounds.append(Round(them_code, result_code))

        return cls(rounds)


def main():
    with open("input", "r") as f:
        lines = f.read().splitlines()

    game = Game.from_input(lines)

    print(sum([r.score for r in game.rounds]))


if __name__ == "__main__":
    main()
