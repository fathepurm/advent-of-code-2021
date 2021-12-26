from aocd import get_data
from dataclasses import dataclass
from typing import List


@dataclass
class UserBingoBoards:
    board: List[List[str]]


def construct_puzzle_input_and_user_boards() -> (List[str], List[UserBingoBoards]):
    p_input: List[str] = data[0].split(',')
    u_boards: List[UserBingoBoards] = list()

    for index in range(1, len(data), 6):
        rows = [i.split(' ') for i in data[index+1:index+6]]
        u_boards.append(
            UserBingoBoards(list(list(filter(lambda values_inside:  values_inside != '', row)) for row in rows)))

    return p_input, u_boards


def mark_user_board(read_input: str) -> (bool, int):
    user_won = False
    board_sum = 0
    for board_index in range(0, len(user_boards)):
        user_board = user_boards[board_index].board
        for row_index in range(0, len(user_board)):
            if user_board[row_index].count(str(read_input)) == 1:
                column_index = user_board[row_index].index(read_input)
                user_board[row_index].remove(read_input)
                user_board[row_index].insert(column_index, '0')

                if has_user_board_won(user_board, row_index, column_index):
                    user_won = True
                    for row in user_board:
                        board_sum += sum(list(map(int, row)))
                break
        if user_won:
            break

    return user_won, board_sum


def has_user_board_won(user_board: List[List[str]], row_index: int, column_index: int) -> bool:
    if user_board[row_index].count('0') == 5:
        return True
    for row in user_board:
        if row[column_index] != '0':
            return False

    return True


def find_winner() -> None:
    for read_input in puzzle_input:
        user_won, board_sum = mark_user_board(read_input)

        if user_won:
            print(board_sum * int(read_input))
            break


if __name__ == '__main__':
    data = get_data(
        session='<TOKEN>',
        day=4,
        year=2021).split('\n')

    puzzle_input, user_boards = construct_puzzle_input_and_user_boards()
    find_winner()


