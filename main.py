import os

from aoc_2023.solutions.day_one import callibrate, parse_task_one, parse_task_two
from aoc_2023.solutions.day_two.config import Config
from aoc_2023.solutions.day_two.parsers.parse_task_one_strategy import ParseTaskOneStrategy
from aoc_2023.solutions.day_two.validator import Validator

if __name__ == '__main__':
    print('-' * 10 + '[ DAY  01 ]' + '-' * 10)
    print(' ' * 5 + '-' * 5 + '[ TASK 01 ]' + '-' * 5)
    with open(os.path.realpath('./inputs/day_one_input.txt'), 'r') as input_file:
        print('Result: ', callibrate(input_file.read(), parse_task_one))
    print(' ' * 5 + '-' * 5 + '[ TASK 02 ]' + '-' * 5)
    with open(os.path.realpath('./inputs/day_one_input.txt'), 'r') as input_file:
        print('Result: ', callibrate(input_file.read(), parse_task_two))
    print('-' * 10 + '[ DAY  02 ]' + '-' * 10)
    print(' ' * 5 + '-' * 5 + '[ TASK 01 ]' + '-' * 5)
    with open(os.path.realpath('./inputs/day_two_input/task_one.txt'), 'r') as input_file:
        with open(os.path.realpath('./inputs/day_two_input/task_one_config.json'), 'r') as config_file:
            config = Config.from_json(config_file)
            parser = ParseTaskOneStrategy()
            
            validator = Validator(parser=parser, config=config)
            print('Result: ', validator.validate(input_file.read()))
    