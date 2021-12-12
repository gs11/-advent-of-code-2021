from typing import Dict, List

import utils


def read_caves(filename: str) -> Dict[str, List[str]]:
    caves: Dict[str, List[str]] = {}
    for line in utils.read_file_lines(filename=filename):
        from_cave, to_cave = line.split("-")

        if from_cave not in caves:
            caves[from_cave] = []
        if to_cave not in caves and to_cave != "end":
            caves[to_cave] = []

        if to_cave != "start":
            caves[from_cave].append(to_cave)

        if from_cave != "start" and to_cave != "end":
            caves[to_cave].append(from_cave)
    return caves


def has_a_small_cave_been_visited_twice(caves_in_path: List[str]) -> bool:
    visited_caves = {cave: caves_in_path.count(cave) for cave in caves_in_path if cave.islower()}
    return [visited_cave for visited_cave, count in visited_caves.items() if count > 1] != []


def find_unique_paths(caves: Dict[str, List[str]], from_cave: str, distinct_paths: int, caves_in_path: List[str], one_small_cave_twice: bool) -> int:
    caves_in_path_cloned = [cave for cave in caves_in_path]
    caves_in_path_cloned.append(from_cave)

    small_cave_visited_twice = has_a_small_cave_been_visited_twice(caves_in_path=caves_in_path_cloned)

    for to_cave in caves.get(from_cave, []):
        if to_cave == "end":
            distinct_paths += 1
        elif (
            to_cave.isupper()
            or (one_small_cave_twice is False and to_cave not in caves_in_path_cloned)
            or (one_small_cave_twice is True and (small_cave_visited_twice is False or to_cave not in caves_in_path_cloned))
        ):
            distinct_paths = find_unique_paths(
                caves=caves,
                from_cave=to_cave,
                distinct_paths=distinct_paths,
                caves_in_path=caves_in_path_cloned,
                one_small_cave_twice=one_small_cave_twice,
            )
    return distinct_paths


if __name__ == "__main__":
    caves = read_caves(filename="./input/day12.test")
    assert find_unique_paths(caves=caves, from_cave="start", distinct_paths=0, caves_in_path=[], one_small_cave_twice=False) == 226
    assert find_unique_paths(caves=caves, from_cave="start", distinct_paths=0, caves_in_path=[], one_small_cave_twice=True) == 3509

    caves = read_caves(filename="./input/day12.input")
    unique_paths = find_unique_paths(caves=caves, from_cave="start", distinct_paths=0, caves_in_path=[], one_small_cave_twice=False)
    print(f"Part 1: {unique_paths}")
    unique_paths = find_unique_paths(caves=caves, from_cave="start", distinct_paths=0, caves_in_path=[], one_small_cave_twice=True)
    print(f"Part 2: {unique_paths}")
