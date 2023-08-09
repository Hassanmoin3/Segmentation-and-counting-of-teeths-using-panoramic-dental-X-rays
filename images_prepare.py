import os
import numpy as np
from PIL import Image
from zipfile import ZipFile
from natsort import natsorted


def convert_one_channel(img):
    # some images have 3 channels , although they are grayscale image
    if len(img.shape) > 2:
        img = img[:, :, 0]
        return img
    else:
        return img


def pre_images(resize_shape, path, include_zip):
    path = path+'/DentalPanoramicXrays/Images1/'
    dirs = natsorted(os.listdir(path))
    sizes = np.zeros([len(dirs), 2])
    images = []
    for i in range(len(dirs)):
        img = Image.open(path+dirs[i])
        sizes[i, :] = img.size
        img = img.resize((resize_shape), Image.ANTIALIAS)
        img = convert_one_channel(np.asarray(img))
        images.append(img)
    images = np.stack(images, axis=0)
    images = np.expand_dims(images, axis=-1)
    return images, sizes
