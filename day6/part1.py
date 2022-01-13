from aocd import get_data
from dataclasses import dataclass
from typing import List
import pprint


@dataclass
class CountDays:
    original_days: int
    to_be_added_days: int


def update_to_be_added(day_idx: int, count) -> None:
    days_to_number_of_lantern_fish[day_idx].to_be_added_days += count


def update_original(day_idx: int) -> None:
    days_to_number_of_lantern_fish[day_idx].original_days -= days_to_number_of_lantern_fish[day_idx].original_days


class LanternFish:
    def __init__(self, days):
        self.number_of_days = days

    @staticmethod
    def pre_update(day_idx: int) -> None:
        if days_to_number_of_lantern_fish[day_idx].original_days > 0:
            if day_idx == 0:
                update_to_be_added(8, days_to_number_of_lantern_fish[day_idx].original_days)
                update_to_be_added(6, days_to_number_of_lantern_fish[day_idx].original_days)
            else:
                update_to_be_added(day_idx - 1, days_to_number_of_lantern_fish[day_idx].original_days)

            update_original(day_idx)

    @staticmethod
    def post_update() -> None:
        for day_idx in range(len(days_to_number_of_lantern_fish)):
            days_to_number_of_lantern_fish[day_idx].original_days += days_to_number_of_lantern_fish[day_idx].to_be_added_days
            days_to_number_of_lantern_fish[day_idx].to_be_added_days -= days_to_number_of_lantern_fish[day_idx].to_be_added_days

    def get_total_lantern_fish(self) -> int:
        for day in range(self.number_of_days):
            for day_idx in range(len(days_to_number_of_lantern_fish)):
                self.pre_update(day_idx)
            self.post_update()

        l_f_sum = 0
        for day in days_to_number_of_lantern_fish:
            l_f_sum += day.original_days

        return l_f_sum


def initialize(reproduction_cycle: int) -> List[CountDays]:
    return [CountDays(0, 0) for i in range(reproduction_cycle)]


def yield_input() -> int:
    for u_input in data.split(','):
        yield int(u_input)


def parse_input_and_update_dict() -> None:
    s_input = yield_input()
    for r_age in s_input:
        days_to_number_of_lantern_fish[r_age].original_days += 1


if __name__ == '__main__':
    data = get_data(
            session='<TOKEN>',
            day=6,
            year=2021)

    days_to_number_of_lantern_fish = initialize(reproduction_cycle=9)
    parse_input_and_update_dict()
    lantern_fish = LanternFish(days=80)
    print(lantern_fish.get_total_lantern_fish())
