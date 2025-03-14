from PIL import Image

class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Background image settings
        image = Image.open('images/background.jpg')
        resized_image = image.resize((self.screen_width, self.screen_height), Image.LANCZOS)
        resized_image.save('images/background_resized.jpg')

        # Ship image settings
        image_ship = Image.open('images/ship.png')
        resized_image_ship = image_ship.resize((110, 220), Image.LANCZOS)
        resized_image_ship.save('images/ship_resized.png')