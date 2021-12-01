from typing import Any, List


def read_file_lines(filename: str, split_by: str = "\n") -> List[Any]:
    with open(filename, "r") as data:
        return data.read().split(split_by)
