"""
import abstract class
"""
from models.camera import Camera


class FilmCamera(Camera):
    """
        The film camera class describes the film camera entity
    """

    def __init__(self, brand=None, model=None, lens=0, film_type=None, film_iso=0):
        """
            Constructor
        """
        super().__init__(brand, model, lens)
        self.film_type = film_type
        self.film_iso = film_iso

    def take_photo(self):
        """
            Method that returns info about photo
        """
        print("Photo with..." + self.film_type + self.film_iso)

    def __str__(self):
        """
        Method str which return line with camera object parameters
        """
        return f"\n brand: {self.brand}, model:{self.model},lens={self.lens},film type:{self.film_type}" \
               f",filmISO:{self.film_iso}"
