"""
import abstract class
"""
from models.camera import Camera


class NightCamera(Camera):
    """
       The night camera class describes the night camera entity
    """

    def __init__(self, brand=None, model=None, lens=0, has_zoom=None):
        """
            Constructor
        """
        super().__init__(brand, model, lens)
        self.has_zoom = has_zoom

    def take_photo(self):
        """
            Method that returns info about photo
        """
        print("Photo with..." + self.has_zoom)

    def __str__(self):
        """
        Method str which return line with camera object parameters
        """
        return f"\n brand:{self.brand}, model:{self.model}, lens={self.lens}, has zoom:{self.has_zoom}"
