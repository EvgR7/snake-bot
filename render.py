def render(game):
    width = game.width
    height = game.height

    field = [["⬜" for _ in range(width)]
        for _ in range(height)]

    fx, fy = game.food.position
    field[fy][fx] = "🍎"

    for i, (x, y) in enumerate(game.snake.body):
        field[y][x] = "🟩" if i == 0 else "🟢"

    lines = []
    lines.append(f'Рекорд: {game.score}')
    lines.append('⬛'* (width + 2))
    for row in field:
        lines.append('⬛' + ''.join(row) + '⬛')
    lines.append('⬛' * (width + 2))
    return '\n'.join(lines)