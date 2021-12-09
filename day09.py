from typing import Dict, List, Set, Tuple

import utils


class Point:
    def __init__(self, x: int, y: int, height: int):
        self.x = x
        self.y = y
        self.height = height

    def __str__(self) -> str:
        return f"Point(x={self.x}, y={self.y}, height={self.height})"


def read_cave(filename: str) -> Dict[int, Dict[int, int]]:
    points: Dict[int, Dict[int, int]] = {}
    lines = utils.read_file_lines(filename=filename)
    for y, line in enumerate(lines):
        points[y] = {}
        for x, point in enumerate(line):
            points[y][x] = int(point)
    return points


def get_adjacent_points(cave: Dict[int, Dict[int, int]], x: int, y: int) -> List[Point]:
    adjacent_points = [
        Point(x=x - 1, y=y, height=cave.get(y, {}).get(x - 1, -1)),
        Point(x=x + 1, y=y, height=cave.get(y, {}).get(x + 1, -1)),
        Point(x=x, y=y - 1, height=cave.get(y - 1, {}).get(x, -1)),
        Point(x=x, y=y + 1, height=cave.get(y + 1, {}).get(x, -1)),
    ]
    return [point for point in adjacent_points if point.height != -1]  # Remove out of bounds


def get_lowest_adjacent_point(points: List[Point]) -> int:
    lowest_point = min(points, key=lambda point: point.height)
    return lowest_point.height


def get_lowest_points(cave: Dict[int, Dict[int, int]]) -> List[Point]:
    low_points: List[Point] = []
    for y in cave.keys():
        for x in cave[y]:
            current_height = cave[y][x]
            adjacent_points = get_adjacent_points(cave=cave, x=x, y=y)

            if current_height < get_lowest_adjacent_point(points=adjacent_points):
                low_points.append(Point(x=x, y=y, height=current_height))
    return low_points


def traverse_basin(cave: Dict[int, Dict[int, int]], current_point: Point, visited_coordinates: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    if current_point.height != 9:
        visited_coordinates.add((current_point.x, current_point.y))
        for adjacent_point in get_adjacent_points(cave=cave, x=current_point.x, y=current_point.y):
            if adjacent_point.height > current_point.height and (adjacent_point.x, adjacent_point.y) not in visited_coordinates:
                traverse_basin(cave=cave, current_point=adjacent_point, visited_coordinates=visited_coordinates)
    return visited_coordinates


def calculate_risk_level_sum(cave: Dict[int, Dict[int, int]]) -> int:
    risk_level_sum = 0
    for point in get_lowest_points(cave=cave):
        risk_level_sum += point.height + 1
    return risk_level_sum


def get_product_of_largest_basins(cave: Dict[int, Dict[int, int]]) -> int:
    basin_sizes = []
    for lowest_point in get_lowest_points(cave=cave):
        basin_points = traverse_basin(cave=cave, current_point=lowest_point, visited_coordinates=set())
        basin_sizes.append(len(basin_points))
    basin_sizes.sort(reverse=True)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    cave = read_cave("./input/day09.test")
    assert calculate_risk_level_sum(cave=cave) == 15
    assert get_product_of_largest_basins(cave=cave) == 1134

    cave = read_cave("./input/day09.input")
    print(f"Part 1: {calculate_risk_level_sum(cave=cave)}")
    print(f"Part 2: {get_product_of_largest_basins(cave=cave)}")
