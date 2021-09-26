from picture import Picture
pic = Picture("img/pexels-michael-block-3225517.jpg")

pic.blur(10, 10)
pic.lighten(12)
pic.saturation(8)

pic.image.show()
