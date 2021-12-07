from typing import Dict, List

import utils

fuel_consumption_cache: Dict[int, int] = {}


def calculate_increasing_fuel_consumption(steps: int) -> int:
    if steps in fuel_consumption_cache:
        return fuel_consumption_cache[steps]
    else:
        fuel_consumption_cache[steps] = sum(range(0, steps + 1))
        return fuel_consumption_cache[steps]


def find_most_efficient_alignment(crabs: List[int], increasing_fuel_consumption: bool = False) -> int:
    leftmost_position, rightmost_position = min(crabs), max(crabs)

    fuel_consumptions = []
    for position in range(leftmost_position, rightmost_position + 1):
        position_fuel_consumption = 0
        for crab in crabs:
            steps = abs(crab - position)
            if increasing_fuel_consumption is True:
                position_fuel_consumption += calculate_increasing_fuel_consumption(steps)
            else:
                position_fuel_consumption += steps
        fuel_consumptions.append(position_fuel_consumption)
    return min(fuel_consumptions)


if __name__ == "__main__":
    crabs = [int(crab) for crab in utils.read_file_lines(filename="./input/day07.test")[0].split(",")]
    assert find_most_efficient_alignment(crabs=crabs) == 37
    assert find_most_efficient_alignment(crabs=crabs, increasing_fuel_consumption=True) == 168

    crabs = [int(crab) for crab in utils.read_file_lines(filename="./input/day07.input")[0].split(",")]
    print(f"Part 1: {find_most_efficient_alignment(crabs=crabs)}")
    print(f"Part 2: {find_most_efficient_alignment(crabs=crabs, increasing_fuel_consumption=True)}")
