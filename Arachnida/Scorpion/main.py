import argparse
from meta_data import get_exif_metadata


'''


'''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('images', nargs='+', help='The image files to display metadata for.')
    args = parser.parse_args()

    for image_path in args.images:
        print(f"EXIF Metadata for {image_path}:")
        get_exif_metadata(image_path)
        print()

if __name__ == "__main__":
    main()