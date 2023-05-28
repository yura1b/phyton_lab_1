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

    def get_lens(self) -> int:
        return self.lens

    def get_brand(self) -> str:
        return self.brand

    @abstractmethod
    def take_photo(self):
        pass


class CinematicCamera(Camera):
    """
        Constructor
    """

    def __init__(self, lens_type=None):
        """
            Constructor
        """
        super().__init__()
        self.lens_type = lens_type

    def take_photo(self) -> None:
        print("photo with..." + self.lens_type)

    def __str__(self):
        """
        Method str which return line with camera object parameters
        """
        return f"\n brand:{self.brand}, model:{self.model}, lens={self.lens}, lens type:{self.lens_type}"




class DigitalCamera(Camera):
    """

    """

    def __init__(self, resolution=None, zoom=0.0, memory_card_type=None, photo_count=0):
        super().__init__()
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photo_count = photo_count

    def take_photo(self):
        print("Photo with..." + self.resolution + self.zoom)

    def reset_zoom(self):
        """
        Function that sets the zoom parameter to the default value
        """
        self.zoom = 1

    def erase_memory(self):
        """
        Function that changes the value photo count to 0
        """
        self.photo_count = 0

    def save_photo(self):
        """
        Function that changes the number of photos by +1
        """
        self.photo_count = (self.photo_count + 1)

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
        return f"\n brand:{self.brand}, model:{self.model},lens={self.lens} resolution = {self.resolution} zoom = {self.zoom}" \
               f" memory card type = {self.memory_card_type} photo count = {self.photo_count}"


class FilmCamera(Camera):
    """

    """

    def __init__(self, film_type=None, film_iso=0):
        super().__init__()
        self.film_type = film_type
        self.film_iso = film_iso

    def take_photo(self):
        print("Photo with..." + self.film_type + self.film_iso)

    def __str__(self):
        """
        Method str which return line with camera object parameters
        """
        return f"\n brand: {self.brand}, model:{self.model},lens={self.lens},film type:{self.film_type}" \
               f",filmISO:{self.film_iso}"


class NightCamera(Camera):
    """

    """

    def __init__(self, has_zoom=None):
        super().__init__()
        self.has_zoom = has_zoom

    def take_photo(self):
        print("Photo with..." + self.has_zoom)

    def __str__(self):
        """
        Method str which return line with camera object parameters
        """
        return f"\n brand:{self.brand}, model:{self.model}, lens={self.lens}, has zoom:{self.has_zoom}"


class CameraManager:
    """

    """

    def add_camera(self):
        """

        """
        return Camera()

    def find_camera_with_brand_sony(self, cameras):
        """

        """
        return list(filter(lambda camera: camera.brand == 'sony', cameras))

    def find_camera_with_lens_more_than_(self, find_lens, cameras):
        """

        """
        return list(filter(lambda camera: camera.lens > find_lens, cameras))


cameras = []
CameraManager = CameraManager()
cameras.append(FilmCamera("Flix" ))
cameras.append(NightCamera("Canon"))
cameras.append(CinematicCamera("Fuji"))
cameras.append(DigitalCamera("Sony", 23))
for camera in cameras:
    print(camera)

