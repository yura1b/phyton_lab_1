"""
    imports
"""
from managers.camera_manager import CameraManager
from models.film_camera import FilmCamera
from models.night_camera import NightCamera
from models.digital_camera import DigitalCamera
from models.cinematic_camera import CinematicCamera


class SetManager:
    """
       class set_manager work with sets
    """

    def __init__(self, camera_manager_):
        self.camera_manager = camera_manager_

    def __iter__(self):
        for camera in self.camera_manager:
            for material in camera.material_set:
                yield material

    def __len__(self):
        count = 0
        for camera in self.camera_manager:
            count += len(camera.material_set)
        return count

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("Index not found")
        for camera in self.camera_manager:
            if index < len(camera.material_set):
                return list(camera.material_set)[index]
            index -= len(camera.material_set)

    def __next__(self):
        for camera in self.camera_manager:
            for material_ in camera.material_set:
                yield material_
