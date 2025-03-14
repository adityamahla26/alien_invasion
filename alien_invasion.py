import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise the game and create game resources"""
        pygame.init()

        # Create an instance of Settings class
        self.settings = Settings()
        # Create a clock instance for controlling the frame rate
        self.clock = pygame.time.Clock()
        # Create a screen instance
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # Load the background image
        self.bg_image = pygame.image.load("images/background_resized.jpg").convert()
        # Load the ship image
        self.ship = Ship(self)
        # Set the window caption
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keywords and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.blit(self.bg_image, (0,0))
            self.ship.blitme()
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()

