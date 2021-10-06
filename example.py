import picture


pic1 = picture.Picture("img/pexels-rodrigo-souza-2531608.jpg")
pic1.blur("triangles", 1)
pic1.saturation("triangles", 5, 0.4)
pic1.saturation("triangles", 1, 1.4)
pic1.lighten("triangles",1, 1.5)
pic1.image.show()

pic2 = picture.Picture("img/pexels-eberhard-grossgasteiger-844297.jpg")
pic2.lighten("triangles",20)
pic2.blur("squares", 20)
pic2.saturation("squares", 10)
pic2.image.show()

pic3 = picture.Picture("img/pexels-simon-berger-1323550.jpg")
pic3.lighten("squares",20,vCount=40)
pic3.blur("squares", 20, vCount=40)
pic3.image.show()

pic4 = picture.Picture("img/pexels-michael-block-3225517.jpg")
pic4.lighten("triangles", 12, vCount=16)
pic4.blur("squares", 6, 20, vCount=8)
# pic4.saturation("squares", 10)
pic4.image.show()