class Snake():
    ALLOWD_DIRECTIONS = ('UP','DOWN','LEFT','RIGHT')
    OPPOSITE = {'UP':'DOWN','DOWN':'UP','LEFT':'RIGHT','RIGHT':'LEFT'}

    def __init__(self, user_id, width, height):
        self.user_id = user_id
        cx = width//2
        cy = height//2
        self.body = [(cx, cy), (cx-1, cy), (cx-2, cy)]
        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'
        self.alive = True
        self.score = 0
        self.grow_pending = 0
    def __str__(self):
        return f'Змеюга по имени {self.user_id} успешно создана c телом {self.body}'

    def set_direction(self, new_direction):
        if new_direction not in self.ALLOWD_DIRECTIONS:
            return
        if new_direction == self.OPPOSITE[self.next_direction]:
            return
        self.next_direction = new_direction

    def move(self):
        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        if self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)

        self.body.insert(0,new_head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def check_wall_collision(self,width,height):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= width:
            self.alive = False
        if head_y < 0 or head_y >= height:
            self.alive = False

    def check_self_collision(self):
        if self.body[0] in self.body[1:]:
            self.alive = False

    def grow(self, amount = 1):
        self.grow_pending += amount



