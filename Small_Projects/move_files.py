import os
import shutil

images = [f for f in os.listdir() if '.webp' in f.lower()]

os.mkdir('downloaded_images')

for image in images:
    new_path = 'downloaded_images/' + image
    shutil.move(image, new_path)
