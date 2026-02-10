from snake import Snake
from food import Food

class Game():

    def __init__(self, user_id, width, height):
        self.user_id = user_id
        self.width = width
        self.height = height
        self.score = 0
        self.snake = Snake(user_id, width, height)
        self.food = Food(width, height, self.snake.body)
        self.running = True
        self.task = None
        self.game_over = False

    def tick(self):
        if self.game_over:
            return

        self.snake.move()
        self.snake.check_wall_collision(self.width, self.width)
        self.snake.check_self_collision()
        #print(self.snake.alive)
        #print(self.game_over)
        if not self.snake.alive:
            self.game_over = True
            return

        #print(self.snake.body)
        if self.snake.body[0] == self.food.position:

            self.snake.grow()
            self.score += 1
            self.food = Food(self.width, self.height, self.snake.body)


    def set_directon(self, direction):
        if self.game_over:
            return
        self.snake.set_direction(direction)


