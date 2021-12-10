from typing import List, Optional

import utils

CHUNK_CHARACTERS = {"(": ")", "[": "]", "{": "}", "<": ">"}
ILLEGAL_CHARACTER_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
CLOSING_CHARACTER_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def get_first_illegal_character(line: str) -> Optional[str]:
    open_chunk_characters = []
    for char in line:
        if char in CHUNK_CHARACTERS.keys():
            open_chunk_characters.append(char)
        elif char in CHUNK_CHARACTERS.values() and char == CHUNK_CHARACTERS[open_chunk_characters[-1]]:
            open_chunk_characters.pop()
        else:
            return char
    return None


def get_autocomplete_chunk_characters(line: str) -> Optional[List[str]]:
    open_chunk_characters = []
    for char in line:
        if char in CHUNK_CHARACTERS.keys():
            open_chunk_characters.append(char)
        elif char in CHUNK_CHARACTERS.values() and char == CHUNK_CHARACTERS[open_chunk_characters[-1]]:
            open_chunk_characters.pop()
        else:
            return None
    open_chunk_characters.reverse()
    return [CHUNK_CHARACTERS[open_chunk_character] for open_chunk_character in open_chunk_characters]


def get_syntax_error_score(lines: List[str]) -> int:
    syntax_error_score = 0
    for line in lines:
        first_illegal_character = get_first_illegal_character(line)
        if first_illegal_character:
            syntax_error_score += ILLEGAL_CHARACTER_SCORES[first_illegal_character]
    return syntax_error_score


def get_middle_autocomplete_score(lines: List[str]) -> int:
    line_scores = []
    for line in lines:
        autocomplete_chunk_characters = get_autocomplete_chunk_characters(line)
        if autocomplete_chunk_characters:
            line_score = 0
            for autocomplete_chunk_character in autocomplete_chunk_characters:
                line_score *= 5
                line_score += CLOSING_CHARACTER_SCORES[autocomplete_chunk_character]
            line_scores.append(line_score)
    line_scores.sort()
    return line_scores[int((len(line_scores) - 1) / 2)]


if __name__ == "__main__":
    lines = utils.read_file_lines("./input/day10.test")
    assert get_syntax_error_score(lines=lines) == 26397
    assert get_middle_autocomplete_score(lines=lines) == 288957

    lines = utils.read_file_lines("./input/day10.input")
    print(f"Part 1: {get_syntax_error_score(lines=lines)}")
    print(f"Part 2: {get_middle_autocomplete_score(lines=lines)}")
