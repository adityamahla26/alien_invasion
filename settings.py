from PIL import Image

class Settings:
    def __init__(self,ai_game):
        # Screen settings
        self.screen_width = ai_game.screen_width
        self.screen_height = ai_game.screen_height

        # Background image settings
        image = Image.open('images/background.jpg')
        resized_image = image.resize((self.screen_width, self.screen_height), Image.LANCZOS)
        resized_image.save('images/background_resized.jpg')
        
        # Ship image settings
        image_ship = Image.open('images/ship.png')
        resized_image_ship = image_ship.resize((110, 220), Image.LANCZOS)
        resized_image_ship.save('images/ship_resized.png')

        # Ship settings
        self.ship_speed = 10.0

        #Bullet settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255,60,60)
        self.bullet_speed = 1.0
        self.bullets_allowed = 3

        # Alien image settings
        image_alien = Image.open('images/alien.png')
        resized_image_alien = image_alien.resize((80, 80), Image.LANCZOS)
        resized_image_alien.save('images/alien_resized.png')

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
