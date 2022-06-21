import Augmentor

# This is to balance up the number of images in each country

# added 7000 images to Czech
c = Augmentor.Pipeline("dataset/train/Czech/images")
c.flip_left_right(probability=0.4)
c.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
c.sample(7000)

# added 7000 images to India
i = Augmentor.Pipeline("dataset/train/India/images")
i.flip_left_right(probability=0.4)
i.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
i.sample(2000)
