# przepicture
Przepicture provides four methods of image transformations.


1. Blurring
2. Changing lighteness
3. Changing saturation
4. Triangulation with Delaunay method


First three apply effects on shape-based maps (rectangles or triangles). Triangulation replicates the images with best triangle-based split.


Triangulation inspired by
![Iain Barr](https://github.com/ijmbarr)


## Results of shape-based effects
Result of blur by 50 degrees on rectangles map:

![blur](output/pexels-rodrigo-souza-2531608_blur.jpg?raw=true)

Result of lighten by 1.5 degree on triangles map:

![lighten](output/pexels-eberhard-grossgasteiger-844297_lighten.jpg?raw=true)

Result of saturation by 5 degree on rectangles map:

![saturation](output/pexels-simon-berger-1323550_saturate.jpg?raw=true)


## Results of triangulation

Original picture:

![original](input/pexels-caio-56733.jpg?raw=true)


500 points triangulation:

![500points](output/pexels-caio-56733_triangulated_500.jpg?raw=true)


1000 points triangulation:

![1000points](output/pexels-caio-56733_triangulated_1000.jpg?raw=true)


5000 points triangulation:

![5000points](output/pexels-caio-56733_triangulated_5000.jpg?raw=true)


## Results of methods combinations
![example1](output/pexels-simon-berger-1323550_example1.jpg?raw=true)

![example2](output/pexels-eberhard-grossgasteiger-844297_example2.jpg?raw=true)

![example3](output/pexels-simon-berger-1323550_example3.jpg?raw=true)

![example4](output/pexels-michael-block-3225517_example4.jpg?raw=true)

![example5](output/pexels-caio-56733_example5.jpg?raw=true)


Above pictures were created using codes privided in ![example.py](example.py?raw=true) file.




