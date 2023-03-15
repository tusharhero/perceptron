# PERCEPTRON

This program will implement a linear classifier algorithm and this program can differentiate between a circle and a rectangle.

[wikipedia article explaining this algorithm.](https://wikipedia.org/wiki/Perceptron)

## dependencies
- PIL (Pillow)

No really, I *hate* programs which have a lot of dependencies for no good reason.

## Implementation

To generate the data set to train our algorithm, we will need to generate a few data sets.

- circle
- rectangle

### circle

We will use pillow generate the 20x20 images of circle with different configuration(i'e varying a,b,r).

```
 (x-a)^2 + (y-b)^2 <= r^2
```

### rectangle

we will need to generate rectangles.
