from typing import List, Optional

import utils


def get_most_common_bit(bits: List[str]) -> Optional[str]:
    number_of_zeroes = len([bit for bit in bits if bit == "0"])
    number_of_ones = len([bit for bit in bits if bit == "1"])
    if number_of_zeroes > number_of_ones:
        return "0"
    elif number_of_ones > number_of_zeroes:
        return "1"
    else:
        return None


def inverse_bit(bit: str) -> str:
    return str(int(not bool(int(bit))))


def get_rate(diagnostics: List[str], use_most_common_bit: bool = True) -> int:
    bit_string = ""
    for index in range(len(diagnostics[0])):
        most_common_bit = get_most_common_bit([diagnostic[index] for diagnostic in diagnostics])
        if most_common_bit:
            bit_string += most_common_bit if use_most_common_bit is True else inverse_bit(most_common_bit)
    return int(bit_string, 2)


def get_power_consumption(diagnostics: List[str]) -> int:
    gamma_rate = get_rate(diagnostics=diagnostics)
    epsilon_rate = get_rate(diagnostics=diagnostics, use_most_common_bit=False)
    return gamma_rate * epsilon_rate


def get_rating(diagnostics: List[str], default_most_common_bit: str, use_most_common_bit: bool = True) -> int:
    for index in range(len(diagnostics[0])):
        most_common_bit = get_most_common_bit([diagnostic[index] for diagnostic in diagnostics])
        if most_common_bit is not None:
            filter_by_bit = most_common_bit if use_most_common_bit is True else inverse_bit(most_common_bit)
        else:
            filter_by_bit = default_most_common_bit
        diagnostics = [diagnostic for diagnostic in diagnostics if diagnostic[index] == filter_by_bit]
        if len(diagnostics) == 1:
            break
    return int(diagnostics[0], 2)


def get_life_rating(diagnostics: List[str]) -> int:
    oxygen_generator_rating = get_rating(diagnostics=diagnostics, default_most_common_bit="1")
    co2_scrubber_rating = get_rating(diagnostics=diagnostics, default_most_common_bit="0", use_most_common_bit=False)
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    diagnostics = utils.read_file_lines(filename="./input/day03.test")
    assert get_power_consumption(diagnostics=diagnostics) == 198
    assert get_life_rating(diagnostics=diagnostics) == 230

    diagnostics = utils.read_file_lines(filename="./input/day03.input")
    print(f"Part 1: {get_power_consumption(diagnostics=diagnostics)}")
    print(f"Part 2: {get_life_rating(diagnostics=diagnostics)}")
