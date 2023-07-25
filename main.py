from PIL import Image
from pathlib import Path

def convert_to_webp(source:Path):
    destination = source.with_suffix('.png')
    image = Image.open(source)
    image.save(destination, format='png')

    return destination

convert_to_webp(Path('./webp/image.jpg'))