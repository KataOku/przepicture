from colorthief import ColorThief

class ImageBasedColorThief(ColorThief):
    """ColorThief class with modified constructor (based on PIL.Image rather than file name)."""
    def __init__(self, img):
        self.image=img