from typing import List, Any
import os


class Board:
    def __init__(self, size_x: int, size_y: int):
        self.board: List[Any] = [[0 for x in range(size_x + 2)] for y in range(size_y + 2)]  # noqa: E501
        self.size_x = size_x
        self.size_y = size_y

        self._create_border()

    def _create_border(self) -> None:
        """Creates border in board"""

        for x_index, x in enumerate(self.board[0]):
            self.board[0][x_index] = 1

        for x_index, x in enumerate(self.board[-1]):
            self.board[-1][x_index] = 1

        for y in self.board:
            y[0] = 1
            y[-1] = 1

    def clear(self) -> None:
        """Clears board and console"""

        self.board = [[0 for x in range(self.size_x + 2)] for y in range(self.size_y + 2)]  # noqa: E501

        self._create_border()
        os.system('cls')

    def update(self) -> None:
        """Clears console and draws board"""

        for_draw = ''

        for y in self.board:
            for x in y:
                if x == 'apple':
                    for_draw += '@'

                elif x:
                    for_draw += '#'

                else:
                    for_draw += ' '

            for_draw += '\n'

        self.clear()

        print(for_draw)
