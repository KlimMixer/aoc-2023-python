import re
from typing import Callable, TypeAlias

Parser: TypeAlias = Callable[[str], int]

def parse_task_one(line: str) -> int:
    digits_regexp = re.compile(r'(\d)')
    if digits := digits_regexp.findall(line):
        return int(digits[0] + digits[-1])
    return 0

def parse_task_two(line: str) -> int:
    digits_regexp = re.compile(r'(\d)')
    digits_and_text_regexp = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
    text_to_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    if digits := digits_and_text_regexp.findall(line):
        first_digit = digits[0]
        last_digit = digits[-1]
        if digits_regexp.match(first_digit) is None:
            first_digit = text_to_digit[first_digit]
        if digits_regexp.match(last_digit) is None:
            last_digit = text_to_digit[last_digit]
        return int(first_digit + last_digit)

    return 0

def callibrate(lines: str, parser: Parser) -> int:
    parsed_lines = map(parser, lines.split('\n'))
    return sum(parsed_lines)

if __name__ == "__main__":
    print()