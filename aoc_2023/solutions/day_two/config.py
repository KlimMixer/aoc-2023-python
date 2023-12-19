from io import TextIOWrapper
import json

class Config:
    def __init__(self, red_limit: int, green_limit: int, blue_limit: int):
        self.red_limit = red_limit
        self.green_limit = green_limit
        self.blue_limit = blue_limit
    
    @classmethod
    def from_json(cls, file: TextIOWrapper):
        data = json.loads(file.read())
        return cls(
            red_limit=data.get('red', 0),
            green_limit=data.get('green', 0),
            blue_limit=data.get('blue', 0)
        )
