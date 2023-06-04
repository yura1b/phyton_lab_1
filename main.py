from models.digital_camera import DigitalCamera
from models.cinematic_camera import CinematicCamera
from models.film_camera import FilmCamera
from models.night_camera import NightCamera
from managers.camera_manager import CameraManager


if __name__ == '__main__':

    Manager = CameraManager()
    cameras = [(DigitalCamera("Sony", "fj-45", 3, 4.5, 3.0, "64-gb", 23)),
               (FilmCamera("Fuji", "dd-34", 2, "all-stage", 3)),
               (FilmCamera("Fuji", "dd-34", 2, "all-stage", 3)), (CinematicCamera("Samsung", "we-23", 3, "all format"))]
    Manager.add_camera(cameras)
    for Manager in cameras:
        print(Manager)


