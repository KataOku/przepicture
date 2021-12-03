from PIL import Image
import numpy
import math
from skimage.filters.rank.generic import entropy

import picture
from imageBasedColorThief import ImageBasedColorThief

def toRGBAImage(image):
    """Converts image to PIL.Image with alpha."""
    if type(image) is numpy.ndarray:
        image=Image.fromarray(image)
    if type(image) == picture.Picture:
        image=image.image
    if image.mode=="RGB":
        image.putalpha(255)
    return image
    

def mergeImages(image1, image2):
    """Merges two images into PIL.Image."""
    image1=toRGBAImage(image1)
    image1.alpha_composite(toRGBAImage(image2))
    return image1.convert("RGB")


def triangleColor(triangle, image):
    """Finds dominant color of triangle (using square of side length 2*r of incircle of triangle)."""

    # calculate triangle edges lengths
    a=math.sqrt((triangle[0][0]-triangle[1][0])**2+(triangle[0][1]-triangle[1][1])**2)
    b=math.sqrt((triangle[1][0]-triangle[2][0])**2+(triangle[1][1]-triangle[2][1])**2)
    c=math.sqrt((triangle[0][0]-triangle[2][0])**2+(triangle[0][1]-triangle[2][1])**2)

    # center and radius of circle inscribed in triangle
    barycenter=((triangle[0][0]+triangle[1][0]+triangle[2][0])/3,(triangle[0][1]+triangle[1][1]+triangle[2][1])/3 )
    d=(a+b+c)/2
    r=math.sqrt((d-a)*(d-b)*(d-c)/(d))

    # quarter of edge length of square inscribed in a cricle,
    # capped at 2, so the square always exists
    dist = max(2,r/(math.sqrt(2)*2))

    resizedImg=image.crop((
        math.floor(max(0,barycenter[0]-dist)),
        math.floor(max(0,barycenter[1]-dist)),
        math.floor(min(image.size[0],barycenter[0]+dist)),
        math.floor(min(image.size[1],barycenter[1]+dist))))

    return ImageBasedColorThief(resizedImg).get_color()
   


