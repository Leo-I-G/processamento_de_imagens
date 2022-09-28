from skimage.io import imread, imsave

def read_image(path, isgray=False):
    image = imread(path, asgray = isgray)
    return image

def save_image(image, path):
    imsave(path,image)