from functools import reduce
from aoc_2023.solutions.day_two.game_model import GameModel

from aoc_2023.solutions.day_two.parse_strategy import ParseStrategy
from aoc_2023.solutions.day_two.validator import Validator


class CalculatorTaskTwo:
    def __init__(self, parser: ParseStrategy, validator: Validator):
        self.parser = parser
        self.validator = validator

    def calculate(self, games_log: str):
        games = map(self.parser.parse , games_log.split('\n'))
        valid_games = filter(lambda game: not (game is None), games)
        return sum(map(self._power_max_colors, valid_games))

    def _power_max_colors(self, game: GameModel) -> int:
        return reduce(
            lambda x,y: x*y,
            [
                max(getattr(game.colors, color))
                for color in game.colors.__dict__
            ]
        )
