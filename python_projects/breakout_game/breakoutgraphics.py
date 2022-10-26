"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball

# global variable
start_ball = False


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.window.add(self.paddle, (window_width-self.paddle_width) / 2, window_height-self.paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, (window_width - ball_radius * 2) / 2, (window_height - ball_radius * 2) / 2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.drop_ball)
        onmousemoved(self.move_paddle)
        # Draw bricks
        # self.brick_lst = []
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                # self.brick_lst.append(brick)
                self.window.add(brick, (brick_width+brick_spacing)*i,
                                brick_offset + (brick_height+brick_spacing)*j)
                if j/brick_rows < 0.2:
                    brick.fill_color = 'red'
                    brick.color = 'red'
                elif 0.2 <= j/brick_rows < 0.4:
                    brick.fill_color = 'orange'
                    brick.color = 'orange'
                elif 0.4 <= j/brick_rows < 0.6:
                    brick.fill_color = 'yellow'
                    brick.color = 'yellow'
                elif 0.6 <= j/brick_rows < 0.8:
                    brick.fill_color = 'green'
                    brick.color = 'green'
                else:
                    brick.fill_color = 'blue'
                    brick.color = 'blue'
        self.total_brick = brick_cols*brick_rows

    def move_paddle(self, mouse):
        if mouse.x-1/2*self.paddle_width <= 0:
            self.window.add(self.paddle, 0, self.window.height-self.paddle_offset)
        elif mouse.x+1/2*self.paddle_width >= self.window.width:
            self.window.add(self.paddle, self.window.width-self.paddle_width, self.window.height-self.paddle_offset)
        else:
            self.window.add(self.paddle, mouse.x-1/2*self.paddle_width, self.window.height-self.paddle_offset)

    def drop_ball(self, mouse):
        global start_ball
        if not start_ball:
            start_ball = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
            self.__dy = INITIAL_Y_SPEED

    def reset_ball(self):
        global start_ball
        self.__dx = 0
        self.__dy = 0
        start_ball = False
        self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height-self.ball.height)/2)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def reset_dx(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def detect_collisions(self):
        for i in range(2):
            for j in range(2):
                obj = self.window.get_object_at(self.ball.x + i * self.ball.width, self.ball.y + j * self.ball.height)
                if obj is not None:
                    return obj
        return None



