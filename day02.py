from typing import List, Tuple

import utils

DIRECTION_UP = "up"
DIRECTION_DOWN = "down"
DIRECTION_FORWARD = "forward"


def read_commands(filename: str) -> List[Tuple[str, int]]:
    lines = utils.read_file_lines(filename=filename)
    commands = []
    for line in lines:
        direction, units = line.split(" ")
        commands.append((direction, int(units)))
    return commands


def navigate(commands: List[Tuple[str, int]]) -> int:
    horizontal_position, depth = 0, 0
    for direction, units in commands:
        if direction == DIRECTION_UP:
            depth -= units
        elif direction == DIRECTION_DOWN:
            depth += units
        elif direction == DIRECTION_FORWARD:
            horizontal_position += units
    return horizontal_position * depth


def navigate_with_aim(commands: List[Tuple[str, int]]) -> int:
    horizontal_position, depth, aim = 0, 0, 0
    for direction, units in commands:
        if direction == DIRECTION_UP:
            aim -= units
        elif direction == DIRECTION_DOWN:
            aim += units
        elif direction == DIRECTION_FORWARD:
            horizontal_position += units
            depth += aim * units
    return horizontal_position * depth


if __name__ == "__main__":
    commands = read_commands(filename="input/day02.test")
    assert navigate(commands=commands) == 150
    assert navigate_with_aim(commands=commands) == 900

    commands = read_commands(filename="input/day02.input")
    print(f"Part 1: {navigate(commands=commands)}")
    print(f"Part 2: {navigate_with_aim(commands=commands)}")
