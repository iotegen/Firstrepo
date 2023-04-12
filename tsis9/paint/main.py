import pygame, math

pygame.init()
WIDTH, HEIGHT = 900, 760
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
COLOR = BLACK

tool_screen = pygame.Surface((900, 40))
objects = []

class GameObject:
    def draw(self):
        raise NotImplementedError

    def handle(self, mouse_pos):
        raise NotImplementedError


class Button:
    def __init__(self,x, y, path):
        self.x = x
        self.y = y
        #self.rect = pygame.Rect((self.x, self.y, 20, 20))
        self.image = pygame.transform.scale((pygame.image.load(path)), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
        

    def draw(self):
        pygame.draw.rect(surface=tool_screen, color = BLACK, rect=self.rect, width=1)
        tool_screen.blit(self.image, self.rect)
        

class Pen(GameObject):
    def __init__(self, *args, **kwargs):
        self.points = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for idx, value in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                COLOR,
                start_pos=value,  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=3
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)
   

class Rectangle(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos  # (x1, y1)
        self.end_pos = start_pos  # (x2, y2)

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            SCREEN,
            COLOR,
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=2,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Circle(GameObject):
    def __init__(self, start_pos):
        self.center = start_pos #x, y
        self.radius = 0 # r
    def draw(self):
        pygame.draw.circle(surface=SCREEN,
                           color=COLOR,
                           center=self.center,
                           radius=self.radius,
                           width=2)
    def handle(self, mouse_pos):
        a = self.center[0] - mouse_pos[0]
        b = self.center[1] - mouse_pos[1]
        self.radius = math.sqrt(a*a + b*b)
    
class Triangle(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.polygon(
            SCREEN,
            BLACK,
            (
                (start_pos_x, start_pos_y),
                (start_pos_x, end_pos_y),
                (end_pos_x, end_pos_y),
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class equilateralTriangle(GameObject): # triangle triangle triangle
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        rad = end_pos_x - start_pos_x
        pygame.draw.polygon(
            SCREEN, BLACK,
            (
                (start_pos_x, start_pos_y),
                (start_pos_x - rad // (3 ** .5 * 2), start_pos_y + rad // 2),
                (start_pos_x + rad // (3 ** .5 * 2), start_pos_y + rad // 2),
            ),
            width=5
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos
        
        
class Romb(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.polygon(
            SCREEN,
            BLACK,
            (
                (start_pos_x + (end_pos_x - start_pos_x) // 2, start_pos_y),
                (start_pos_x, start_pos_y + (end_pos_y - start_pos_y) // 2),
                (start_pos_x + (end_pos_x - start_pos_x) // 2, end_pos_y),
                (end_pos_x, start_pos_y + (end_pos_y - start_pos_y) // 2),
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos




    
def main():
    running = True
    clock = pygame.time.Clock()
    active_obj = None
    pen_button = Button(20, 20, "images/pen.png")
    rect_button = Button(70, 20, "images/rect.png")
    circle_button = Button(120, 20, "images/circle.png")
    eraser_button = Button(400, 20, "images/eraser.png")
    triangle_button = Button(170, 20, "images/triangle.png")
    equilateralTriangle_button = Button(220, 20, "images/triangle2.png")
    romb_button = Button(270, 20, "images/romb.png")

    tools = [
        pen_button,
        rect_button,
        circle_button,
        eraser_button,
        triangle_button,
        equilateralTriangle_button,
        romb_button
        
    ]
    
    # current_shape = 'pen'
    current_shape = Pen
   
    while running:
        SCREEN.fill((WHITE))
        tool_screen.fill((200, 200, 200))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    global COLOR
                    COLOR = (0,0,255)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_button.rect.collidepoint(event.pos):
                    current_shape = Rectangle
                if pen_button.rect.collidepoint(event.pos):
                    current_shape = Pen
                if circle_button.rect.collidepoint(event.pos):
                    current_shape = Circle
                if triangle_button.rect.collidepoint(event.pos):
                    current_shape = Triangle 
                if equilateralTriangle_button.rect.collidepoint(event.pos):
                    current_shape = equilateralTriangle   
                if romb_button.rect.collidepoint(event.pos):
                    current_shape = Romb
                if eraser_button.rect.collidepoint(event.pos):
                    if objects:
                        objects.pop()
                else:
                    active_obj = current_shape(start_pos=event.pos)

            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.handle(pygame.mouse.get_pos())
                active_obj.draw()

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None

        for obj in objects:
            obj.draw()
        
        for tool in tools:
            tool.draw()
       
        SCREEN.blit(tool_screen, (0, 0))
        

        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()