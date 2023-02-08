import random
import pygame

pygame.init()

WIN_HEIGHT = 500
WIN_WIDTH = 500
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Snake:
    def __init__(self, head: tuple[int] = (0,0)) -> None:
        self.head = head
        self.body: list[tuple[int]] = [head]
        self.length = 1
    
    def add_pos(self, pos: tuple[int]) -> None:
        self.body.append(pos)
        self.head = pos

    def rem_pos(self) -> tuple[int]:
        return self.body.pop(0)


class Board:
    def __init__(self, surface: pygame.Surface, num: int = 50) -> None:
        self.rect_dict = {}
        self.surface = surface
        self.rect_size = 10
        self.num = num
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.snake: Snake = None
        self.free_squares: list[tuple[int]] = None
        self.food: tuple[int] = None
        self.last_direction = 'r'

    def initialise_game(self) -> None:
        self.draw()
        self.draw_snake()

    def draw(self) -> None:
        for i in range(self.num):
            for j in range(self.num):
                new_rect = self.draw_rect(BLUE, j*self.rect_size, i*self.rect_size)
                self.rect_dict[i, j] = new_rect
        self.free_squares = list(self.rect_dict.keys())
        pygame.draw.rect(self.surface, (25, 25, 25), (20, self.num*self.rect_size + 10, 150, 40))
    
    def draw_snake(self, pos: tuple[int] = (0, 0)) -> None:
        self.draw_rect(WHITE, pos[0], pos[1])
        self.snake = Snake(pos)
        self.free_squares.remove(pos)

    def draw_rect(self, color: tuple[int], x: int, y: int) -> pygame.Rect:
        return pygame.draw.rect(self.surface, color, (x, y, self.rect_size, self.rect_size))

    def generate_food(self) -> None:
        key = random.choice(self.free_squares)
        random_square = self.rect_dict[key]
        self.draw_rect(GREEN, random_square.x, random_square.y)
        self.free_squares.remove(key)
        self.food = key
    
    def eat(self) -> None:
        if self.snake.head == self.food:
            self.snake.add_pos(self.food)
            x, y = self.rect_dict[self.food].x, self.rect_dict[self.food].y
            self.draw_rect(WHITE, x, y)
            self.generate_food()
            return True
    
    def move(self, pos: tuple[int]) -> bool:
        if pos in self.snake.body:
            return
        x, y = pos
        if (x < 0 or x > self.num-1) or (y < 0 or y > self.num-1):
            return
        self.snake.add_pos(pos)
        x, y = self.rect_dict[pos].x, self.rect_dict[pos].y
        self.draw_rect(WHITE, x, y)
        freed_square = self.snake.rem_pos()
        self.draw_rect(BLUE, self.rect_dict[freed_square].x, self.rect_dict[freed_square].y)
        self.free_squares.append(freed_square)
        return True

board = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT + 100))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake Game')

def main() -> None:
    run = True
    game = Board(board)
    game.initialise_game()
    game.generate_food()
    while run:
        clock.tick(10)
        if game.last_direction == 'u':
            if not game.move((game.snake.head[0]-1, game.snake.head[1])):
                run = False
        elif game.last_direction == 'd':
            if not game.move((game.snake.head[0]+1, game.snake.head[1])):
                run = False
        elif game.last_direction == 'r':
            if not game.move((game.snake.head[0], game.snake.head[1]+1)):
                run = False
        elif game.last_direction == 'l':
            if not game.move((game.snake.head[0], game.snake.head[1]-1)):
                run = False
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
            
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    if game.last_direction == 'd':
                        continue
                    game.last_direction = 'u'
                if ev.key == pygame.K_DOWN:
                    if game.last_direction == 'u':
                        continue
                    game.last_direction = 'd'
                if ev.key == pygame.K_RIGHT:
                    if game.last_direction == 'l':
                        continue
                    game.last_direction = 'r'                
                if ev.key == pygame.K_LEFT:
                    if game.last_direction == 'r':
                        continue
                    game.last_direction = 'l'

        game.eat()
        
        pygame.display.flip()

if __name__ == "__main__":
    main()