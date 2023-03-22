"""
The GPLv3 License (GPLv3)

Copyright (c) 2023 Tushar Maharana

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from PIL import Image as im
import random as ran


def getfilename(
    shape, var=100, step=5
):  # select random files from dataset. (This is possible because they follow a specific naming rule.)
    filename = ""
    if shape == "circle":
        a = ran.randrange(0, var, step)
        b = ran.randrange(0, var, step)
        r = ran.randrange(0, var, step)
        filename = f"circles/({a},{b},{r}).png"
    if shape == "rectangle":
        a = ran.randrange(0, var, step)
        b = ran.randrange(0, var, step)
        c = ran.randrange(0, var, step)
        d = ran.randrange(0, var, step)
        filename = f"rectangles/({a},{b},{c},{d}).png"
    return filename


def list_float2int(list):  # convert each elemenet of the list into an integer
    intlist = []
    for i in list:
        intlist.append(int(i))
    return intlist


def genrandweight(size):  # randomly generate weight for first run
    weight = []
    for i in range(size[0] * size[1]):
        weight.append(ran.randint(-1, 1))
    return weight


def getfilecontent(filepath):
    with open(filepath) as fp:
        text = fp.read()
    return text


def multiply(weight, image_list, size=(100, 100)):
    product = 0
    for i in range(size[0] * size[1]):
        product += weight[i] * image_list[i]
    return product


def addition(weight, image_list, SubOrAdd=1, size=(100, 100)):
    sum = []
    for i in range(size[0] * size[1]):
        sum.append(weight[i] + (image_list[i] * SubOrAdd))
    return sum


def normalize(list, factor):  # fit it in the range of [0,1]
    normalized_list = []
    for i in list:
        normalized_list.append(i / 255 * factor)
    return normalized_list


def getimage_list(image):
    image_list = normalize(list((image.getdata())), 1)
    return image_list


def guess(imagepath, weight, bias=100, shapes=("circle", "rectangle")):
    image_list = getimage_list(im.open(imagepath).convert("L"))
    product = multiply(weight, image_list)

    if product + bias > 0:
        predict_shape = shapes[0]
        guess = 0
    else:
        predict_shape = shapes[1]
        guess = 1
    return guess


def train(
    bias=1000,
    enouchs=10000,
    weightpath="",
    size=(100, 100),
    shapes=("circle", "rectangle"),
    image_converstion=False,
):
    # load weight from file or generate randomly
    if len(weightpath) == 0:
        weight = genrandweight(size)
        weightpath = "weight"
    else:
        weight = eval(getfilecontent("weight"))

    correct_guesses = 0

    # Read Wikipedia article linked in README.md
    for i in range(enouchs):
        shape = shapes[ran.randrange(2)]
        filename = getfilename(shape)
        image = image.open(filename)

        if image_converstion:
            image.convert("L")
        image_list = getimage_list(image)

        product = multiply(weight, image_list)

        print(product)

        if product + bias > 0:
            predict_shape = shapes[0]
            if shape != predict_shape:
                weight = addition(weight, image_list, -1)
        else:
            predict_shape = shapes[1]
            if shape != predict_shape:
                weight = addition(weight, image_list, +1)

        if shape == predict_shape:
            correct_guesses += 1

        if i % 1000 == 0:  # log and save every 1000 enouchs
            weight_viz = im.new("RGB", size)
            weight_viz.putdata(list_float2int(weight))
            weight_viz.save("weight.png")

            with open(weightpath, "w") as w:
                w.write(str(weight))

            with open("log", "a") as log:
                log.write(
                    f"{correct_guesses/(i+1)}; {i/(enouchs+1) * 100}% := {filename}\n"
                )

        print(i, correct_guesses, predict_shape, shape)
