from typing import NoReturn, List, Optional
from random import randint
from snake_game.board import Board
from math import sqrt
from os import _exit
import keyboard
import asyncio


class SnakeGame:
    def __init__(
        self,
        x: int,
        y: int,
        fps: int = 6,
        border_collision: bool = False
    ):

        self.apple: Optional[List[int]] = []
        self.board = Board(x, y)
        self.snake = [[1, 1]]
        self.vector = {
            "Up": (0, -1),
            "Down": (0, 1),
            "Left": (-1, 0),
            "Right": (1, 0)
        }
        self.direction = self.vector['Right']
        self.sleep = 1 / fps
        self.border_collision = border_collision

    async def spawn_apple(self) -> None:
        """Spawns apple on the map"""

        apple = [randint(1, self.board.size_y), randint(1, self.board.size_x)]  # noqa: E501

        if apple in self.snake:
            await self.spawn_apple()

        else:
            self.apple = apple
            self.board.board[self.apple[0]][self.apple[1]] = 'apple'

    async def defeat(self) -> NoReturn:
        """Finishes game and close program"""

        print(f'You lose! Score: {len(self.snake) - 1}')

        _exit(0)

    async def update(self) -> None:
        """Game update frame"""

        await asyncio.sleep(self.sleep)

        if not self.apple:
            await self.spawn_apple()

        else:
            self.board.board[self.apple[0]][self.apple[1]] = 'apple'

        for element in self.snake:
            self.board.board[element[0]][element[1]] = 1

        self.board.update()

        y, x = self.snake[0]

        y += self.direction[1]
        x += self.direction[0]

        if self.border_collision:
            if y > self.board.size_y or y <= 0:
                await self.defeat()

            if x > self.board.size_x or x <= 0:
                await self.defeat()

        else:
            if y > self.board.size_y:
                y = 1

            elif y <= 0:
                y = self.board.size_y

            if x > self.board.size_x:
                x = 1

            elif x <= 0:
                x = self.board.size_x

        if self.apple and y == self.apple[0] and x == self.apple[1]:
            self.apple = []

        elif [y, x] in self.snake:
            await self.defeat()

        else:
            self.snake.pop()

        self.snake.insert(0, [y, x])

        print('* Press Escape to end the game')
        print('* WASD and arrows - movement')
        print('-------------------------------')
        print('* Board size:', self.board.size_x, 'x', self.board.size_y)
        print('* Snake length:', len(self.snake))
        print('* Apples collected:', len(self.snake)-1)
        print('* Current direction:', dict([(v, k) for k, v in self.vector.items()])[self.direction])  # noqa: E501
        print('* Border collision is', 'enabled' if self.border_collision else 'disabled')  # noqa: E501
        print('* Sleep between update:', round(self.sleep, 2))
        print('* FPS:', 1 / self.sleep)

        if self.apple:
            y_distance = (self.apple[0] - self.snake[0][0]) ** 2
            x_distance = (self.apple[1] - self.snake[0][1]) ** 2

            distance = sqrt(y_distance + x_distance)

            print('* Distance to apple:', round(distance, 0))

    async def bind_update(self) -> None:
        """Sets the direction by pressing the button"""

        while True:
            await asyncio.sleep(0.0001)

            if keyboard.is_pressed('w'):
                self.direction = self.vector['Up']

            if keyboard.is_pressed('s'):
                self.direction = self.vector['Down']

            if keyboard.is_pressed('a'):
                self.direction = self.vector['Left']

            if keyboard.is_pressed('d'):
                self.direction = self.vector['Right']

            if keyboard.is_pressed('up'):
                self.direction = self.vector['Up']

            if keyboard.is_pressed('down'):
                self.direction = self.vector['Down']

            if keyboard.is_pressed('left'):
                self.direction = self.vector['Left']

            if keyboard.is_pressed('right'):
                self.direction = self.vector['Right']

            if keyboard.is_pressed('escape'):
                await self.defeat()

    async def run_update(self):
        """Runs console update (without bind update)"""

        while True:
            await self.update()
