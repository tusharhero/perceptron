# PERCEPTRON

This program implements a linear classifier algorithm that can differentiate between circles and rectangles. The algorithm is based on the Perceptron model, which is a type of neural network that learns by adjusting weights to classify input data.


## Dependencies

The only dependency required to run this program is PIL (Pillow). We believe in keeping dependencies to a minimum to reduce unnecessary complexity.

## Usage

1. Clone the repository by running the following command:

```
git clone https://github.com/tusharhero/perceptron.git
```
2. Navigate to the project directory:

```
cd perceptron
```
3. Train the model by running the following command:

```
python train.py
```
This will train the model using the default dataset and save the trained weights to disk.

4. Test the model by running the following command:

```
python test.py /path/to/weights /path/to/image
```
Replace `/path/to/weights` with the location of the trained weights file( `./weight` by default), and `/path/to/image` with the location of the test image. This will run the model on the test image and display the results. 

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
