from snake_game.snake import SnakeGame
from settings import (
    BOARD_X_SIZE,
    BOARD_Y_SIZE,
    FPS
)
import asyncclick as click
import asyncio


@click.command()
@click.option('--x_size')
@click.option('--y_size')
@click.option('--fps')
@click.option('--border')
async def main(x_size, y_size, fps, border):
    snake = SnakeGame(
        x=int(x_size) if x_size else BOARD_X_SIZE,
        y=int(y_size) if y_size else BOARD_Y_SIZE,
        fps=int(fps) if fps else FPS,
        border_collision=bool(int(border) if border else 0)
    )

    await asyncio.gather(
        snake.bind_update(),
        snake.run_update()
    )

if __name__ == "__main__":
    main()
