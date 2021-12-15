"""Advent of code 2021 - Day 1 - Part 2"""
from aocd import get_data
from typing import List


def max_increase_btw_window(measurements: List[int], window: int) -> int:
    index: int = 0
    count: int = 0
    max_window: int = float('inf')

    while index + 2 < len(measurements):
        current_window_sum = sum(measurements[index: index+3])
        if current_window_sum > max_window:
            count += 1

        max_window = current_window_sum
        index += 1
    return count


if __name__ == '__main__':
    print(
        max_increase_btw_window(list(map(int, get_data(
            session='<TOKEN>',
            day=1,
            year=2021).split('\n'))), window=3)
    )