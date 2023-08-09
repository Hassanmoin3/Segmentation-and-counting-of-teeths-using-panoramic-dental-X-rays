import os
import sys
import numpy as np
from PIL import Image
from zipfile import ZipFile
from natsort import natsorted
script_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
default_path = script_dir+'/Original_Masks/'


def convert_one_channel(img):
    # some images have 3 channels , although they are grayscale image
    if len(img.shape) > 2:
        img = img[:, :, 0]
        return img
    else:
        return img


def pre_masks(resize_shape=(512, 512), path=default_path):
    ZipFile(path+"/Orig_Masks.zip").extractall(path+'/Masks/')
    path = path+'/Masks/Orig_Masks/'
    dirs = natsorted(os.listdir(path))
    masks = []
    for i in range(len(dirs)):
        img = Image.open(path+dirs[i])
        img = img.resize((resize_shape), Image.ANTIALIAS)
        img = convert_one_channel(np.asarray(img))
        masks.append(img)
    masks = np.stack(masks, axis=0)
    masks = np.expand_dims(masks, axis=-1)
    return masks

default_path = script_dir+'/Custom_Masks/'


def pre_splitted_masks(path=default_path):
    ZipFile(path+"/splitted_masks.zip").extractall(path+'/Masks/')
    path = path+'/Masks/'
    dirs = natsorted(os.listdir(path))
    masks = []
    for i in range(len(dirs)):
        img = Image.open(path+dirs[i])
        img = convert_one_channel(np.asarray(img))
        masks.append(img)
    masks = np.stack(masks, axis=0)
    masks = np.expand_dims(masks, axis=-1)
    return masks
