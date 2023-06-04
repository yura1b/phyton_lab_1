"""
import abstract class
"""
from models.camera import Camera


class DigitalCamera(Camera):
    """
        The digital camera class describes the digital camera entity
    """
    def __init__(self, brand=None, model=None, lens=0, resolution=None, zoom=0, memory_card_type=None, photo_count=0):
        """
            Constructor
        """
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photo_count = photo_count
        self.material_set = set()

    def take_photo(self):
        """
            Method that returns info about photo
        """
        print("Photo with..." + self.resolution + str(self.zoom))

    def reset_zoom(self, zoom_par=0.0):
        """
        Function that sets the zoom parameter to the default value
        """
        self.zoom = zoom_par

    def chose_memory(self, number):
        """
        Function that changes the value photo count to 0
        """
        try:
            self.photo_count = self.photo_count/number
        except ZeroDivisionError:
            print("false value")

    def save_photo(self):
        """
        Function that changes the number of photos by +1
        """
        if self.photo_count < 500:
            self.photo_count = (self.photo_count+1)

    def change_settings(self, resolution, zoom):
        """
        A function that changes the values resolution, zoom to those passed to it
        """
        self.resolution = resolution
        self.zoom = zoom

    def __str__(self):
        """
        Method str which return line with camera object parameters
        """
        return f"\n brand:{self.brand}, model:{self.model},lens={self.lens} resolution = {self.resolution}" \
               f" zoom = {self.zoom} memory card type = {self.memory_card_type} photo count = {self.photo_count}"

    def camera_material(self):
        """
            Method camera_material which return camera materials
        """
        return self.material_set
