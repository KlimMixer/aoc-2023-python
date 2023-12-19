import unittest

from aoc_2023.solutions.day_two.config import Config
from aoc_2023.solutions.day_two.parsers.parse_task_one_strategy import ParseTaskOneStrategy
from aoc_2023.solutions.day_two.validator import Validator

class DayTwoTestCase(unittest.TestCase):
    def test_task_one(self):
        input_data = '''
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        '''

        config = Config(red_limit=12, green_limit=13, blue_limit=14)
        parser = ParseTaskOneStrategy()
        
        validator = Validator(parser=parser, config=config)

        self.assertEqual(
            first=validator.validate(games_log=input_data), 
            second=8, 
            msg='Task one not callibrated'
        )