from typing import Optional
from aoc_2023.solutions.day_two.config import Config
from aoc_2023.solutions.day_two.game_model import GameModel

class Validator:
    def __init__(self, config: Config):
        self.config = config

    def validate(self, games: list[Optional[GameModel]]) -> list[GameModel]:
        return filter(self._validate_game, games)

    def _validate_game(self, game: Optional[GameModel]) -> bool:
        if game:
            return all(
                self.check_limit(
                    getattr(self.config, color),
                    getattr(game.colors, color)
                )
                for color in game.colors.__dict__
            )
        return False

    def check_limit(self, limit: int, color_counts: list[int]):
        return all(map(lambda x: limit >= x, color_counts))
