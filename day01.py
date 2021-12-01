from typing import List

import utils


def count_depth_increases(scans: List[int], window_size: int) -> int:
    depth_increases = 0
    previous_window_sum = None
    for index in range(len(scans)):
        window_sum = 0
        if index >= window_size - 1:
            window_sum = sum(scans[index - window_size + 1 : index + window_size])

            if previous_window_sum and window_sum > previous_window_sum:
                depth_increases += 1
        previous_window_sum = window_sum
    return depth_increases


if __name__ == "__main__":
    scans = [int(scan) for scan in utils.read_file_lines(filename="input/day01.test")]
    assert count_depth_increases(scans=scans, window_size=1) == 7
    assert count_depth_increases(scans=scans, window_size=3) == 5

    scans = [int(scan) for scan in utils.read_file_lines(filename="input/day01.input")]
    print(f"Part 1: {count_depth_increases(scans=scans, window_size=1)}")
    print(f"Part 2: {count_depth_increases(scans=scans, window_size=3)}")
