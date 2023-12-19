import re

from aoc_2023.solutions.day_two.game_model import GameModel
from aoc_2023.solutions.day_two.parsers.parse_strategy import ParseStrategy


class ParseTaskOneStrategy(ParseStrategy):
    def __init__(self):
        self.game_regexp = re.compile(r'Game (\d+)')
        self.red_regexp = re.compile(r'(\d+) red')
        self.green_regexp = re.compile(r'(\d+) green')
        self.blue_regexp = re.compile(r'(\d+) blue')

    def parse(self, line: str) -> GameModel | None:
        if game_id := self.game_regexp.findall(line):
            red_all = self.red_regexp.findall(line)
            green_all = self.green_regexp.findall(line)
            blue_all = self.blue_regexp.findall(line)
            return GameModel(
                identificator=int(game_id[0]),
                red=map(int, red_all),
                green=map(int, green_all),
                blue=map(int, blue_all)
            )
        else:
            return None
