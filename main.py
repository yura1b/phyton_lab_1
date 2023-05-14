class Camera:

    cameras = []
    def __init__(self, model, resolution, zoom, memory_card_type, photo_count):
        self.__model = model
        self.__resolution = resolution
        self.__zoom = zoom
        self.__memory_card_type = memory_card_type
        self.__photo_count = photo_count

    @property
    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    @property
    def get_resolution(self):
        return self.__resolution

    def set_resolution(self, resolution):
        self.__resolution = resolution

    @property
    def get_zoom(self):
        return self.__zoom

    def set_zoom(self, zoom):
        self.__zoom = zoom

    @property
    def get_memory_card_type(self):
        return self.__memory_card_type

    def set_memory_card_type(self, memory_card_type):
        self.__memory_card_type = memory_card_type

    @property
    def get_photo_count(self):
        return self.__photo_count

    def set_photo_count(self, photo_count):
        self.__photo_count = photo_count

    def reset_zoom(self):
        self.__zoom = 1

    def erase_memory(self):
        self.__photo_count = 0

    def save_photo(self):
        self.__photo_count = (self.__photo_count + 1)

    def change_settings(self, resolution, zoom):
        self.__resolution = resolution
        self.__zoom = zoom

    def get_instance(self):
        default_camera = Camera()
        return default_camera

    def __str__(self):
        return f"\n model:{self.__model} resolution = {self.__resolution} zoom = {self.__zoom}" \
               f" memory card type = {self.__memory_card_type} photo count = {self.__photo_count}"


test_camera_1 = Camera("Sony jx-76", 0.2, 1.5, "64 gb", "46")
test_camera_2 = Camera("Canon fg-22", 0.4, 2.25, "128 gb", "31")
Camera.cameras.append(test_camera_1)
Camera.cameras.append(test_camera_2)

for cameras in Camera.cameras:
    print(cameras)
