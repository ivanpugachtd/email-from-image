from PIL import Image
from typing import Type
import os


class ImageHandler:
    def __init__(self, image_path: str) -> None:
        self.path: str = image_path
    
    @property
    def path(self) -> str:
        return self._path
    
    @path.setter
    def path(self, value: str) -> None:
        if not os.path.exists(value):
            raise Exception("Image path does not exist")
        self._path = value 
    
    def load_image(self) -> Type[Image.Image]:
        return Image.open(self._path)