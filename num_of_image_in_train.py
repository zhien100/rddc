import os
from os import listdir

# Show number of images in each country (total 3 countries)

def image_num(folder_name, folder_dir):
    i = 0
    for images in os.listdir(folder_dir):
        if (images.endswith(".jpg")):
            i += 1
    print('Number of images in ' + folder_name + " = " + str(i))

# get the path/directory
czech_dir = "dataset/train/Czech/images"
india_dir = "dataset/train/India/images"
japan_dir = "dataset/train/Japan/images"

image_num("Czech",czech_dir)
image_num("India",india_dir)
image_num("Japan",japan_dir)