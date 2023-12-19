import re

from aoc_2023.solutions.day_two.game_model import Color, GameModel

class ParseStrategy:
    def __init__(self):
        self.game_regexp = re.compile(r'Game (\d+)')

        self.color_regexps = {
            'red': re.compile(r'(\d+) red'),
            'green': re.compile(r'(\d+) green'),
            'blue': re.compile(r'(\d+) blue')
        }

    def parse(self, line: str) -> GameModel | None:
        if game_id := self.game_regexp.findall(line):
            return GameModel(
                identificator=int(game_id[0]),
                colors=Color(
                    **{
                        color: self.parse_color(line, color)
                        for color in self.color_regexps
                    }
                )
            )
        else:
            return None

    def parse_color(self, line: str, color: str):
        return map(int, self.color_regexps[color].findall(line))
