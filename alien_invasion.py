import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise the game and create game resources"""
        pygame.init()

        # Create a clock instance for controlling the frame rate
        self.clock = pygame.time.Clock()
        # Create a screen instance
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # Get the screen width and height
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        # Create an instance of Settings class
        self.settings = Settings(self)
        # Load the background image
        self.bg_image = pygame.image.load("images/background_resized.jpg").convert()
        # Load the ship image
        self.ship = Ship(self)
        # Set the window caption
        pygame.display.set_caption("Alien Invasion")
        # Create a group to store the bullets
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # call helper method for keywords and mouse events.
            self._check_events()
            # Update the ship's position based on the movement flags
            self.ship.update()
            # Update bullets position
            self._update_bullets()
            # Redraw the screen during each pass through the
            self._update_screen()
            #Limit the loop to 60 frames per second
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses to exit the game."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.bg_image, (0,0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()

