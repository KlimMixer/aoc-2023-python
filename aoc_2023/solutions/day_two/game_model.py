class GameModel:
    def __init__(self, id: int, red: list[int], green: list[int], blue: list[int]):
        self.id = id
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'Game #{self.id} (r = {self.red}, g = {self.green}, b = {self.blue})'