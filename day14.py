from typing import Dict, Tuple

import utils


def read_element_pairs_and_rules(filename: str) -> Tuple[Dict[str, int], Dict[str, str], Dict[str, int]]:
    lines = utils.read_file_lines(filename=filename)

    rules: Dict[str, str] = {}
    element_pair_count: Dict[str, int] = {}
    element_count: Dict[str, int] = {}
    for line in lines[2:]:
        pair, value = line.split(" -> ")
        element, _ = list(pair)
        element_count[element] = 0
        rules[pair] = value
        element_pair_count[pair] = 0

    last_element = None
    for element in lines[0]:
        element_count[element] += 1

        if last_element is not None:
            element_pair_count[last_element + element] += 1
        last_element = element

    return element_pair_count, rules, element_count


def polymerize(element_pair_count: Dict[str, int], rules: Dict[str, str], element_count: Dict[str, int], steps: int) -> int:
    for _ in range(steps):
        for element_pair, count in {**element_pair_count}.items():
            infix_element = rules[element_pair]

            element_pair_count[element_pair[0] + infix_element] += count
            element_pair_count[infix_element + element_pair[1]] += count
            element_pair_count[element_pair] -= count
            element_count[infix_element] += count
    return max(element_count.values()) - min(element_count.values())


if __name__ == "__main__":
    element_pair_count, rules, element_count = read_element_pairs_and_rules(filename="./input/day14.test")
    assert polymerize(element_pair_count={**element_pair_count}, rules=rules, element_count={**element_count}, steps=10) == 1588
    assert polymerize(element_pair_count={**element_pair_count}, rules=rules, element_count={**element_count}, steps=40) == 2188189693529

    element_pair_count, rules, element_count = read_element_pairs_and_rules(filename="./input/day14.input")
    print(f"Part 1: {polymerize(element_pair_count={**element_pair_count}, rules=rules, element_count={**element_count}, steps=10)}")
    print(f"Part 2: {polymerize(element_pair_count={**element_pair_count}, rules=rules, element_count={**element_count}, steps=40)}")
