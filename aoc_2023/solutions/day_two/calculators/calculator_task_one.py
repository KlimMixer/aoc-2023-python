from aoc_2023.solutions.day_two.parse_strategy import ParseStrategy
from aoc_2023.solutions.day_two.validator import Validator


class CalculatorTaskOne:
    def __init__(self, parser: ParseStrategy, validator: Validator):
        self.parser = parser
        self.validator = validator

    def calculate(self, games_log: str) -> int:
        games = map(self.parser.parse , games_log.split('\n'))
        valid_games = self.validator.validate(games=games)
        return sum(map(lambda game: game.identificator, valid_games))
