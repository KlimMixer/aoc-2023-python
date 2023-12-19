import os

from aoc_2023.solutions.day_one import callibrate, parse_task_one, parse_task_two

if __name__ == '__main__':
    print('-' * 10 + '[ DAY  01 ]' + '-' * 10)
    print(' ' * 5 + '-' * 5 + '[ TASK 01 ]' + '-' * 5)
    with open(os.path.realpath('./inputs/day_one_input.txt'), 'r') as input_file:
        print('Result: ', callibrate(input_file.read(), parse_task_one))
    print(' ' * 5 + '-' * 5 + '[ TASK 02 ]' + '-' * 5)
    with open(os.path.realpath('./inputs/day_one_input.txt'), 'r') as input_file:
        print('Result: ', callibrate(input_file.read(), parse_task_two))