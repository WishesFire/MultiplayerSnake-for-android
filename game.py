from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import *
from network.client import User
import json

# Resolution for sm
res_playground = [1600, 900]
apple_color = (1, 1, 0, 1)

# Settings
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', res_playground[0])
Config.set('graphics', 'height', res_playground[1])

# Moving
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

moving_values = {LEFT: [-1, 0],
                 UP: [0, 1],
                 RIGHT: [1, 0],
                 DOWN: [0, -1]}

touch_start_pos = ListProperty()
action = BooleanProperty()


# SnakePlayground
class Playground(Widget):
    fruit = ObjectProperty(None)

    score = NumericProperty(0)
    turn_counter = NumericProperty(0)
    fruit_score = NumericProperty(0)


# Add function(Apple)
class Apple(Widget):
    position = ObjectProperty(None)

    duration = NumericProperty(10)
    interval = NumericProperty(3)


# Full body Snake
class Snake(Widget):
    def __init__(self):
        super(Snake, self).__init__()
        self.size = (30, 30)
        self.pos = (200, 200)
        self.head = ObjectProperty(None)
        self.tail = ObjectProperty(None)

        self.snake_cord = ListProperty()
        self.direction = StringProperty(RIGHT, options=(LEFT, UP, RIGHT, DOWN))

    def start(self):
        Clock.schedule_interval(self.update, 0.01)

    def move(self):
        new_tail = list(self.head.position)
        self.head.move()
        self.tail.add_block(new_tail)

    def update_head_tail(self):
        self.head.remove()
        self.tail.remove()

    def update(self, *args):
        pass


class SnakeHead(Widget):
    x_position = NumericProperty(0)
    y_position = NumericProperty(0)
    position = ReferenceListProperty(x_position, y_position)


class SnakeTail(Widget):
    size = NumericProperty(3)
    block_positions_tail = ListProperty()

    def update_head_tail(self):
        self.size = 3

        for block in self.block_positions_tail:
            self.canvas.remove(block)


# Main control
class ControlAndroid:
    pass


class SnakeApp(App):
    game = ObjectProperty(None)

    def build(self):
        self.game_region = Playground()
        return self.game_region


if __name__ == "__main__":
    SnakeApp().run()