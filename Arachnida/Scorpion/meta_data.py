#import subprocess
from PIL import Image
from PIL.ExifTags import TAGS
import argparse

'''

'''


def get_exif_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data is not None:
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            print(f"{tag_name}: {value}")