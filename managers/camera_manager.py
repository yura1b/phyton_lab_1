


class CameraManager:
    """
       The camera manager class describes the camera manager entity
    """

    def __init__(self):
        self.cameras = []

    def add_camera(self, camera):
        """
           Method that add new camera with empty value
        """
        self.cameras.append(camera)

    def find_camera_with_brand_sony(self, brand):
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

    def __getitem__(self, index):
        return self.cameras[index]

    def __iter__(self):
        return iter(self.cameras)

    def completed_list(self):
        return [camera.take_photo()for camera in self.cameras]

    def enumerate(self):
        return [f'{index}:{value}'for index, value in enumerate(self.cameras)]

    def zipp(self):
        result = [camera.take_photo()for camera in self.cameras]
        return [f"{result}  {camera}" for result, camera in zip(result, self.cameras)]

    def check_condition(self, condition):
        all_condition = all(condition(camera) for camera in self.cameras)
        any_condition = any(condition(camera) for camera in self.cameras)
        return {"All cameras": all_condition, "Any camera": any_condition}
