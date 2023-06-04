"""
   imports
"""
from abc import ABC, abstractmethod


class Camera(ABC):
    """
        The camera class describes the camera entity
    """

    def __init__(self, brand=None, model=None, lens=0):

        """
            Constructor
        """
        self.brand = brand
        self.model = model
        self.lens = lens
        self.material_set = set()

    def __iter__(self):
        """
        iter
        """
        pass

    def get_attributes_of_class(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    @abstractmethod
    def camera_material(self):
        """
            Method camera_material which return camera materials
        """

    @property
    def get_brand(self):
        return self.brand

    @property
    def get_model(self):
        return self.model

    @property
    def get_lens(self):
        return self.lens

    def get_lens_(self) -> int:
        """
        Method that returns the value of the parameter lens
        """
        return self.lens

    def get_brand_(self) -> str:
        """
        Method that returns the value of the parameter brand
        """
        return self.brand

    @abstractmethod
    def take_photo(self):
        """
        Method which return info about photo
        """
