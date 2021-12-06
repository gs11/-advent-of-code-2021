from typing import Dict

import utils


def initialize_empty_school_of_fish() -> Dict[int, int]:
    return {days_left: 0 for days_left in range(9)}


def read_school_of_fish(filename: str) -> Dict[int, int]:
    school_of_fish = initialize_empty_school_of_fish()
    for fish in utils.read_file_lines(filename=filename)[0].split(","):
        school_of_fish[int(fish)] += 1
    return school_of_fish


def lifecycle_school_of_fish(school_of_fish: Dict[int, int], days: int) -> int:
    for _ in range(days):
        updated_school_of_fish = initialize_empty_school_of_fish()
        for days_left, number_of_fish in school_of_fish.items():
            if days_left == 0:
                updated_school_of_fish[6] += number_of_fish
                updated_school_of_fish[8] += number_of_fish
            else:
                updated_school_of_fish[days_left - 1] += number_of_fish
        school_of_fish = updated_school_of_fish
    return sum(school_of_fish.values())


if __name__ == "__main__":
    school_of_fish = read_school_of_fish(filename="./input/day06.test")
    assert lifecycle_school_of_fish(school_of_fish=school_of_fish, days=80) == 5934
    assert lifecycle_school_of_fish(school_of_fish=school_of_fish, days=256) == 26984457539

    school_of_fish = read_school_of_fish(filename="./input/day06.input")
    print(f"Part 1: {lifecycle_school_of_fish(school_of_fish=school_of_fish, days=80)}")
    print(f"Part 2: {lifecycle_school_of_fish(school_of_fish=school_of_fish, days=256)}")
