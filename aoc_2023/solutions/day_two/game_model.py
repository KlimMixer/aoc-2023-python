from dataclasses import dataclass

@dataclass
class Color:
    red: list[int]
    green: list[int]
    blue: list[int]

    def __repr__(self):
        return f'(r = {self.red}, g = {self.green}, b = {self.blue})'


@dataclass
class GameModel:
    identificator: int
    colors: Color

    def __repr__(self):
        return f'Game #{self.identificator} {self.colors}'
