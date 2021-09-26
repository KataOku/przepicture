from PIL import Image, ImageFilter, ImageEnhance
from math import floor

class Picture():
    def __init__(self, initial_path):
        self.path=initial_path
        self.image=Image.open(initial_path)


    def findSquares(self, squareNumber):
        distanceX, distanceY = self.image.size[0]/squareNumber, self.image.size[1]/squareNumber
        pixelList=[]
        for i in range(1,squareNumber+2):
            for j in range(1,squareNumber+2):
                dim=(floor(i*distanceX-distanceX),floor(j*distanceY-distanceY),floor(i*distanceX),floor(j*distanceY))
                pixelList.append(dim)
        return pixelList


    def blur(self, squareNumber=20, degree=10):
        pixelList=self.findSquares(squareNumber)
        for i in range(0,len(pixelList)):
            if i%2==0:
                square=self.image.crop(pixelList[i])
                square=square.filter(ImageFilter.GaussianBlur(degree))
                self.image.paste(square,(pixelList[i][0], pixelList[i][1]))
        

    def lighten(self, squareNumber=20, degree=1.2):
        pixelList=self.findSquares(squareNumber)
        for i in range(0,len(pixelList)):
            if i%2==0:
                square=self.image.crop(pixelList[i])
                brighten=ImageEnhance.Brightness(square)
                square=brighten.enhance(degree) #0.0-1.0 darker  , lighter >1
                self.image.paste(square,(pixelList[i][0], pixelList[i][1]))
   

    def saturation(self, squareNumber=20, degree=0.7):
        pixelList=self.findSquares(squareNumber)
        for i in range(0,len(pixelList)):
            if i%2==0:
                square=self.image.crop(pixelList[i])
                saturation = ImageEnhance.Color(square)
                square = saturation.enhance(degree) #0.0-1.0
                self.image.paste(square,(pixelList[i][0], pixelList[i][1]))

       



