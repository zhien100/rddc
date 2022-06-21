from PIL import Image

# Show example of images in dataset

def show_image():
    for i in range(5):
        image = Image.open('dataset/train/Japan/images/Japan_00000'+str(i)+'.jpg')
        image.show()

show_image()