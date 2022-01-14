from colorthief import ColorThief, MMCQ

class ImageBasedColorThief(ColorThief):
    """ColorThief class with modified constructor (based on PIL.Image rather than file name)."""
    def __init__(self, img):
        self.image=img


    def get_palette(self, color_count=10, quality=10):
        
        pixels = self.image.getdata()

        # Send array to quantize function which clusters values
        # using median cut algorithm
        cmap = MMCQ.quantize(pixels, color_count)
        return cmap.palette
