from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy
from math import floor
from skimage.filters.rank.generic import entropy
from scipy.spatial import Delaunay


import pictureTools, entropyCalc


class Picture():
    def __init__(self, initial_path):
        self.path=initial_path
        self.image=Image.open(initial_path)


    def _splitAreas(self, hCount, vCount=None):
        """Splits image into evenly shaped rectangles based on hCount and vCount."""
        distanceX, distanceY = self.image.size[0]/hCount, self.image.size[1]/vCount
        pointsMap=[]
        for i in range(1,hCount+1):
            for j in range(1,vCount+1):
                x1,y1=floor(i*distanceX-distanceX),floor(j*distanceY-distanceY)
                x2,y2=floor(i*distanceX),floor(j*distanceY)
                pointsMap.append([(x1,y1), (x2,y1), (x2,y2), (x1,y2)])
        return pointsMap


    def splitToRectangles(self, hCount, vCount):
        """Splits image to evenly sized rectangles based on hCount and vCount.
        Returns coordinates of every second one."""
        rectanglesMap=self._splitAreas(hCount, vCount)
        if vCount%2==1:
            return rectanglesMap[::2]
        else:
            helper1=helper2=[]
            while rectanglesMap!=[]:
                helper1+=rectanglesMap[0:vCount]
                helper2+=rectanglesMap[vCount:2*vCount]
                rectanglesMap=rectanglesMap[2*vCount:]
            helper2=helper2[1:]
            return helper1[::2]+helper2[::2]

    def splitToTriangles(self,hCount, vCount):
        """Splits image to evenly sized rectangles based on hCount and vCount,
        and thean split each of them into two triangles.
        Returns coordinates of lower right triangle."""
        pointsMap=self._splitAreas(hCount, vCount)
        trianglesMap=[]
        for shape in pointsMap:
            trianglesMap.append([shape[0], shape[2], shape[3]])
        return trianglesMap
        

    def shapeBasedMask(self, shape, hCount=5, vCount=None):
        """Returns alpha mask of hCount x vCount given shapes."""
        if vCount==None:
            vCount=hCount        
        if shape =="triangles":
            shapeMap=self.splitToTriangles(hCount, vCount)
        elif shape =="rectangles":
            shapeMap=self.splitToRectangles(hCount, vCount)

        alpha = Image.new('L', self.image.size,0)
        draw = ImageDraw.Draw(alpha)
        for shape in shapeMap:
            print(shape)
            draw.polygon(shape,fill=255)
        return alpha
                

    def pasteWithMask(self,pastedImage,mask):
        """Pastes pastedImage based on mask."""
        pastedWithMask=numpy.dstack((numpy.array(pastedImage),numpy.array(mask)))
        self.image=pictureTools.mergeImages(self, pastedWithMask)
    

    def blur(self, shape="rectangles", hCount=20, degree=10, vCount=None):
        """Blurres shape based parts of image by given degree."""
        blurred=self.image.filter(ImageFilter.GaussianBlur(degree))
        self.pasteWithMask(blurred, self.shapeBasedMask(shape, hCount, vCount))
 

    def lighten(self, shape="rectangles", hCount=20, degree=1.2, vCount=None):
        """Lightens (darkens) shape based parts of image by given degree."""
        lightened=ImageEnhance.Brightness(self.image).enhance(degree)
        self.pasteWithMask(lightened, self.shapeBasedMask(shape, hCount, vCount))
   

    def saturate(self, shape="rectangles", hCount=20, degree=0.7, vCount=None):
        """Saturates shape based parts of image by given degree."""
        saturated=ImageEnhance.Color(self.image).enhance(degree)
        self.pasteWithMask(saturated, self.shapeBasedMask(shape, hCount, vCount))


    def triangulate(self, pointsCount=20):
        """Creates triangulation effect based on pointsCount points of max entropy"""
        baseImg = self.image.resize((1000, int(self.image.size[1]*1000/self.image.size[0])))
        result=baseImg.copy()
        discourageDistance=floor(numpy.sqrt(baseImg.size[0]*baseImg.size[1] / pointsCount))
        interestPoints=entropyCalc.interestPointsCalc(baseImg, discourageDistance, pointsCount)

        for triangle in Delaunay(interestPoints).vertices:
            triangleCoords=[interestPoints[triangle[0]], interestPoints[triangle[1]], interestPoints[triangle[2]]]
            ImageDraw.Draw(result).polygon(
                triangleCoords, 
                fill=pictureTools.triangleColor(triangleCoords, baseImg))
        self.image=result
