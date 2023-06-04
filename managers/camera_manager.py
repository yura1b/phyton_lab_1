from models.camera import Camera


class CameraManager:
    """
       The camera manager class describes the camera manager entity
    """

    def __init__(self):
        """
            Constructor
        """
        self.cameras = []

    def add_camera(self, camera: Camera):
        """
           Method that add new camera with empty value
        """
        self.cameras.append(camera)

    def find_camera_with_brand_sony(self):
        """
           Method which find camera with brand "sony"
        """
        return list(filter(lambda camera: camera.brand == 'sony', self.cameras))

    def find_camera_with_lens_more_than_(self, find_lens):
        """
           Method which find camera with lens more than value
        """
        var = [camera for camera in self.cameras if camera.lens > find_lens]
        return var

    def __len__(self):
        return len(self.cameras)

    def __getitem__(self, camera_index: int):
        return self.cameras[camera_index]

    def __iter__(self):
        return iter(self.cameras)

    def completed_list(self) -> [int]:
        """

        :return: list comprehension
        """
        return [camera.take_photo() for camera in self.cameras]

    def enumerate(self):
        """

        :return: number object and object
        """
        return [f'{index}:{value}' for index, value in enumerate(self.cameras)]

    def zipp(self):
        """
        :return: zipped line which contains object and number
        """
        return list(zip(self.take_photo(), self.cameras))

    def check_condition(self, condition):
        """
        :param condition:
        :return: is condition is right or false
        """
        all_condition = all(condition(camera) for camera in self.cameras)
        any_condition = any(condition(camera) for camera in self.cameras)
        return {"All cameras": all_condition, "Any camera": any_condition}
