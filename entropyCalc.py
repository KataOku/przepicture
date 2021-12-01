from PIL import ImageFilter
import numpy
from skimage.filters.rank.generic import entropy
from skimage import filters, morphology, util


def imageEntropy(image):
    """Calculates entropy values of points in image."""
    grayscale=util.img_as_ubyte(image.convert('L'))
    return filters.rank.entropy(grayscale, morphology.disk(1))


def maxEntropyPoint(entropyValues):
    """Finds index of point with maximum entropy value."""
    flatIndex=numpy.argmax(entropyValues)
    pointIndex=numpy.unravel_index(flatIndex, (len(entropyValues[0]), len(entropyValues)),order="F")
    entropyValues[pointIndex[1]][pointIndex[0]]=0
    return pointIndex


def lowerEntropy(entropyValues, pointIndex, discourageDistance):
    """Lowers entropy around specified point (to avoid points clustrering)."""
    for y in range(max(0,pointIndex[1]-discourageDistance), min(len(entropyValues)-1,pointIndex[1]+discourageDistance)):
        for x in range(max(0,pointIndex[0]-discourageDistance), min(len(entropyValues[y])-1,pointIndex[0]+discourageDistance)):              
            if numpy.sqrt((x-pointIndex[0])**2 + (y-pointIndex[1])**2) <= discourageDistance:
                entropyValues[y][x]=entropyValues[y][x]*numpy.sqrt((x-pointIndex[0])**2 + (y-pointIndex[1])**2)/discourageDistance*0.2
    return entropyValues


def edgePoints(image, distance):
    """Finds points on the boundary of image, separated by pointDstance from each other."""
    x=y=0
    entropyEdgePoints=[]
    while x<=image.size[0]:
        entropyEdgePoints.append((x,0))
        entropyEdgePoints.append((x,image.size[1]))
        x+=distance
    while y<=image.size[1]:
        entropyEdgePoints.append((0,y))
        entropyEdgePoints.append((image.size[0],y)) 
        y+=distance
    entropyEdgePoints.append((image.size))
    return entropyEdgePoints


def interestPointsCalc(pic, discourageDistance, pointsNumber):
    """Finds distinctive points of image for triangles corners."""
    blurred=pic.filter(ImageFilter.GaussianBlur(2))
    entropyValues=imageEntropy(blurred)
    interestPoints=edgePoints(pic, discourageDistance*2)
    for i in range(0,pointsNumber):
        pointIndex=maxEntropyPoint(entropyValues)
        interestPoints.append(pointIndex)
        entropyValues=lowerEntropy(entropyValues,pointIndex,discourageDistance)
    return interestPoints