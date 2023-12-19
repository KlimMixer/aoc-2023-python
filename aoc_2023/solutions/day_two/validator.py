from aoc_2023.solutions.day_two.config import Config
from aoc_2023.solutions.day_two.game_model import GameModel
from aoc_2023.solutions.day_two.parsers.parse_strategy import ParseStrategy


class Validator:
    def __init__(self, parser: ParseStrategy, config: Config):
        self.parser = parser
        self.config = config

    def validate(self, games_log: str) -> int:
        games = map(self.parser.parse , games_log.split('\n'))
        valid_games = filter(self._validate_game, games)
        return sum(map(lambda game: game.identificator, valid_games))

    def _validate_game(self, game: GameModel | None) -> bool:
        return (
            not (game is None) and
            all(map(lambda x: self.config.red_limit >= x, game.red)) and
            all(map(lambda x: self.config.green_limit >= x, game.green)) and
            all(map(lambda x: self.config.blue_limit >= x, game.blue))
        )
