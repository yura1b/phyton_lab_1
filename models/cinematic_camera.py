"""
import abstract class
"""
from models.camera import Camera


class CinematicCamera(Camera):
    """
        The cinematic camera class describes the cinematic camera entity
    """

    def __init__(self, brand=None, model=None, lens=0, lens_type=None):
        """
            Constructor
        """
        super().__init__(brand, model, lens)
        self.lens_type = lens_type
        self.material_set = set()

    def take_photo(self) -> None:
        """
        Method that returns info about photo
        """
        print("photo with..." + self.lens_type)

    def __str__(self):
        """
        Method str which return line with camera object parameters
        """
        return f"\n brand:{self.brand}, model:{self.model}, " \
               f"lens={self.lens}, lens type:{self.lens_type}"

    def camera_material(self):
        """
            Method camera_material which return camera materials
        """
        return self.material_set
