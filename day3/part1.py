from aocd import get_data
from dataclasses import dataclass
from typing import List


@dataclass
class BitCount:
    zeros: int
    ones: int


@dataclass
class Message:
    gamma_rate: str
    epsilon_rate: str


def get_message_bit_objects(user_input: List[str]) -> List[BitCount]:
    number_of_bits: int = len(user_input[0])
    bit_count_objects: List[BitCount] = [BitCount(0, 0) for bit in range(0, number_of_bits)]
    read_each_message_at_index: int = 0

    while read_each_message_at_index < len(user_input):
        for bit_index in range(0, number_of_bits):
            if int(user_input[read_each_message_at_index][bit_index]) != 1:
                bit_count_objects[bit_index].zeros += 1
            else:
                bit_count_objects[bit_index].ones += 1
        read_each_message_at_index += 1

    return bit_count_objects


if __name__ == '__main__':
    message_bit_objects = get_message_bit_objects(
        get_data(
            session='<TOKEN>',
            day=3,
            year=2021).split('\n'))

    message = Message('', '')
    for objects in message_bit_objects:
        if objects.ones > objects.zeros:
            message.gamma_rate += '1'
            message.epsilon_rate += '0'
        else:
            message.epsilon_rate += '1'
            message.gamma_rate += '0'

    print(int(message.gamma_rate, 2) * int(message.epsilon_rate, 2))
