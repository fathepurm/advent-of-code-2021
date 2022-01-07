from aocd import get_data
from dataclasses import dataclass
from typing import List
import pprint

MAX_COORDINATE = float('-inf')


@dataclass
class Coordinates:
    x: int
    y: int


class Line:
    def __init__(self, start_coordinates: Coordinates, end_coordinates: Coordinates):
        self.start_x: int = start_coordinates.x
        self.start_y: int = start_coordinates.y
        self.end_x: int = end_coordinates.x
        self.end_y: int = end_coordinates.y
        global MAX_COORDINATE
        MAX_COORDINATE = max(MAX_COORDINATE, self.start_x, self.end_x, self.start_y, self.end_y)


def get_line_segments() -> Line:
    for line in data:
        coordinates = line.split(" -> ")
        yield Line(Coordinates(int(coordinates[0].split(',')[0]), int(coordinates[0].split(',')[1])),
                   Coordinates(int(coordinates[1].split(',')[0]), int(coordinates[1].split(',')[1])))


def parse_input_and_get_line_segments() -> None:
    l_s = get_line_segments()
    for line in l_s:
        lines.append(line)


def update_y_for_constant_x(x: int, column_index: int, increment_index_by: int):
    c_index = column_index
    while c_index <= (column_index + increment_index_by):
        matrix[x][c_index] += 1
        c_index += 1


def update_x_for_constant_y(y: int, row_index: int, increment_index_by: int):
    r_index = row_index
    while r_index <= (row_index + increment_index_by):
        matrix[r_index][y] += 1
        r_index += 1


def update_matrix():
    for line in lines:
        if line.start_x == line.end_x:
            update_y_for_constant_x(line.start_x, min(line.start_y, line.end_y), abs(line.start_y - line.end_y))
        elif line.start_y == line.end_y:
            update_x_for_constant_y(line.start_y, min(line.start_x, line.end_x), abs(line.start_x - line.end_x))


def get_cross_lines() -> int:
    number_of_overlapping_coordinates: int = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] >= 2:
                number_of_overlapping_coordinates += 1

    return number_of_overlapping_coordinates


if __name__ == '__main__':
    data = get_data(
        session='<TOKEN>',
        day=5,
        year=2021).split('\n')

    lines: List[Line] = []
    parse_input_and_get_line_segments()

    MAX_COORDINATE += 1
    matrix: List[List[int]] = [[0 for row in range(MAX_COORDINATE)] for column in range(MAX_COORDINATE)]
    update_matrix()

    print(get_cross_lines())
