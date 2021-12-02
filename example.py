import picture

# Example of blur by 50 degrees on rectangles map.
pic1 = picture.Picture("input/pexels-rodrigo-souza-2531608.jpg")
pic1.blur("rectangles", 4, degree=50)
pic1.image.save("output/pexels-rodrigo-souza-2531608_blur.jpg")

# Example of lighten by 1.5 degree on triangles map.
pic2 = picture.Picture("input/pexels-eberhard-grossgasteiger-844297.jpg")
pic2.lighten("triangles",4, degree=1.5)
pic2.image.save("output/pexels-eberhard-grossgasteiger-844297_lighten.jpg")

# Example of saturation by 5 degree on rectangles map.
pic3 = picture.Picture("input/pexels-simon-berger-1323550.jpg")
pic3.saturate("rectangles",4,degree=5)
pic3.image.save("output/pexels-simon-berger-1323550_saturate.jpg")



#----------   Examples of triangulation   ----------
pic4 = picture.Picture("input/pexels-caio-56733.jpg")            
pic4.triangulate(500)    
pic4.image.save("output/pexels-caio-56733_triangulated_500.jpg")

pic5 = picture.Picture("input/pexels-caio-56733.jpg")            
pic5.triangulate(1000)
pic5.image.save("output/pexels-caio-56733_triangulated_1000.jpg")

pic6 = picture.Picture("input/pexels-caio-56733.jpg")            
pic6.triangulate(5000)
pic6.image.save("output/pexels-caio-56733_triangulated_5000_loerdist02.jpg")



##----------   Examples of combined blur, lighten and saturation methods used with different shape masks.   ----------
# Example 1
pic7 = picture.Picture("input/pexels-simon-berger-1323550.jpg")
pic7.saturate("rectangles",4,degree=4)
pic7.saturate("triangles",4,degree=0)
pic7.image.save("output/pexels-simon-berger-1323550_example1.jpg")

# Example 2
pic8 = picture.Picture("input/pexels-eberhard-grossgasteiger-844297.jpg")
pic8.lighten("triangles",20)
pic8.blur("rectangles", 20)
pic8.saturate("rectangles", 10)
pic8.image.save("output/pexels-eberhard-grossgasteiger-844297_example2.jpg")

# Example 3
pic9 = picture.Picture("input/pexels-simon-berger-1323550.jpg")
pic9.lighten("rectangles",20,vCount=40)
pic9.blur("rectangles", 20, vCount=40)
pic9.image.save("output/pexels-simon-berger-1323550_example3.jpg")

# Example 4
pic10 = picture.Picture("input/pexels-michael-block-3225517.jpg")
pic10.lighten("triangles", 12, vCount=16)
pic10.blur("rectangles", 6, 20, vCount=8)
pic10.image.save("output/pexels-michael-block-3225517_example4.jpg")

# Example 5
pic11 = picture.Picture("input/pexels-caio-56733.jpg")
pic11.blur("rectangles", 2, degree=150)
pic11.triangulate(5000)
pic11.image.save("output/pexels-caio-56733_example5.jpg")
