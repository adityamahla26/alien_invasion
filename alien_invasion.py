import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        # Create a group to store the aliens
        self.aliens = pygame.sprite.Group()
        # Create the fleet of aliens
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # call helper method for keywords and mouse events.
            self._check_events()
            # Update the ship's position based on the movement flags
            self.ship.update()
            # Update bullets position
            self._update_bullets()
            # Update the aliens position
            self._update_aliens()
            # Redraw the screen during each pass through the loop
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
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # Check for any bullets that have hit aliens
        # If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        current_x = alien_width
        current_y = alien_height

        while(current_y <self.screen_height-alien_height*6):
            while(current_x < self.screen_width - alien_width*2):
                self._create_alien(current_x,current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 2*alien_height


    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in a row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()

