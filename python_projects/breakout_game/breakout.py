"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts

# global variable
remove_brick = 0


def main():
    global remove_brick
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        if lives > 0:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx()
            if graphics.ball.y <= 0:
                graphics.set_dy()
            if graphics.ball.y >= graphics.window.height:
                graphics.reset_ball()
                lives -= 1
                if lives == 0:
                    break
            may_be_obj = graphics.detect_collisions()
            if may_be_obj is not None:
                if may_be_obj is not graphics.paddle:  # hit bricks
                    graphics.window.remove(may_be_obj)
                    remove_brick += 1
                    if remove_brick == graphics.total_brick:
                        graphics.window.clear()
                        break
                    graphics.set_dy()
                else:  # hit paddle
                    if graphics.get_dy() > 0:
                        graphics.set_dy()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
