from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy
import pictureTools
from math import floor


class Picture():
    def __init__(self, initial_path):
        self.path=initial_path
        self.image=Image.open(initial_path)


    def _splitAreas(self, hCount, vCount=None):
        if vCount==None:
            vCount=hCount
        distanceX, distanceY = self.image.size[0]/hCount, self.image.size[1]/vCount
        pointsMap=[]
        for i in range(1,hCount+2):
            for j in range(1,vCount+2):
                x1,y1=floor(i*distanceX-distanceX),floor(j*distanceY-distanceY)
                x2,y2=floor(i*distanceX),floor(j*distanceY)
                dim=[(x1,y1), (x2,y1), (x2,y2), (x1,y2)]
                pointsMap.append(dim)
        return pointsMap


    def findSquares(self, hCount, vCount=None):
        squaresMap=self._splitAreas(hCount, vCount)
        return squaresMap[::2]

    def findTriangles(self,hCount, vCount=None):
        pointsMap=self._splitAreas(hCount, vCount)
        trianglesMap=[]
        for shape in pointsMap:
            newTriangle=[shape[0], shape[2], shape[3]]
            trianglesMap.append(newTriangle)
        return trianglesMap
        

    def patternMask(self, shapeChoice, hCount=5, vCount=None):
        if shapeChoice =="triangles":
            shapeMap=self.findTriangles(hCount, vCount)
        elif shapeChoice =="squares":
            shapeMap=self.findSquares(hCount, vCount)

        alpha = Image.new('L', self.image.size,0)
        draw = ImageDraw.Draw(alpha)
        for shape in shapeMap:
            draw.polygon(shape,fill=255)
        
        return alpha
                

    def joinWithMask(self,image,mask):
        numpyImage=numpy.array(image)
        numpyImageMask=numpy.dstack((numpyImage,numpy.array(mask)))
        self.image=pictureTools.joinImages(self, numpyImageMask)
    

    def blur(self, shapesType="squares", hCount=20, degree=10, vCount=None):
        blurred=self.image.filter(ImageFilter.GaussianBlur(degree))
        self.joinWithMask(blurred, self.patternMask(shapesType, hCount, vCount))
 

    def lighten(self, shapesType="squares", hCount=20, degree=1.2, vCount=None):
        brighten=ImageEnhance.Brightness(self.image)
        lightened=brighten.enhance(degree)
        self.joinWithMask(lightened, self.patternMask(shapesType, hCount, vCount))
   
    def saturation(self, shapesType="squares", hCount=20, degree=0.7, vCount=None):
        saturation = ImageEnhance.Color(self.image)
        saturated=saturation.enhance(degree)
        self.joinWithMask(saturated, self.patternMask(shapesType, hCount, vCount))



        