# PERCEPTRON

This program implements a linear classifier algorithm that can differentiate between circles and rectangles. The algorithm is based on the Perceptron model, which is a type of neural network that learns by adjusting weights to classify input data.


## Dependencies

The only dependency required to run this program is PIL (Pillow). We believe in keeping dependencies to a minimum to reduce unnecessary complexity.

## Implementation

### Generating the dataset
To train the algorithm, we need to generate two types of images: circles and rectangles. For circles, we use the PIL library to create 20x20 images with varying configurations of radius and center coordinates. The circle is defined by the equation:
```
(x-a)^2 + (y-b)^2 <= r^2
```
For rectangles, we generate images with a random size and position. The rectangle is defined by the equation:

```
|x-a| <= q and |y-b| <= p
```

### Applying the algorithm
To test the algorithm, we randomly select an image with a shape (either circle or rectangle) and run it through the algorithm. The algorithm then adjusts its weights based on whether the classification was correct or not. We continue this process until the algorithm can accurately classify all images.

*For more information on the Perceptron algorithm, please refer to the [Wikipedia article](https://wikipedia.org/wiki/Perceptron).*
