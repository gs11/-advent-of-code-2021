from typing import Dict, List

import utils


def split_line_to_numbers(line: str) -> List[int]:
    numbers = []
    for index in range(0, len(line), 3):
        numbers.append(int(line[index : index + 3]))
    return numbers


def get_boards(numbers_and_boards: List[str]) -> Dict[int, List[List[int]]]:
    boards: Dict[int, List[List[int]]] = {}
    current_board_number = 0
    rows = []
    for row in numbers_and_boards[2:]:
        if row:
            rows.append(split_line_to_numbers(row))
            if len(rows) == 5:
                boards[current_board_number] = rows
                current_board_number += 1
                rows = []
    return boards


def board_has_bingo(board: List[List[int]], drawn_numbers: List[int]) -> bool:
    # Horizontal rows
    for row in board:
        if set(row).issubset(set(drawn_numbers)):
            return True

    # Vertical lines
    for column_index in range(len(row)):
        column_numbers = [row[column_index] for row in board]
        if set(column_numbers).issubset(set(drawn_numbers)):
            return True

    return False


def get_sum_of_remaining_numbers(board: List[List[int]], drawn_numbers: List[int]) -> int:
    remaining_numbers = set([number for row in board for number in row]) - set(drawn_numbers)
    return sum(remaining_numbers) * drawn_numbers[-1]


def play_bingo(numbers_and_boards: List[str], play_until_last: bool) -> int:
    numbers = [int(number) for number in numbers_and_boards[0].split(",")]
    boards = get_boards(numbers_and_boards)

    bingoed_boards = []
    last_bingoed_drawn_numbers = []

    for no_drawn_numbers in range(len(numbers)):
        drawn_numbers = numbers[: no_drawn_numbers + 1]
        for board_number, board in boards.items():
            bingo = board_has_bingo(board=board, drawn_numbers=drawn_numbers)
            if bingo and board_number not in bingoed_boards:
                bingoed_boards.append(board_number)
                if play_until_last is False:
                    return get_sum_of_remaining_numbers(board=board, drawn_numbers=drawn_numbers)
                last_bingoed_drawn_numbers = drawn_numbers

    return get_sum_of_remaining_numbers(board=boards[bingoed_boards[-1]], drawn_numbers=last_bingoed_drawn_numbers)


if __name__ == "__main__":
    numbers_and_boards = utils.read_file_lines(filename="./input/day04.test")
    assert play_bingo(numbers_and_boards=numbers_and_boards, play_until_last=False) == 4512
    assert play_bingo(numbers_and_boards=numbers_and_boards, play_until_last=True) == 1924

    numbers_and_boards = utils.read_file_lines(filename="./input/day04.input")
    print(f"Part 1: {play_bingo(numbers_and_boards=numbers_and_boards, play_until_last=False)}")
    print(f"Part 2: {play_bingo(numbers_and_boards=numbers_and_boards, play_until_last=True)}")
