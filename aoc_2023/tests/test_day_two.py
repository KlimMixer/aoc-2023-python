import unittest
from aoc_2023.solutions.day_two.calculators.calculator_task_one import CalculatorTaskOne
from aoc_2023.solutions.day_two.calculators.calculator_task_two import CalculatorTaskTwo

from aoc_2023.solutions.day_two.config import Config
from aoc_2023.solutions.day_two.parse_strategy import ParseStrategy
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

        config = Config(red=12, green=13, blue=14)
        validator = Validator(config=config)

        parser = ParseStrategy()
        calculator = CalculatorTaskOne(parser, validator)

        self.assertEqual(
            first=calculator.calculate(games_log=input_data),
            second=8,
            msg='Task one not callibrated'
        )

    def test_task_two(self):
        input_data = '''
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        '''

        config = Config(red=12, green=13, blue=14)
        validator = Validator(config=config)

        parser = ParseStrategy()
        calculator = CalculatorTaskTwo(parser, validator)

        self.assertEqual(
            first=calculator.calculate(games_log=input_data),
            second=2286,
            msg='Task two not callibrated'
        )
