from typing import Dict, List, Set, Tuple, Union

import utils


def read_entries(filename: str) -> List[Tuple[List[str], List[str]]]:
    lines = utils.read_file_lines(filename=filename)
    entries = []
    for line in lines:
        signal_patterns, segments = line.split(" | ")
        signal_patterns = ["".join(sorted(signal_pattern)) for signal_pattern in signal_patterns.split(" ")]
        segments = ["".join(sorted(segment)) for segment in segments.split(" ")]
        entries.append((signal_patterns, segments))
    return entries


def identify_signal_patterns(signal_patterns: List[str]) -> Dict[str, int]:
    signal_pattern_number_xref: Dict[str, int] = {}
    number_signal_pattern_xref: Dict[int, str] = {}

    while len(number_signal_pattern_xref) < 10:
        for signal_pattern in signal_patterns:
            if signal_pattern not in signal_pattern_number_xref:
                identified_number = None

                if len(signal_pattern) == 2:
                    identified_number = 1
                elif len(signal_pattern) == 3:
                    identified_number = 7
                elif len(signal_pattern) == 4:
                    identified_number = 4
                elif len(signal_pattern) == 7:
                    identified_number = 8
                elif len(signal_pattern) == 6:
                    if 4 in number_signal_pattern_xref and set(number_signal_pattern_xref[4]).issubset(set(signal_pattern)):
                        identified_number = 9
                    elif (
                        1 in number_signal_pattern_xref
                        and 9 in number_signal_pattern_xref
                        and set(number_signal_pattern_xref[1]).issubset(set(signal_pattern))
                    ):
                        identified_number = 0
                    elif 0 in number_signal_pattern_xref:
                        identified_number = 6
                elif len(signal_pattern) == 5:
                    if 1 in number_signal_pattern_xref and set(number_signal_pattern_xref[1]).issubset(set(signal_pattern)):
                        identified_number = 3
                    elif 6 in number_signal_pattern_xref and set(signal_pattern).issubset(set(number_signal_pattern_xref[6])):
                        identified_number = 5
                    elif 5 in number_signal_pattern_xref and set(signal_pattern).issubset(set(number_signal_pattern_xref[8])):
                        identified_number = 2

                if identified_number is not None:
                    signal_pattern_number_xref[signal_pattern] = identified_number
                    number_signal_pattern_xref[identified_number] = signal_pattern
    return signal_pattern_number_xref


def count_numbers(entries: List[Tuple[List[str], List[str]]], numbers: List[int]) -> int:
    number_count = 0
    for signal_patterns, display in entries:
        identified_signal_patterns = identify_signal_patterns(signal_patterns=signal_patterns)
        for segment in display:
            number = identified_signal_patterns[segment]
            if number in numbers:
                number_count += 1

    return number_count


def sum_displays(entries: List[Tuple[List[str], List[str]]]) -> int:
    displays_sum = 0
    for signal_patterns, display in entries:
        identified_signal_patterns = identify_signal_patterns(signal_patterns=signal_patterns)
        display_value = int("".join([str(identified_signal_patterns[segment]) for segment in display]))
        displays_sum += display_value
    return displays_sum


if __name__ == "__main__":
    entries = read_entries(filename="./input/day08.test")
    assert count_numbers(entries=entries, numbers=[1, 4, 7, 8]) == 26
    assert sum_displays(entries=entries) == 61229

    entries = read_entries(filename="./input/day08.input")
    print(f"Part 1: {count_numbers(entries=entries, numbers=[1, 4, 7, 8])}")
    print(f"Part 2: {sum_displays(entries=entries)}")
