from abc import ABC, abstractmethod

from aoc_2023.solutions.day_two.game_model import GameModel

class ParseStrategy(ABC):
    @abstractmethod
    def parse(self, line: str) -> GameModel | None:
        pass
