import os
from PIL import Image

source_dir = os.path.expanduser('~/Pictures/br/downloaded_images')

# List all webp files in the source directory
images = [f for f in os.listdir(source_dir) if f.lower().endswith('.webp')]

# Convert each webp file to jpg in place
for image in images:
    source_path = os.path.join(source_dir, image)
    if os.path.isfile(source_path):
        img = Image.open(source_path)
        img.convert("RGB").save(os.path.splitext(source_path)[0] + '.jpg', "JPEG")
