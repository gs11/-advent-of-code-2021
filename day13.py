from typing import Dict, List, Tuple

import utils


def read_paper(filename: str) -> Tuple[Dict[int, Dict[int, str]], List[Tuple[str, int]]]:
    paper: Dict[int, Dict[int, str]] = {}
    folds = []
    for line in utils.read_file_lines(filename=filename):
        if line.startswith("fold"):
            orientation, position = line.replace("fold along ", "").split("=")
            folds.append((orientation, int(position)))
        elif line != "":
            x, y = [int(position) for position in line.split(",")]
            if y not in paper:
                paper[y] = {}
            paper[y][x] = "#"
    return paper, folds


def print_paper(paper: Dict[int, Dict[int, str]]) -> None:
    for y in range(max(paper) + 1):
        line = ""
        for x in range(max(paper[y]) + 1):
            line += str(paper.get(y, {}).get(x, "."))
        print(line)


def count_dots(paper: Dict[int, Dict[int, str]]) -> int:
    return len([point for y in paper.values() for point in y.values()])


def fold_paper(paper: Dict[int, Dict[int, str]], folds: List[Tuple[str, int]]) -> int:
    for orientation, position in folds:
        if orientation == "y":
            for y in range(position + 1, max(paper) + 1):
                if y in paper:
                    mirrored_y = position * 2 - y
                    if mirrored_y not in paper:
                        paper[mirrored_y] = {}
                    paper[mirrored_y].update(paper[y])
                    del paper[y]
        else:
            for y in range(max(paper) + 1):
                if y in paper:
                    for x in range(position + 1, max(paper[y]) + 1):
                        if x in paper[y]:
                            mirrored_x = position * 2 - x
                            paper[y][mirrored_x] = paper[y][x]
                            del paper[y][x]
    return count_dots(paper=paper)


if __name__ == "__main__":
    paper, folds = read_paper(filename="./input/day13.test")
    assert fold_paper(paper=paper, folds=folds[0:1]) == 17
    fold_paper(paper=paper, folds=folds)

    paper, folds = read_paper(filename="./input/day13.input")
    print(f"Part 1: {fold_paper(paper=paper, folds=folds[0:1])}")
    fold_paper(paper=paper, folds=folds)
    print("Part 2:")
    print_paper(paper)
