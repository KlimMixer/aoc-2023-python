import os

from aoc_2023.solutions.day_one import callibrate, parse_task_one, parse_task_two
from aoc_2023.solutions.day_two.calculators.calculator_task_one import CalculatorTaskOne
from aoc_2023.solutions.day_two.calculators.calculator_task_two import CalculatorTaskTwo
from aoc_2023.solutions.day_two.config import Config
from aoc_2023.solutions.day_two.parse_strategy import ParseStrategy
from aoc_2023.solutions.day_two.validator import Validator

if __name__ == '__main__':
    print('-' * 10 + '[ DAY  01 ]' + '-' * 10)
    print(' ' * 5 + '-' * 5 + '[ TASK 01 ]' + '-' * 5)
    with open(os.path.realpath('./inputs/day_one_input.txt'), 'r', encoding='UTF-8') as input_file:
        print('Result: ', callibrate(input_file.read(), parse_task_one))
    print(' ' * 5 + '-' * 5 + '[ TASK 02 ]' + '-' * 5)
    with open(os.path.realpath('./inputs/day_one_input.txt'), 'r', encoding='UTF-8') as input_file:
        print('Result: ', callibrate(input_file.read(), parse_task_two))

    print('-' * 10 + '[ DAY  02 ]' + '-' * 10)
    print(' ' * 5 + '-' * 5 + '[ TASK 01 ]' + '-' * 5)
    with open(
            os.path.realpath('./inputs/day_two_input/task_input.txt'),
            'r',
            encoding='UTF-8'
        ) as input_file, \
         open(
            os.path.realpath('./inputs/day_two_input/task_one_config.json'),
            'r',
            encoding='UTF-8'
        ) as config_file:

        config = Config(red=12, green=13, blue=14)
        validator = Validator(config=config)

        parser = ParseStrategy()
        calculator = CalculatorTaskOne(parser, validator)
        print('Result: ', calculator.calculate(input_file.read()))
    
    print(' ' * 5 + '-' * 5 + '[ TASK 02 ]' + '-' * 5)
    with open(
            os.path.realpath('./inputs/day_two_input/task_input.txt'),
            'r',
            encoding='UTF-8'
        ) as input_file:
        parser = ParseStrategy()
        calculator = CalculatorTaskTwo(parser, validator)
        print('Result: ', calculator.calculate(input_file.read()))