from snake import SnakeGame
from settings import (
    BORDER_COLLISION,
    BOARD_X_SIZE,
    BOARD_Y_SIZE,
    FPS
)
import asyncio


async def main():
    snake = SnakeGame(
        x=BOARD_X_SIZE,
        y=BOARD_Y_SIZE,
        fps=FPS,
        border_collision=BORDER_COLLISION
    )

    await asyncio.gather(
        snake.bind_update(),
        snake.run_update()
    )

asyncio.run(main())
