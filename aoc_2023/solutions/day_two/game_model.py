class GameModel:
    def __init__(self, identificator: int, red: list[int], green: list[int], blue: list[int]):
        self.identificator = identificator
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'Game #{self.identificator} (r = {self.red}, g = {self.green}, b = {self.blue})'
