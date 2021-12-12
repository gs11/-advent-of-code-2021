from typing import Dict, Set, Tuple

import utils


def read_octopi(filename: str) -> Dict[int, Dict[int, int]]:
    points: Dict[int, Dict[int, int]] = {}
    lines = utils.read_file_lines(filename=filename)
    for y, line in enumerate(lines):
        points[y] = {}
        for x, point in enumerate(line):
            points[y][x] = int(point)
    return points


def increase_adjacent_octopi_energy_levels(octopi: Dict[int, Dict[int, int]], y: int, x: int) -> Dict[int, Dict[int, int]]:
    adjacent_coordinates = [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y, x - 1), (y, x + 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]

    for adjacent_y, adjacent_x in adjacent_coordinates:
        if adjacent_y in octopi and adjacent_x in octopi[adjacent_y]:
            octopi[adjacent_y][adjacent_x] += 1
    return octopi


def get_to_be_flashed_octopi(octopi: Dict[int, Dict[int, int]]) -> int:
    return len([octopus for row in octopi.values() for octopus in row.values() if octopus > 9])


def flash_octopi(octopi: Dict[int, Dict[int, int]]) -> int:
    flashed_octopi: Set[Tuple[int, int]] = set()
    energy_increased_octopi: Set[Tuple[int, int]] = set()
    while not energy_increased_octopi or get_to_be_flashed_octopi(octopi=octopi):
        for y in octopi:
            for x in octopi[y]:
                if octopi[y][x] > 9 and (y, x) not in flashed_octopi:
                    flashed_octopi.add((y, x))
                    increase_adjacent_octopi_energy_levels(octopi=octopi, y=y, x=x)
                elif (y, x) not in energy_increased_octopi:
                    octopi[y][x] += 1
                    energy_increased_octopi.add((y, x))
        for y, x in flashed_octopi:
            octopi[y][x] = 0
    return len(flashed_octopi)


def repeat_energy_increase_cycles(octopi: Dict[int, Dict[int, int]], no_steps: int) -> int:
    number_of_flashes = 0
    for _ in range(no_steps):
        number_of_flashes += flash_octopi(octopi=octopi)
    return number_of_flashes


def get_steps_until_synchronized_flash(octopi: Dict[int, Dict[int, int]]) -> int:
    number_of_octopi = len([octopus for row in octopi.values() for octopus in row.values()])
    executed_steps = 0
    while True:
        number_of_flashed_octopi = flash_octopi(octopi=octopi)
        executed_steps += 1
        if number_of_flashed_octopi == number_of_octopi:
            break
    return executed_steps


if __name__ == "__main__":
    octopi = read_octopi(filename="./input/day11.test")
    assert repeat_energy_increase_cycles(octopi=octopi, no_steps=100) == 1656

    octopi = read_octopi(filename="./input/day11.test")
    assert get_steps_until_synchronized_flash(octopi=octopi) == 195

    octopi = read_octopi(filename="./input/day11.input")
    print(f"Part 1: {repeat_energy_increase_cycles(octopi=octopi, no_steps=100)}")

    octopi = read_octopi(filename="./input/day11.input")
    print(f"Part 1: {get_steps_until_synchronized_flash(octopi=octopi)}")
