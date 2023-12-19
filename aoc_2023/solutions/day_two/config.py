from io import TextIOWrapper
import json
from dataclasses import dataclass


@dataclass
class Config:
    red: int
    green: int
    blue: int

    @classmethod
    def from_json(cls, file: TextIOWrapper):
        data = json.loads(file.read())
        return cls(
            red=data.get('red', 0),
            green=data.get('green', 0),
            blue=data.get('blue', 0)
        )
