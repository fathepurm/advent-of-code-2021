from aocd import get_data
from dataclasses import dataclass
from typing import List, Sequence


@dataclass
class BitCount:
    zeros: int
    ones: int


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


def filter_o2_and_co2_message_bytes(msg_input: List[str], is_o2: bool, bit_index: int, message_bit_objects: List[BitCount]) -> Sequence[int]:
    bit = 1 if is_o2 else 0

    if len(msg_input) == 2:
        if int(msg_input[0][bit_index]) == int(msg_input[1][bit_index]):
            return msg_input
        elif message_bit_objects[bit_index].ones >= message_bit_objects[bit_index].zeros:
            return list(filter(lambda i: int(i[bit_index]) == bit, msg_input))
        else:
            return list(filter(lambda i: int(i[bit_index]) != bit, msg_input))

    if message_bit_objects[bit_index].ones >= message_bit_objects[bit_index].zeros:
        return list(filter(lambda i: int(i[bit_index]) == bit, msg_input))
    else:
        return list(filter(lambda i: int(i[bit_index]) != bit, msg_input))


if __name__ == '__main__':
    user_input = get_data(
        session='<TOKEN>',
        day=3,
        year=2021).split('\n')

    bit_index = 0
    o2_message_from_user_input, co2_message_from_user_input = user_input, user_input
    for bit_index in range(0, len(user_input[0])):
        if len(o2_message_from_user_input) != 1:
            o2_message_bit_objects = get_message_bit_objects(o2_message_from_user_input)
            o2_message_from_user_input = filter_o2_and_co2_message_bytes(msg_input=o2_message_from_user_input,
                                                                         is_o2=True,
                                                                         bit_index=bit_index,
                                                                         message_bit_objects=o2_message_bit_objects)

        if len(co2_message_from_user_input) != 1:
            co2_message_bit_objects = get_message_bit_objects(co2_message_from_user_input)
            co2_message_from_user_input = filter_o2_and_co2_message_bytes(msg_input=co2_message_from_user_input,
                                                                          is_o2=False,
                                                                          bit_index=bit_index,
                                                                          message_bit_objects=co2_message_bit_objects)

        if len(co2_message_from_user_input) == 1 and len(o2_message_from_user_input) == 1:
            break

    print(int(o2_message_from_user_input[0], 2) * int(co2_message_from_user_input[0], 2))
