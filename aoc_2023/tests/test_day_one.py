import unittest
from aoc_2023.solutions.day_one import callibrate, parse_task_one, parse_task_two

class DayOneTestCase(unittest.TestCase):
    def test_task_one(self):
        input_data = '''
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
        '''
        self.assertEqual(
            first=callibrate(input_data, parse_task_one), 
            second=142, 
            msg='Task one not callibrated'
        )

    def test_task_two(self):
        input_data = '''
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
        '''
        self.assertEqual(
            first=callibrate(input_data, parse_task_two), 
            second=281, 
            msg='Task two not callibrated'
        )

if __name__ == '__main__':
    unittest.main()