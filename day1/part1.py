"""Advent of code 2021 - Day 1 - Part 1"""
from aocd import get_data
from typing import List


def process_measurements(measurements: List[str]) -> int:
    """

    :param measurements: List of input measurements
    :return: Number of increased measurements
    """
    previous_depth: int = float('inf')
    increased_measurements: int = 0

    for measurement in measurements:
        increased_measurements = increased_measurements + 1 if int(measurement) > previous_depth else increased_measurements
        previous_depth = int(measurement)

    return increased_measurements


if __name__ == '__main__':
    print(
        process_measurements(get_data(
            session='<TOKEN>',
            day=1,
            year=2021).split('\n'))
    )
