"""Advent of code 2021 - Day 1 - Part 1"""
from aocd import get_data
from typing import List


def process_measurements(measurements: List[str]) -> int:
    prev_value: int = float('inf')
    increased_measurements: int = 0
    for measurement in measurements:
        if int(measurement) > prev_value:
            increased_measurements += 1

        prev_value = int(measurement)

    return increased_measurements


if __name__ == '__main__':
    print(
        process_measurements(get_data(
            session='53616c7465645f5fe300aa9818e9994ea9a0fc7bac997a1fab89013376f446dd07a36bf1c043e3b61f7ce3684605ace6',
            day=1,
            year=2021).split('\n'))
    )
