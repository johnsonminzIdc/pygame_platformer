import pygame
import settings

class Character:
    def __init__(self, x, y, width, height, color):
        # 1. The Physics Box
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        
        # 2. Movement variables
        self.direction = pygame.Vector2(0, 0) # Store dx and dy here
        self.velocity_y = 0
        self.speed = 5
        
        # 3. State flags
        self.on_ground = False
        self.is_attacking = False

    def apply_gravity(self):
        # Hint: Add a small gravity constant to velocity_y
        # and then add velocity_y to the rect.y
        pass

    def move(self, dx):
        # Hint: Set the horizontal part of direction based on input
        pass

    def jump(self):
        # Hint: Only allow if self.on_ground is True
        # Set velocity_y to a negative value (jumping up)
        pass

    def check_collisions(self, tiles):
        # This is the tricky part!
        # Step A: Move X -> Check Tiles -> If hit, snap to side
        # Step B: Move Y -> Check Tiles -> If hit, snap to top/bottom
        pass

    def update(self, tiles):
        # This is the 'Brain' that runs every frame
        self.apply_gravity()
        # Call move logic
        # Call collision logic
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)