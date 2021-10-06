from PIL import Image
import numpy
import picture

def toRGBAImage(image):
    if type(image) is numpy.ndarray:
        image=Image.fromarray(image)
    if type(image) == picture.Picture:
        image=image.image
    if image.mode=="RGB":
        image.putalpha(255)
    return image
    

def joinImages(image1, image2):
    image1=toRGBAImage(image1)
    image1.alpha_composite(toRGBAImage(image2))
    return image1.convert("RGB")