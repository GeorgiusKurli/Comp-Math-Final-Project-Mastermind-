from pygame import *
from pygame.sprite import *

# Color used
white = (255, 255, 255)
black = (0, 0, 0)
grey = (100, 100, 100)


# Class to make buttons
class Button(Sprite):
    def __init__(self, message, x, y, fontsize=42, font="arial", color=(0, 0, 0), backcolor=None, align="center"):
        Sprite.__init__(self)
        self.color = color
        self.backcolor = backcolor
        self.x = x
        self.y = y
        self.message = message
        self.font = pygame.font.SysFont(font, fontsize)
        self.image = self.font.render(message, 1, color, backcolor)
        self.rect = self.image.get_rect()
        self.align = align.lower()
        if self.align == "center":
            self.rect.center = (x, y)

        elif self.align == "left":
            self.rect.left = x
            self.rect.top = y

        elif self.align == "right":
            self.rect.right = x
            self.rect.top = y

    # used to update
    def update_message(self, message):
        self.image = self.font.render(message, 1, self.color, self.backcolor)
        self.message = message
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    # used to change colour
    def change_colour(self, color):
        self.color = color
        self.image = self.font.render(self.message, 1, self.color, self.backcolor)

    # used to change backcolor
    def change_backcolour(self, color):
        self.backcolor = color
        self.image = self.font.render(self.message, 1, self.color, self.backcolor)


# Class to make balls
class Ball(Sprite):
    def __init__(self, x, y, color = (0,0,0), size = 40):
        Sprite.__init__(self)
        self.color = color
        self.x = x
        self.y = y
        self.surface_size = size
        self.circle_size = round(size/2)

        # used to create the surface
        self.image = Surface((self.surface_size, self.surface_size), SRCALPHA)

        draw.circle(self.image, self.color, (self.circle_size,self.circle_size), self.circle_size)
        self.rect = self.image.get_rect(center=(x, y))

    # used to change the colour
    def change_colour(self, color):
        self.color = color
        draw.circle(self.image, self.color, (self.circle_size,self.circle_size), self.circle_size)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # create a larger white circle to show a 'glowing effect'
    def glow(self):
        self.image = Surface((self.surface_size + 10, self.surface_size + 10), SRCALPHA)
        draw.circle(self.image, (255,255,255), (self.circle_size + 5,self.circle_size + 5), self.circle_size + 5)
        draw.circle(self.image, self.color, (self.circle_size + 5,self.circle_size + 5), self.circle_size)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # removes the larger white circle
    def deglow(self):
        self.image = Surface((self.surface_size,self.surface_size), SRCALPHA)
        draw.circle(self.image, self.color, (self.circle_size,self.circle_size), self.circle_size)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # moves the ball
    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)

    # creates a copy of the ball
    def reproduce(self, size):
        return Ball(self.x, self.y, self.color , size)

    # getter for position
    def get_position(self):
        return [self.x, self.y]

    # getter for colour
    def get_colour(self):
        return self.color
