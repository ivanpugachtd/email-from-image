from PIL import Image
from typing import List, Type, Union
import os


class ImageHandler:
    def __init__(self, image_path: str) -> None:
        self.path: str = image_path
        
    def load_image(self) -> Type[Image.Image]:
        if not os.path.exists(self.path):
            raise Exception("Image path does not exist")
        return Image.open(self.path)