from aocd import get_data
from typing import List
from dataclasses import dataclass


@dataclass
class SubmarineLocation:

    horizontal_pos: int
    depth: int


def move_forward(by_position: int, location: SubmarineLocation) -> None:
    location.horizontal_pos += by_position


def move_up(by_position: int, location: SubmarineLocation) -> None:
    location.depth -= by_position


def move_down(by_position: int, location: SubmarineLocation) -> None:
    location.depth += by_position


directions = {
    'up': move_up,
    'down': move_down,
    'forward': move_forward
}

if __name__ == '__main__':
    user_commands = get_data(session='<TOKEN>',
                             day=2,
                             year=2021).split('\n')

    submarineLocation = SubmarineLocation(0, 0)
    for command in user_commands:
        command_parts: List[str] = command.split(" ")
        directions[command_parts[0]](int(command_parts[1]), submarineLocation)

    print(submarineLocation.depth * submarineLocation.horizontal_pos)


