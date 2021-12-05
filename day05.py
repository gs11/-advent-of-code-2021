from typing import Dict, List

import utils


def get_vents(filename: str) -> List[List[int]]:
    vents = []
    for line in utils.read_file_lines(filename=filename):
        vents.append([int(position) for vent in line.split(" -> ") for position in vent.split(",")])
    return vents


def place_vents(vents: List[List[int]], use_diagonal_vents: bool) -> Dict[int, Dict[int, int]]:
    map: Dict[int, Dict[int, int]] = {}

    for vent in vents:
        from_x, from_y, to_x, to_y = vent

        if from_x < to_x:
            x_step_size = 1
        elif from_x > to_x:
            x_step_size = -1
        else:
            x_step_size = 0

        if from_y < to_y:
            y_step_size = 1
        elif from_y > to_y:
            y_step_size = -1
        else:
            y_step_size = 0

        x = from_x
        y = from_y

        if (from_x == to_x or from_y == to_y) or use_diagonal_vents is True:
            vent_length = max(abs(from_x - to_x), abs(from_y - to_y)) + 1
            for _ in range(vent_length):
                if y not in map:
                    map[y] = {}
                if x not in map[y]:
                    map[y][x] = 1
                else:
                    map[y][x] += 1

                x += x_step_size
                y += y_step_size
    return map


def find_dangerous_points(vents: List[List[int]], use_diagonal_vents: bool = False) -> int:
    map = place_vents(vents=vents, use_diagonal_vents=use_diagonal_vents)
    dangerous_points = []
    for x in map.values():
        dangerous_points.extend([count for count in x.values() if count > 1])
    return len(dangerous_points)


if __name__ == "__main__":
    vents = get_vents(filename="./input/day05.test")
    assert find_dangerous_points(vents=vents) == 5
    assert find_dangerous_points(vents=vents, use_diagonal_vents=True) == 12

    vents = get_vents(filename="./input/day05.input")
    print(f"Part 1: {find_dangerous_points(vents=vents)}")
    print(f"Part 2: {find_dangerous_points(vents=vents, use_diagonal_vents=True)}")
