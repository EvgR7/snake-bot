import random

class Food():
    def __init__(self, width, height, snake_body):
        self.width = width
        self.height = height
        self.position = self._spavn(snake_body)
    def _spavn(self, snake_body):
        while True:
            dx = random.randint(0, self.width - 1)
            dy = random.randint(0, self.height -1)
            if (dx,dy) not in snake_body:
                return (dx,dy)
